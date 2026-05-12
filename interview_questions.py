def generate_questions(skills):

    questions = []

    question_bank = {

        "python": [
            "Explain list vs tuple in Python.",
            "What are Python decorators?",
            "Explain OOP concepts in Python."
        ],

        "sql": [
            "What is JOIN in SQL?",
            "Difference between DELETE and TRUNCATE?",
            "What is normalization?"
        ],

        "html": [
            "What is semantic HTML?",
            "Difference between div and span?"
        ],

        "css": [
            "What is Flexbox?",
            "Difference between Grid and Flexbox?"
        ],

        "javascript": [
            "Explain closures in JavaScript.",
            "Difference between var, let, and const?"
        ],

        "machine learning": [
            "What is overfitting?",
            "Difference between supervised and unsupervised learning?"
        ],

        "ai": [
            "What is Artificial Intelligence?",
            "Explain neural networks."
        ],

        "c++": [
            "Explain pointers in C++.",
            "What is polymorphism?"
        ],

        "java": [
            "Explain JVM.",
            "Difference between abstract class and interface?"
        ]
    }

    for skill in skills:

        if skill.lower() in question_bank:
            questions.extend(question_bank[skill.lower()])

    return questions