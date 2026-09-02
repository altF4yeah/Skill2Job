import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize the new Google GenAI client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume_with_ai(resume_text, target_role):
    # Added stricter JSON formatting instructions to prevent parsing errors
    prompt = f"""
    You are an expert career counselor and technical recruiter. Analyze the following resume text against the target role of '{target_role}'.
    Return the response strictly as a JSON object with the following exact keys:
    "match_score" (integer 0-100),
    "extracted_skills" (list of strings),
    "strengths" (list of strings),
    "weaknesses" (list of strings)
    
    Resume Text:
    {resume_text}
    """
    
    try:
        # The new generate_content syntax
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt
        )
        
        # Clean up Markdown formatting from the AI response
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned_text)
        
    except Exception as e:
        print(f"AI Analysis Error: {e}")
        return {
            "match_score": 0,
            "extracted_skills": ["Error extracting skills"],
            "strengths": ["AI Service Unavailable"],
            "weaknesses": ["AI Service Unavailable"]
        }