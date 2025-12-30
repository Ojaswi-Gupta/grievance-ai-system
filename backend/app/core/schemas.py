from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ComplaintInput(BaseModel):
    complaint_text: str = Field(..., min_length=10, max_length=5000)
    source: Optional[str] = Field(default="manual")
    submitted_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
