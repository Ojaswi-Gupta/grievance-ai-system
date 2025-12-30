from fastapi import APIRouter
from app.core.schemas import ComplaintInput
from app.services.pii_masking import mask_pii
from app.services.language_detection import detect_language
from app.services.text_normalization import normalize_text
from app.services.classification_service import classify_complaint
from app.services.priority_service import predict_priority
from app.services.retrieval_service import retrieve_context
from app.services.response_service import generate_response

router = APIRouter(prefix="/complaints", tags=["Complaints"])


@router.post("/submit")
def submit_complaint(payload: ComplaintInput):

    # Step 1: PII masking
    pii_result = mask_pii(payload.complaint_text)

    # Step 2: Language detection
    language_info = detect_language(pii_result["masked_text"])

    # Step 3: Text normalization
    normalization = normalize_text(
        pii_result["masked_text"],
        language_info["language_code"]
    )

    # Defaults (IMPORTANT for governance)
    ai_result = None
    priority = None
    response_draft = None

    # Step 4: AI classification (assistive, English-only)
    if language_info["language_code"] == "en":
        ai_result = classify_complaint(normalization["normalized_text"])

    # Step 5: Priority + response draft (ONLY if AI ran)
    if ai_result:
        priority = predict_priority(
            confidence=ai_result["confidence_score"],
            department=ai_result["predicted_department"],
            complaint_length=len(payload.complaint_text),
            time_keywords=1 if "day" in payload.complaint_text.lower() else 0
        )

        retrieved = retrieve_context(payload.complaint_text)

        response_draft = generate_response(
            complaint_text=payload.complaint_text,
            department=ai_result["predicted_department"],
            priority=priority,
            retrieved_context=retrieved["context"]
        )

    # Final response (human-in-the-loop)
    return {
        "status": "processed",
        "language": language_info,
        "pii_analysis": pii_result,
        "ai_classification": {
            "suggestion": ai_result,
            "requires_human_review": True
        },
        "priority": {
            "suggestion": priority,
            "requires_human_review": True
        },
        "draft_response": {
            "content": response_draft,
            "auto_send": False
        }
    }
