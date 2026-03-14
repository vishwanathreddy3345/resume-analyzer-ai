def resume_suggestions(resume_skills):

    suggestions = []

    if "python" in resume_skills and "flask" not in resume_skills:
        suggestions.append("Consider adding a backend framework like Flask or Django.")

    if "sql" not in resume_skills:
        suggestions.append("Database skills like SQL are highly recommended.")

    if "docker" not in resume_skills:
        suggestions.append("Learning Docker can improve deployment skills.")

    if "aws" not in resume_skills:
        suggestions.append("Cloud platforms like AWS are commonly required.")

    if len(resume_skills) < 5:
        suggestions.append("Add more technical skills to strengthen your resume.")

    return suggestions