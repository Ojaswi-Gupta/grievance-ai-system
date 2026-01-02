from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config.settings import settings
from app.api.complaints import router as complaints_router
from app.services.feedback_service import init_feedback_db
from app.api.feedback import router as feedback_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(complaints_router)
app.include_router(feedback_router)


@app.on_event("startup")
def startup_event():
    init_feedback_db()


@app.get("/", include_in_schema=False)
def root():
    return {"message": "Grievance AI Backend is running"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("app/static/favicon.ico")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "grievance-ai-backend",
        "environment": settings.ENVIRONMENT
    }
