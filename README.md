# Grievance AI System 🚨🤖

An AI-powered backend system for **automated grievance classification, prioritization, and routing**.  
Designed for real-world complaint handling systems such as government portals, enterprises, and large organizations.

This project focuses on **backend intelligence, scalability, and production readiness**, enabling any frontend (web/mobile) to integrate seamlessly.

---

## 🧩 Problem Statement

Organizations receive thousands of grievances daily through emails, portals, and feedback forms.  
Manual triage leads to:

- Delayed responses
- Incorrect routing
- Poor prioritization
- Low user satisfaction

**Grievance AI System** automates this process using NLP and ML models to:
- Classify complaints
- Detect grievance category
- Assign severity & priority
- Route to appropriate departments

---

## ✨ Key Features

- 🧠 **AI-based complaint classification**
- 🏷️ **Automatic category & sub-category detection**
- ⚠️ **Severity & priority prediction**
- 🗂️ **Role-based grievance routing**
- 💬 **Feedback loop for continuous learning**
- 🧪 **SQLite-backed persistence**
- ⚡ **FastAPI-based high-performance backend**

---

## 🏗️ System Architecture

The system follows a backend-first, API-driven architecture. All AI inference,
business logic, and persistence are handled by the backend, while any web or
mobile client communicates via REST APIs.


Client (Web / Mobile)
        |
        |  HTTP / JSON
        v
+----------------------------+
|        FastAPI Backend     |
|----------------------------|
| • Input Validation         |
| • Complaint Analysis API   |
| • Priority & Severity ML   |
| • Routing Logic            |
| • Feedback Handler         |
+-------------+--------------+
              |
              v
+----------------------------+
|     ML Models (NLP)        |
|----------------------------|
| • Complaint Classifier     |
| • Priority Predictor       |
+-------------+--------------+
              |
              v
+----------------------------+
|      SQLite Database       |
|----------------------------|
| • Feedback Data            |
| • Metadata                 |
+----------------------------+


---

## 🛠️ Tech Stack

**Backend**
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

**ML / NLP**
- scikit-learn
- joblib
- custom-trained models

**Database**
- SQLite (dev-ready, easily replaceable)

---

## 📂 Project Structure

grievance_ai_system/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── routes/ # API routes
│ │ ├── models/ # ML models (ignored in git)
│ │ ├── services/ # Inference & logic
│ │ ├── data/ # Runtime data (ignored)
│ │ └── db/ # SQLite handling
│ │
│ └── requirements.txt
│
├── .gitignore
└── README.md



---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Ojaswi-Gupta/grievance-ai-system.git
cd grievance_ai_system

