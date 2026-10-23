from main import app

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


# Expected values come from the business contract, not calculate_discount().
# Each pytest ID corresponds to the case table presented in the review.
@pytest.mark.parametrize(
    "amount, expected_discount, expected_payable",
    [
        pytest.param(5000, 0, 5000, id="Q01"),
        pytest.param(20000, 1000, 19000, id="Q02"),
        pytest.param(1, 0, 1, id="Q03"),
        pytest.param(100000, 1000, 99000, id="Q04"),
        pytest.param(9999, 0, 9999, id="Q05"),
        pytest.param(10000, 1000, 9000, id="Q06"),
        pytest.param(10001, 1000, 9001, id="Q07"),
    ],
)
def test_quote_contract(client, amount, expected_discount, expected_payable):
    response = client.post("/quotes", json={"amount": amount})

    assert response.status_code == 200
    assert response.json() == {
        "amount": amount,
        "discount": expected_discount,
        "payable": expected_payable,
    }


@pytest.mark.parametrize(
    "body",
    [
        pytest.param({"amount": 0}, id="Q08"),
        pytest.param({"amount": 100001}, id="Q09"),
        pytest.param({}, id="Q10"),
        pytest.param({"amount": "10000"}, id="Q11"),
        pytest.param({"amount": 10000.0}, id="Q12"),
        pytest.param({"amount": 1.5}, id="Q13"),
        pytest.param({"amount": True}, id="Q14"),
        pytest.param({"amount": False}, id="Q15"),
        pytest.param({"amount": None}, id="Q16"),
    ],
)
def test_quote_rejects_invalid_amount(client, body):
    response = client.post("/quotes", json=body)

    assert response.status_code == 422
    # Supplemental check follows the provided test's FastAPI error format.
    # Exact error wording is not specified by the business contract.
    detail = response.json()["detail"]
    assert isinstance(detail, list)
    assert any(error["loc"] == ["body", "amount"] for error in detail)
