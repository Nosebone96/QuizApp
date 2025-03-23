def get_questions():
    """
    Returns a list of questions for the quiz game.
    Each question is a dictionary with the following keys:
    - text: The question text
    - options: A list of possible answers
    - correct_answer: The correct answer (must be one of the options)
    """
    return [
        {
            "text": "¿Cuál es la capital de Francia?",
            "options": ["París", "Londres", "Madrid", "Berlín"],
            "correct_answer": "París"
        },
        {
            "text": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "options": ["1939", "1945", "1914", "1918"],
            "correct_answer": "1939"
        },
        {
            "text": "¿Cuál es el planeta más grande del sistema solar?",
            "options": ["Júpiter", "Saturno", "Tierra", "Marte"],
            "correct_answer": "Júpiter"
        },
        {
            "text": "¿Quién pintó La Mona Lisa?",
            "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Miguel Ángel"],
            "correct_answer": "Leonardo da Vinci"
        },
        {
            "text": "¿Cuál es el elemento químico más abundante en la Tierra?",
            "options": ["Oxígeno", "Hidrógeno", "Hierro", "Silicio"],
            "correct_answer": "Oxígeno"
        }
    ]

