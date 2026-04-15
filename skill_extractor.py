import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

def load_skills(file_path):
    with open(file_path, "r") as f:
        return list(set([line.strip().lower() for line in f]))

def extract_skills(text, skills_list):
    doc = nlp(text)

    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in skills_list]
    matcher.add("SKILLS", patterns)

    found_skills = set()

    # Phrase Matching
    matches = matcher(doc)
    for _, start, end in matches:
        found_skills.add(doc[start:end].text.lower())

    # NER support
    for ent in doc.ents:
        cleaned = ent.text.lower().strip()
        if ent.label_ in ["ORG", "PRODUCT"]:
            for skill in skills_list:
                if cleaned in skill or skill in cleaned:
                    found_skills.add(skill)

    return sorted(found_skills)
