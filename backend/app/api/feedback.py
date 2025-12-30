from fastapi import APIRouter
from app.core.feedback_schema import FeedbackInput
from app.services.feedback_service import store_feedback

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/submit")
def submit_feedback(feedback: FeedbackInput):
    store_feedback(feedback)
    return {
        "status": "feedback recorded",
        "message": "Thank you. Feedback will be used for periodic model improvement."
    }
