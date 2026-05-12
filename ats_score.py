def calculate_ats(skills):

    total_skills = 16

    score = (len(skills) / total_skills) * 100

    if score > 100:
        score = 100

    return round(score, 2)