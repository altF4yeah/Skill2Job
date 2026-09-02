import re

# Predefined libraries of industry-standard skills
TECH_SKILLS = [
    "python", "java", "javascript", "html", "css", "sql", "react", "node", 
    "c++", "c#", "aws", "docker", "kubernetes", "machine learning", "ai", 
    "data analysis", "git", "github", "linux", "agile", "cybersecurity"
]

SOFT_SKILLS = [
    "communication", "leadership", "teamwork", "problem solving", 
    "time management", "critical thinking", "adaptability", "management"
]

def extract_skills_fallback(text):
    """
    Fallback method to extract skills using Regex keyword matching.
    """
    text_lower = text.lower()
    found_skills = []
    
    # Search for whole words to prevent partial matches (e.g., 'it' matching inside 'with')
    for skill in TECH_SKILLS + SOFT_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            # Capitalize properly for the frontend
            found_skills.append(skill.title() if skill != "sql" else "SQL")
            
    return list(set(found_skills))