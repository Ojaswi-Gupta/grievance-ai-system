def normalize_text(text: str, language_code: str) -> dict:
    if language_code == "en":
        return {
            "normalized_text": text,
            "note": "Text is already in English"
        }

    return {
        "normalized_text": None,
        "note": f"Language '{language_code}' detected. Translation required."
    }
