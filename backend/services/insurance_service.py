import datetime
import logging

from fastapi import HTTPException

from api.v1.models import CostOfInsurance
from api.v1.schema.insurance import (
    PriceInsurance,
    CostOfInsurancePydantic,
    TariffIn,
    UploadTariffOut,
)
from api.v1.utils.paginator import FastApiPaginator

logger = logging.getLogger(__name__)


class InsuranceService:
    @staticmethod
    async def calculate_price(cargo: str, date: datetime.date, declared_value: float) -> PriceInsurance:
        """
        Расчет стоимости страховки
        """

        cost_of_insurance = await CostOfInsurance.filter(actual_date=date, cargo=cargo).first()
        if not cost_of_insurance:
            raise HTTPException(status_code=404, detail="Тариф на данный груз отсутствует")
        price = declared_value * cost_of_insurance.rate
        return PriceInsurance(actual_date=cost_of_insurance.actual_date, price=price, cargo=cargo)

    @staticmethod
    async def set_tariff(tariff: TariffIn) -> UploadTariffOut:
        """
        Загрузка тарифов в базу
        """

        result = UploadTariffOut()
        for date, items in tariff.__root__.items():
            for item in items:
                result.count += 1
                obj = await CostOfInsurance.filter(actual_date=date, cargo=item.cargo).first()
                if not obj:
                    obj = CostOfInsurance(actual_date=date, cargo=item.cargo, rate=item.rate)
                    await obj.save()
                    result.created += 1
                elif obj.rate != item.rate:
                    obj.rate = item.rate
                    await obj.save()
                    result.updated += 1
        return result

    @staticmethod
    async def get_tariff_list(
        paginator: FastApiPaginator,
    ) -> list[CostOfInsurancePydantic]:
        """
        Вывод списка тарифов
        """

        costs = await CostOfInsurance.all().limit(paginator.page_size).offset(paginator.get_offset())
        return [await CostOfInsurancePydantic.from_tortoise_orm(_) for _ in costs]
