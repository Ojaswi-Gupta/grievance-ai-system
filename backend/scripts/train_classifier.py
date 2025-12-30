import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder
from datasets import Dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)

# Load data
# df = pd.read_csv("app/data/training_data.csv")
df = pd.read_csv("app/data/training_data_sanitized.csv")


# Encode labels
label_encoder = LabelEncoder()
df["label_encoded"] = label_encoder.fit_transform(df["label"])

# Save label mapping (VERY IMPORTANT)
label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
pd.Series(label_mapping).to_json("app/models/label_mapping.json")

# Convert to HF dataset
dataset = Dataset.from_pandas(df[["text", "label_encoded"]])

# Load tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label_encoded", "labels")
dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

# Train/test split
dataset = dataset.train_test_split(test_size=0.2)

# Load model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(label_encoder.classes_)
)

# # Training config (CPU friendly)
training_args = TrainingArguments(
    output_dir="app/models",
    eval_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=4,          # ⬅️ increased
    learning_rate=2e-5,          # stable for larger data
    logging_steps=20,
    save_strategy="epoch",
    save_total_limit=1,
    load_best_model_at_end=True,
    report_to="none",
    seed=42
)



# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"]
)

# Train
trainer.train()

# Save model
model.save_pretrained("app/models/complaint_classifier")
tokenizer.save_pretrained("app/models/complaint_classifier")

print("Training complete. Model saved.")
