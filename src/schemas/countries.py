from pydantic import BaseModel, Field


class CountryInfo(BaseModel):
    code: str  # TODO length == 3
    name: str
    capital: str
    population: int


class PartialCountryInfo(BaseModel):  # TODO: make everything optional
    code: str  # TODO length == 3
    name: str
    capital: str
    population: int


class CreateCountryResult(BaseModel):
    status: str = Field("success")


class ListCountriesResult(BaseModel):
    status: str = Field("success")
    data: list[str] = Field(...)


class GetCountryResult(BaseModel):
    status: str = Field("success")
    data: CountryInfo


class UpdateCountryResult(BaseModel):
    status: str = Field("success")


class DeleteCountryResult(BaseModel):
    status: str = Field("success")
