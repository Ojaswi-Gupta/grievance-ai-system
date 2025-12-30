# import torch
# import json
# from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
# import torch.nn.functional as F

# MODEL_PATH = "app/models/complaint_classifier"
# LABEL_MAPPING_PATH = "app/models/label_mapping.json"

# # Load tokenizer and model (ONCE)
# tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
# model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
# model.eval()

# # Load label mapping
# with open(LABEL_MAPPING_PATH, "r") as f:
#     label_mapping = json.load(f)

# # Reverse mapping: index → label
# id_to_label = {v: k for k, v in label_mapping.items()}


# def classify_complaint(text: str) -> dict:
#     inputs = tokenizer(
#         text,
#         return_tensors="pt",
#         truncation=True,
#         padding=True
#     )

#     with torch.no_grad():
#         outputs = model(**inputs)

#     logits = outputs.logits
#     probabilities = F.softmax(logits, dim=1)

#     confidence, predicted_id = torch.max(probabilities, dim=1)

#     return {
#         "predicted_department": id_to_label[predicted_id.item()],
#         "confidence_score": round(confidence.item(), 4),
#         "all_probabilities": {
#             id_to_label[i]: round(probabilities[0][i].item(), 4)
#             for i in range(len(id_to_label))
#         }
#     }


import torch
import json
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch.nn.functional as F

MODEL_PATH = "app/models/complaint_classifier"
LABEL_MAPPING_PATH = "app/models/label_mapping.json"

# Load tokenizer and model (ONCE)
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# Load label mapping
with open(LABEL_MAPPING_PATH, "r") as f:
    label_mapping = json.load(f)

# Reverse mapping: index → label
id_to_label = {v: k for k, v in label_mapping.items() if isinstance(v, int)}

def confidence_level(score: float) -> str:
    if score >= 0.75:
        return "HIGH"
    elif score >= 0.5:
        return "MEDIUM"
    else:
        return "LOW"

def extract_reasoning(text: str):
    keywords = [
        "delay", "late", "slow", "damaged", "broken", "lost",
        "missing", "money order", "bank", "account", "customs",
        "international", "staff", "rude"
    ]
    text_lower = text.lower()
    return [kw for kw in keywords if kw in text_lower]

def classify_complaint(text: str) -> dict:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = F.softmax(logits, dim=1)

    confidence, predicted_id = torch.max(probabilities, dim=1)
    confidence_score = round(confidence.item(), 4)

    num_labels = probabilities.shape[1]

    return {
        "predicted_department": id_to_label[predicted_id.item()],
        "confidence_score": confidence_score,
        "confidence_level": confidence_level(confidence_score),
        "reasoning_summary": extract_reasoning(text),
        "all_probabilities": {
            id_to_label[i]: round(probabilities[0][i].item(), 4)
            for i in range(num_labels)
        }
    }
