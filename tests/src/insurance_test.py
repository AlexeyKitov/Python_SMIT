import json
from http import HTTPStatus

import pytest

from test_data.insurance import (
    parametrize_tariff_post,
    parametrize_calculate_price_get,
    parametrize_insurance_get,
)


@pytest.mark.parametrize("params, expected", parametrize_tariff_post)
@pytest.mark.asyncio
async def test_set_tariff_post(params, expected, make_post_request):
    """
    Заполнение базы тарифами
    """
    response = await make_post_request(target=f"/insurance/set_tariff", json=params)

    assert response.status == expected["status"]
    if not response.status == HTTPStatus.OK:
        assert response.body["detail"][0]["msg"] == expected["msg"]


@pytest.mark.parametrize("params, expected", parametrize_calculate_price_get)
@pytest.mark.asyncio
async def test_calculate_price(params, expected, make_get_request):
    """
    Расчет стоимости страховки
    """
    response = await make_get_request(
        target=f"/insurance/calculate_price", params=params
    )

    assert response.status == expected["status"]
    if not response.status == HTTPStatus.OK:
        assert response.body["detail"][0]["msg"] == expected["msg"]
    else:
        assert response.body == expected["body"]


@pytest.mark.parametrize("params, expected", parametrize_insurance_get)
@pytest.mark.asyncio
async def test_insurance_get(params, expected, make_get_request):
    """
    Получения списк тарифов
    """
    response = await make_get_request(target="/insurance", params=params)
    assert response.status == expected["status"]
    if response.status == HTTPStatus.OK:
        assert len(response.body) == expected["count"]
    else:
        assert response.body["detail"][0]["msg"] == expected["msg"]


@pytest.mark.asyncio
async def test_send_file(make_send_file_request):
    """
    Тест заполнения базы из файла
    """
    response = await make_send_file_request(
        target="/insurance/upload_file", file_path="test_data/json.json"
    )
    assert response.status == HTTPStatus.OK
