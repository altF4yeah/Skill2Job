from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.resume_parser import extract_text
from services.ai_parser import analyze_resume_with_ai

resume_bp = Blueprint('resume', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@resume_bp.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['resume']
    role = request.form.get('role')
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if not role or role == "Select Career Role":
        return jsonify({"error": "Target role is required"}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        
        # 1. Extract Text
        resume_text = extract_text(filepath)
        if not resume_text:
            return jsonify({"error": "Could not read file contents"}), 500
            
        # 2. Analyze with AI
        analysis_results = analyze_resume_with_ai(resume_text, role)
        
        # Clean up file after analysis
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify(analysis_results), 200
        
    return jsonify({"error": "Invalid file type"}), 400