from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_send_email():
    response = client.post(
        url='/send_email',
        json={
            "to": "kaidenvlr@gmail.com",
            "subject": "test",
            "message": "TEST"
        }
    )
    assert response.status_code == 200
    assert response.json() == {'status': 'success'}


def test_send_email_incorrect():
    response = client.post(
        url='/send_email',
        json={
            "to": "kaidenvlr@gmail",
            "subject": "test",
            "message": "TEST"
        }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect email'}
