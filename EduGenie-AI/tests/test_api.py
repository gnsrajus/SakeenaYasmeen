from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_homepage():

    response = client.get("/")

    assert response.status_code == 200

    assert "EduGenie" in response.text


def test_qa_empty_question():

    response = client.post(
        "/qa",
        json={
            "question": ""
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is False


def test_explain_empty_topic():

    response = client.post(
        "/explain",
        json={
            "topic": ""
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is False


def test_quiz_empty_text():

    response = client.post(
        "/quiz",
        json={
            "text": ""
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is False


def test_summary_empty_text():

    response = client.post(
        "/summarize",
        json={
            "text": ""
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is False


def test_learning_path_empty_topic():

    response = client.post(
        "/learn/recommendations",
        json={
            "topic": ""
        }
    )

    assert response.status_code == 200

    assert response.json()["success"] is False