import os
from flask import Flask, render_template, request
import matplotlib.pyplot as plt

# project modules
from skill_extractor import extract_skills
from matcher import match_skills
from suggestions import resume_suggestions
from job_recommender import recommend_jobs
from keyword_analyzer import keyword_density
from report_generator import generate_report
from database import init_db, save_analysis

import PyPDF2
import os

# port = int(os.environ.get("PORT", 10000))

# app.config['SERVER_NAME'] = None

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Vishwas48'

# initialize database
init_db()

# folder to store uploaded resumes
UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_text_from_pdf(filepath):

    text = ""

    with open(filepath, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")




# -----------------------------
# Resume Analysis
# -----------------------------
@app.route("/analyze", methods=["GET","POST"])
def analyze():

    file = request.files["resume"]

    job_desc = request.form["job_desc"]

    # save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    # extract resume text
    resume_text = extract_text_from_pdf(filepath)

    # keyword density
    keywords = keyword_density(resume_text)

    # extract skills
    resume_skills = extract_skills(resume_text)

    # match skills
    matched_skills, missing_skills, score = match_skills(resume_skills, job_desc)

    # suggestions
    suggestions = resume_suggestions(resume_skills)

    # recommended roles
    recommended_roles = recommend_jobs(resume_skills)

    # save analysis to database
    save_analysis(resume_skills, score)

    # generate report
    report = generate_report(resume_skills, score)

    # chart generation
    labels = ["Matched Skills", "Missing Skills"]
    values = [len(matched_skills), len(missing_skills)]

    plt.bar(labels, values)
    plt.title("Skill Match Analysis")

    chart_path = "static/chart.png"

    plt.savefig(chart_path)

    plt.close()

    return render_template(
        "result.html",
        skills=resume_skills,
        matched=matched_skills,
        missing=missing_skills,
        score=score,
        suggestions=suggestions,
        roles=recommended_roles,
        keywords=keywords,
        report=report
    )


# -----------------------------
# Run Flask App
# -----------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)