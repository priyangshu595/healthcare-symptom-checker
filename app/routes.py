from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_service import analyze_symptoms
from app.utils import check_emergency
from app.db import save_query

router = APIRouter()

class SymptomRequest(BaseModel):
    symptoms: str

@router.post("/analyze-symptoms")
def analyze(request: SymptomRequest):
    try:
        emergency = check_emergency(request.symptoms)
        result = analyze_symptoms(request.symptoms)
        save_query(request.symptoms, result)

        return {
            "emergency": emergency,
            "data": result
        }

    except Exception as e:
        return {
            "emergency": False,
            "data": {
                "conditions": [],
                "recommendations": [],
                "doctor_visit": "",
                "disclaimer": "Error occurred",
                "error": str(e)
            }
        }
