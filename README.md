Skill2Job — AI Career Assistant & Resume Analyzer
Skill2Job is an AI-powered web platform designed to bridge the gap between academic resumes and industry expectations. It parses uploaded resumes, extracts technical and soft skills, evaluates alignment against target career roles, and generates personalized development insights.

1. Overview & Key Features
Resume Ingestion: Supports extraction from both .pdf and .docx document formats.

AI-Driven Skill Extraction: Identifies technical proficiencies and interpersonal capabilities.

Gap Analysis & Scoring: Computes an objective match percentage with explicit strengths and weaknesses.

Structured Roadmap: Generates step-by-step milestones to help candidates achieve job readiness.

2. Tech Stack & Directory Structure
Frontend: Vanilla HTML5, CSS3, Modern JavaScript (Fetch API).

Backend: Python, Flask, Flask-CORS, Flask-SQLAlchemy, SQLite.

Document Processing: PyPDF2, python-docx.

Intelligence Layer: Google GenAI SDK (google-genai).

Plaintext
Skill2Job/
├── frontend/
│   └── index.html
└── backend/
    ├── .env
    ├── .gitignore
    ├── app.py
    ├── models.py
    ├── requirements.txt
    ├── routes/
    │   ├── auth.py
    │   └── resume.py
    ├── services/
    │   ├── ai_service.py
    │   ├── parser_service.py
    │   └── skill_extractor.py
    └── uploads/
3. Installation & Configuration
Clone and prepare environment:

Bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Environment configuration (backend/.env):
Create a .env file in the backend/ directory:

Code snippet
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_APP=app.py
FLASK_ENV=development
4. API Endpoints & Execution
Start the server:

Bash
python app.py
The Flask server initializes SQLite (skill2job.db) and serves API routes on [http://127.0.0.1:5000](http://127.0.0.1:5000).

Primary Endpoints:

POST /api/auth/register — Creates user credentials with hashed passwords.

POST /api/auth/login — Authenticates returning users.

POST /api/resume/analyze — Accepts multipart/form-data (resume file and role string) to return structured JSON analysis.

Client Access:
Open frontend/index.html in any browser or serve it directly via Flask at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

Would you like to add a Docker configuration file or deployment instructions for platforms like Render or AWS?
