from fastapi.testclient import TestClient

import main


def test_health():
    client = TestClient(main.app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_loads():
    client = TestClient(main.app)

    response = client.get("/")

    assert response.status_code == 200
    assert "Sentiment Studio" in response.text


def test_predict_without_groq_key(monkeypatch):
    monkeypatch.setattr(main, "groq_client", None)
    client = TestClient(main.app)

    response = client.post("/predict", json={"text": "This workshop is helpful"})

    assert response.status_code == 200
    body = response.json()
    assert body["label"] == "POSITIVE"
    assert body["score"] > 0
    assert "GROQ_API_KEY" in body["roast"]

