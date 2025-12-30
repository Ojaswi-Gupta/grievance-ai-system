import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from app.services.classification_service import classify_complaint

test_cases = [
    "My parcel was delayed for more than 10 days",
    "Money order was deducted but not delivered",
    "My bank account was charged incorrectly",
    "The package arrived damaged and torn",
    "International shipment is stuck at customs",
    "A high value money order I sent to my landlord has not been credited and rent is already overdue with an eviction warning"
]

for text in test_cases:
    result = classify_complaint(text)
    print("\nTEXT:", text)
    print("PREDICTION:", result)
