import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from fastapi import status
from unittest.mock import patch

from app.main import app


@pytest.mark.asyncio
async def test_predict_success():
    test_question = {"ques": "What are the financial highlights for the year 2023?"}

    with patch("app.main.qa_system.get_answer", return_value="Mocked answer"):
        transport = ASGITransport(app=app)

        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/predict", json=test_question)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["question"] == test_question["ques"]
        assert data["answer"] == "Mocked answer"


@pytest.mark.asyncio
async def test_predict_missing_question():
    # Missing 'ques' key in request
    response_body = {}

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/predict", json=response_body)

    assert response.status_code == 422  # Unprocessable Entity (validation error)


@pytest.mark.asyncio
async def test_predict_internal_error():
    test_question = {"ques": "Trigger an error"}

    with patch("app.main.qa_system.get_answer", side_effect=Exception("Something went wrong")):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/predict", json=test_question)

        assert response.status_code == 200  # FastAPI still returns 200 with error JSON
        data = response.json()
        assert "error" in data
        assert data["error"] == "Unable to process your request."
