import json
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://your-app-name.com",  # can be anything
        "X-Title": "Healthcare Symptom Checker"
    }
)

def analyze_symptoms(symptoms: str):
    try:
        prompt = f"""
        You are a medical assistant (educational purpose only).

        Symptoms: {symptoms}

        Return JSON:
        {{
            "conditions": [
                {{"name": "...", "description": "...", "severity": "..."}}
            ],
            "recommendations": ["...", "..."],
            "doctor_visit": "...",
            "disclaimer": "This is not medical advice"
        }}
        """

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # 🔥 IMPORTANT
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content

        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)

    except Exception as e:
        return {
            "conditions": [
                {
                    "name": "Fallback Response",
                    "description": "Could not fetch AI response",
                    "severity": "low"
                }
            ],
            "recommendations": ["Try again"],
            "doctor_visit": "Consult doctor if serious",
            "disclaimer": "This is not medical advice",
            "error": str(e)
        }