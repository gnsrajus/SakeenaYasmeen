import pytest

from quiz_module import (
    clean_json_block,
    validate_quiz
)


def test_clean_json_block():

    raw = """
    ```json
    [
        {
            "question": "What is Python?",
            "options": [
                "Language",
                "Database",
                "Browser",
                "Operating System"
            ],
            "answer": "Language"
        }
    ]
    ```
    """

    result = clean_json_block(raw)

    assert result.startswith("[")


def test_validate_quiz_requires_three_questions():

    with pytest.raises(ValueError):

        validate_quiz([])


def test_validate_quiz_accepts_valid_data():

    data = [

        {
            "question": "Question 1",

            "options": [
                "A",
                "B",
                "C",
                "D"
            ],

            "answer": "A"
        },

        {
            "question": "Question 2",

            "options": [
                "A",
                "B",
                "C",
                "D"
            ],

            "answer": "B"
        },

        {
            "question": "Question 3",

            "options": [
                "A",
                "B",
                "C",
                "D"
            ],

            "answer": "C"
        }

    ]


    result = validate_quiz(data)


    assert len(result) == 3