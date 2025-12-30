from fastapi import FastAPI
from app.config.settings import settings
from app.api.complaints import router as complaints_router
from app.services.feedback_service import init_feedback_db
from app.api.feedback import router as feedback_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0"
)

# Include routers
app.include_router(complaints_router)
app.include_router(feedback_router)


# Initialize feedback DB on startup
@app.on_event("startup")
def startup_event():
    init_feedback_db()

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "environment": settings.ENVIRONMENT
    }
