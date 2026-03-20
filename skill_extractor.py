def extract_skills(text):
    skills = [
        "python", "sql", "flask", "html", "css", "javascript",
        "machine learning", "data analysis", "pandas", "numpy"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills