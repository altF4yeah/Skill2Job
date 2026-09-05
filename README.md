***🚀 Skill2Job – AI Powered Career Assistant***

Transform Your Skills Into Your Career.

Skill2Job is an AI-powered career assistant that analyzes a user's resume, identifies strengths and skill gaps, recommends suitable career paths, and generates a personalized learning roadmap to help users become job-ready.

Built for a hackathon project using HTML, CSS, JavaScript, Flask, Python, MySQL, and Gemini AI.

**🌟 Features**

📄 Resume Analysis – Upload a PDF or DOCX resume and extract skills using AI.
🧠 AI Skill Evaluation – Identify strengths and weaknesses from the resume.
💼 Career Recommendations – Suggest the most suitable job roles with match percentages.
🛣️ Personalized Roadmap – Generate a step-by-step roadmap for the selected career path.
📊 Progress Tracker – Track completed roadmap steps and learning progress.
🎯 Career Ready Dashboard – View overall resume score, skills, and next learning tasks.

**🛠️ Tech Stack**

Frontend	Backend	Database	AI
HTML5	Flask	MySQL	Gemini AI
CSS3	Python	SQLAlchemy	Google Generative AI
JavaScript	Flask-CORS	MySQL Connector	

**📁 Project Structure**
```
skill2jobb/
│
├── backend/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── resume.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_parser.py
│   │   ├── resume_parser.py
│   │   └── skill_extractor.py
│   │
│   ├── uploads/
│   ├── venv/
│   ├── .env
│   ├── .gitignore
│   ├── app.py
│   ├── models.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── instance/
│   └── skill2job.db
│
└── uploads/
```
**⚙️ Installation & Setup**

1️⃣ Clone the Repository
git clone <repository-url>
cd SKILL2JOB
2️⃣ Create Virtual Environment
cd BACKEND
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables
Create a .env file inside the BACKEND folder.

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
PORT=5001
5️⃣ Setup MySQL Database
Open database_setup.py and add your MySQL password.

password="YOUR_PASSWORD"
Run:

cd database
python3 database_setup.py
6️⃣ Start Backend Server
cd ..
python3 app.py
Backend runs at:

http://127.0.0.1:5001
7️⃣ Run Frontend
Open FRONTEND/INDEX.html using Live Server in VS Code.

Frontend runs at:

http://127.0.0.1:5500/INDEX.html
🔄 Application Workflow
User registers or logs in.

User uploads a resume (PDF/DOCX).

Resume text is extracted using Python.

Gemini AI analyzes the resume.

**Dashboard displays:**

Skills
Strengths
Weaknesses
Suggested Job Roles
Resume Score
User selects a career path.

Skill2Job generates a personalized roadmap.

User tracks progress until becoming Career Ready.

**📊 Database Modules**

Users – Authentication and login details.
Resumes – Uploaded resumes and extracted text.
Analysis Reports – AI-generated strengths, weaknesses, and recommendations.
Jobs – Career role master table.
Required Skills – Skills required for each role.
Roadmaps – Learning roadmap for each career path.
Progress Tracker – User learning progress.

**🎯 Future Improvements**

Resume ATS Score.
Interview Question Generator.
Course Recommendations.
Job & Internship Recommendation Portal.
PDF Report Download.
User Profile Dashboard.

**👩‍💻 Team**
Skill2Job – Hackathon Project

Developed by the Skill2Job Team using AI-powered career guidance to help students become job-ready.

**📌 License**
This project is developed for educational and hackathon purposes.
