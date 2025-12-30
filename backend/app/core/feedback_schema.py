from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackInput(BaseModel):
    complaint_text: str
    predicted_department: str
    corrected_department: Optional[str] = None
    predicted_priority: str
    corrected_priority: Optional[str] = None
    reviewer_role: str = "officer"
    feedback_time: datetime = datetime.utcnow()
