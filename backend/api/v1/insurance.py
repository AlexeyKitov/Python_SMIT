import datetime
import json
import logging

from fastapi import APIRouter, UploadFile, File, Depends, Query

from api.v1.schema.insurance import (
    CostOfInsurancePydantic,
    TariffIn,
    PriceInsurance,
    UploadTariffOut,
)
from api.v1.utils.paginator import FastApiPaginator
from services.insurance_service import InsuranceService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/insurance", tags=["insurance"])


@router.get("/")
async def get_lists(
    paginator: FastApiPaginator = Depends(),
    insurance_service: InsuranceService = Depends(),
) -> list[CostOfInsurancePydantic]:
    """
    Вывод списка тарифов
    """

    return await insurance_service.get_tariff_list(paginator)


@router.post("/upload_file")
async def upload_file(
    file: UploadFile = File(), insurance_service: InsuranceService = Depends()
) -> UploadTariffOut:
    """
    Загрузка тарифов из файла
    """

    content = await file.read()
    tariff = TariffIn(__root__=json.loads(content))
    return await insurance_service.set_tariff(tariff=tariff)


@router.post("/set_tariff")
async def post_price(
    tariff: TariffIn, insurance_service: InsuranceService = Depends()
) -> UploadTariffOut:
    """
    Загрузка тарифа из json
    """

    return await insurance_service.set_tariff(tariff=tariff)


@router.get("/calculate_price")
async def get_price(
    cargo: str = Query(description="Тип груза"),
    date: datetime.date = Query(description="Дата актуальности"),
    declared_value: float = Query(description="Объявленная стоимость"),
    insurance_service: InsuranceService = Depends(),
) -> PriceInsurance:
    """
    Расчет стоимости страховки
    """

    return await insurance_service.calculate_price(cargo, date, declared_value)
