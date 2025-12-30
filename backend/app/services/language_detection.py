from langdetect import detect, DetectorFactory

# Make detection deterministic
DetectorFactory.seed = 0

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "te": "Telugu"
}

def detect_language(text: str) -> dict:
    try:
        lang_code = detect(text)
    except Exception:
        lang_code = "unknown"

    return {
        "language_code": lang_code,
        "language_name": SUPPORTED_LANGUAGES.get(lang_code, "Unknown")
    }
