def match_skills(resume_skills, job_desc):

    job_desc = job_desc.lower()

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:
        if skill in job_desc:
            matched_skills.append(skill)

    for word in job_desc.split():
        if word not in resume_skills:
            if word in ["python","sql","flask","html","css","javascript","docker","aws","pandas","numpy"]:
                missing_skills.append(word)

    if len(resume_skills) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(resume_skills)) * 100

    return matched_skills, missing_skills, round(score,2)