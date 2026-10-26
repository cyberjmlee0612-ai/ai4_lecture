import pytest
from fastapi.testclient import TestClient
from ai4_lecture.Day8.lesson_04_ai_test_cases.main import app

client = TestClient(app)


@pytest.mark.parametrize("amount, payable", [(5000, 5000), (20000, 19000)])
def test_seed_quote(amount, payable):
    response = client.post("/quotes", json={"amount": amount})
    assert response.status_code == 200
    assert response.json()["payable"] == payable
