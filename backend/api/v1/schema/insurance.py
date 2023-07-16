import datetime

from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from api.v1.models import CostOfInsurance

CostOfInsurancePydantic = pydantic_model_creator(CostOfInsurance, exclude=("id",))


class PriceInsurance(BaseModel):
    cargo: str = Field(..., description="Тип груза")
    price: float = Field(..., description="Стоимость")
    actual_date: datetime.date = Field(..., description="Дата актуальности")


class CalculateIn(BaseModel):
    cargo: str = Field(..., description="Тип груза")
    actual_date: datetime.date = Field(..., description="Дата актуальности")
    declared_value: float = Field(..., description="Объявленная стоимость")


class TariffIn(BaseModel):
    __root__: dict[datetime.date, list[CostOfInsurancePydantic]] = Field(
        example="""
{
   "2021-01-01":[
      {
         "cargo":"Glass",
         "rate":0.4
      },
      {
         "cargo":"Other",
         "rate":0.2
      }
   ],
   "2021-01-03":[
      {
         "cargo":"Glass",
         "rate":0.2
      },
      {
         "cargo":"Other",
         "rate":0.5
      }
   ]
}"""
    )


class UploadTariffOut(BaseModel):
    count: int = Field(0, description="Записей обработано")
    created: int = Field(0, description="Записей создано")
    updated: int = Field(0, description="Записей обновлено")
