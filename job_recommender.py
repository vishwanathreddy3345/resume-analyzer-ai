def recommend_jobs(skills):

    roles = []

    if "python" in skills and "flask" in skills:
        roles.append("Backend Developer")

    if "python" in skills and "pandas" in skills:
        roles.append("Data Analyst")

    if "html" in skills and "css" in skills and "javascript" in skills:
        roles.append("Frontend Developer")

    if "python" in skills and "machine learning" in skills:
        roles.append("Machine Learning Engineer")

    return roles