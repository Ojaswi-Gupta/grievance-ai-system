from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

SUPPORTED_ENTITIES = [
    "PERSON",
    "PHONE_NUMBER",
    "EMAIL_ADDRESS",
    "LOCATION",
    "CREDIT_CARD",
    "DATE_TIME"
]

def mask_pii(text: str) -> dict:
    results = analyzer.analyze(
        text=text,
        entities=SUPPORTED_ENTITIES,
        language="en"
    )

    anonymized = anonymizer.anonymize(
        text=text,
        analyzer_results=results
    )

    return {
        "original_text": text,
        "masked_text": anonymized.text,
        "entities_detected": [
            {
                "entity_type": r.entity_type,
                "start": r.start,
                "end": r.end
            } for r in results
        ]
    }
