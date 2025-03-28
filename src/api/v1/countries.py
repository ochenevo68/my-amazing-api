from fastapi import APIRouter

from schemas.countries import (
    CreateCountryResult,
    ListCountriesResult,
    GetCountryResult,
    UpdateCountryResult,
    DeleteCountryResult,
    CountryInfo,
    PartialCountryInfo,
)
from services.countries_service import CountriesService

router = APIRouter()


@router.post("/countries")
def create_country(country_info: CountryInfo) -> CreateCountryResult:
    service = CountriesService()
    success = service.create_country(country_info)
    status = "success" if success else "error"
    return CreateCountryResult(status=status)


@router.get("/countries")
def list_countries() -> ListCountriesResult:
    service = CountriesService()
    data = service.list_countries()
    status = "error" if data is None else "success"
    return ListCountriesResult(data=data, status=status)


@router.get("/countries/{code:str}")
def get_country(code: str) -> GetCountryResult:
    service = CountriesService()
    data = service.get_country(code)
    status = "error" if data is None else "success"
    return GetCountryResult(data=data, status=status)


@router.patch("/countries/{code:str}")
def update_country(code: str, country_info: PartialCountryInfo) -> UpdateCountryResult:
    service = CountriesService()
    success = service.update_country(code, country_info)
    status = "success" if success else "error"
    return UpdateCountryResult(status=status)


@router.delete("/countries/{code:str}")
def delete_country(code: str) -> DeleteCountryResult:
    service = CountriesService()
    success = service.delete_country(code)
    status = "success" if success else "error"
    return DeleteCountryResult(status=status)
