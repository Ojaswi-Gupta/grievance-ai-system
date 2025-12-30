import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)


from app.services.priority_service import predict_priority

# Simulated inputs
confidence = 0.41
department = "Mail-Speed"
complaint_length = 120
time_keywords = 1

priority = predict_priority(
    confidence=confidence,
    department=department,
    complaint_length=complaint_length,
    time_keywords=time_keywords
)

print("Predicted Priority:", priority)
