from iris.core import config

def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={
            "sepal_l": 5.8,
            "sepal_w": 2.7,
            "petal_l": 5.1,
            "petal_w": 1.9
        },
        headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 200
    assert "median_house_value" in response.json()
    assert "currency" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/classification/predict",
        json={},
        headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422