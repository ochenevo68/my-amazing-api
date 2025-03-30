from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class CountryInfo(BaseModel):
    code: Annotated[str, StringConstraints(min_length=3, max_length=3)]
    name: str
    capital: str
    population: int


class PartialCountryInfo(BaseModel):
    name: Optional[str] = None
    capital: Optional[str] = None
    population: Optional[int] = None


class CreateCountryResult(BaseModel):
    status: str = "success"


class ListCountriesResult(BaseModel):
    status: str = "success"
    data: list[str] = []


class GetCountryResult(BaseModel):
    status: str = "success"
    data: CountryInfo


class UpdateCountryResult(BaseModel):
    status: str = "success"


class DeleteCountryResult(BaseModel):
    status: str = "success"
