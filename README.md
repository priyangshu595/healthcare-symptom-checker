# 🩺 AI Healthcare Symptom Checker

## 🚀 Overview

The **AI Healthcare Symptom Checker** is a web-based application that allows users to input symptoms (in text or paragraph form) and receive:

* Probable medical conditions
* Severity levels
* Recommended next steps

---

## ✨ Key Features

* 🧠 **LLM-powered reasoning** for symptom analysis
* 📥 Accepts **natural language input (paragraph or keywords)**
* ⚠️ **Emergency detection system** (e.g., breathing issues, chest pain)
* 📊 **Structured JSON output** for consistency
* 💾 **Query history storage** using SQLite database
* 🎨 **Interactive frontend UI** built with Streamlit
* 🔁 **Fallback mechanism** for API failures
* 🔐 Secure API handling via environment variables

---

## 🏗️ System Architecture

User Input → FastAPI Backend → LLM Processing → Structured JSON → Streamlit Frontend

---

## 🛠️ Tech Stack

| Layer    | Technology                     |
| -------- | ------------------------------ |
| Backend  | FastAPI                        |
| Frontend | Streamlit                      |
| LLM API  | OpenRouter (OpenAI-compatible) |
| Database | SQLite                         |
| Language | Python                         |

---

## 📂 Project Structure

```bash
healthcare-symptom-checker/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI entry point
│   ├── routes.py        # API endpoints
│   ├── llm_service.py   # LLM integration logic
│   ├── utils.py         # Emergency detection logic
│   ├── db.py            # Database operations
│   ├── config.py        # API key configuration
│
├── frontend/
│   ├── app.py           # Streamlit UI
│
├── history.db           # SQLite database
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/healthcare-symptom-checker.git
cd healthcare-symptom-checker
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add API Key

Update your API key in:

```bash
app/config.py
```

```python
OPENAI_API_KEY = "your_api_key_here"
```

---

## ▶️ Run Locally

### Start Backend

```bash
python -m uvicorn app.main:app --reload
```

---

### Start Frontend

```bash
streamlit run frontend/app.py
```

---

## 📡 API Endpoint

### POST `/analyze-symptoms`

#### Request:

```json
{
  "symptoms": "difficulty breathing, dizziness, fainting"
}
```

#### Response:

```json
{
  "emergency": true,
  "data": {
    "conditions": [
      {
        "name": "Hypoxia",
        "description": "Low oxygen supply in the body",
        "severity": "high"
      }
    ],
    "recommendations": [
      "Seek immediate medical attention"
    ],
    "doctor_visit": "Immediate consultation required",
    "disclaimer": "This is not medical advice"
  }
}
```

---

## 🧠 Design Decisions

* **Structured JSON output** ensures predictable frontend rendering
* **Low temperature LLM setting (0.3)** improves consistency
* **Fallback logic** ensures system reliability during API failure
* **Emergency keyword detection** adds a safety layer
* **Modular architecture** improves scalability and maintainability

---

## 🔒 Safety Considerations

* No definitive diagnosis is provided
* Includes **medical disclaimer** in responses
* Emergency cases trigger alerts
* Designed strictly for **educational use only**

---

## 🚀 Future Enhancements

* 🔍 Retrieval-Augmented Generation (RAG) for medical accuracy
* 🌐 Cloud deployment (Render / Streamlit Cloud)
* 📱 Mobile-friendly UI
* 🔐 User authentication & history dashboard

---

## 🎥 Demo Video

(Add your demo video link here)

---

## 🌐 Live Deployment

(Add your deployed app link here if available)

---

## ⭐ Final Note

This project focuses on **responsible AI usage in healthcare**, combining LLM reasoning, safety mechanisms, and real-world system design to deliver a reliable symptom-checking experience.
