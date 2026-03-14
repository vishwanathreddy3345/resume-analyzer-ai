import spacy

nlp = spacy.load("en_core_web_sm")

skills_db = [
    "python","sql","flask","html","css","javascript",
    "docker","aws","pandas","numpy","machine learning",
    "data analysis"
]

def extract_skills(text):

    doc = nlp(text.lower())

    found_skills = set()

    for token in doc:
        if token.text in skills_db:
            found_skills.add(token.text)

    return list(found_skills)