import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import pandas as pd
from app.services.pii_masking import mask_pii

INPUT_FILE = "app/data/training_data.csv"
OUTPUT_FILE = "app/data/training_data_sanitized.csv"

def sanitize_dataset():
    df = pd.read_csv(INPUT_FILE)

    sanitized_texts = []
    entities_log = []

    for text in df["text"]:
        result = mask_pii(text)
        sanitized_texts.append(result["masked_text"])
        entities_log.append(result["entities_detected"])

    df["text"] = sanitized_texts
    df["pii_entities_removed"] = entities_log

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Sanitized dataset saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    sanitize_dataset()
