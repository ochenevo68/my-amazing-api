from fastapi import APIRouter, Depends, HTTPException, status

from dependencies import get_countries_repository
from repositories.countries_repository import CountriesRepository
from schemas.countries import (
    CountryInfo,
    CreateCountryResult,
    DeleteCountryResult,
    GetCountryResult,
    ListCountriesResult,
    PartialCountryInfo,
    UpdateCountryResult,
)
from services.countries_service import CountriesService, OperationStatus

router = APIRouter()


@router.post("/countries")
def create_country(
    country_info: CountryInfo,
    repository: CountriesRepository = Depends(get_countries_repository),
) -> CreateCountryResult:
    service = CountriesService(repository=repository)

    operation_status, detail = service.create_country(country_info)

    if operation_status == OperationStatus.CREATE_FAILURE_ALREADY_EXISTS:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)
    elif operation_status == OperationStatus.CREATE_FAILURE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
    return CreateCountryResult()


@router.get("/countries")
def list_countries(
    repository: CountriesRepository = Depends(get_countries_repository),
) -> ListCountriesResult:
    service = CountriesService(repository=repository)
    _, detail = service.list_countries()
    return ListCountriesResult(data=detail)


@router.get("/countries/{code:str}")
def get_country(
    code: str,
    repository: CountriesRepository = Depends(get_countries_repository),
) -> GetCountryResult:
    service = CountriesService(repository=repository)

    operation_status, detail = service.get_country(code)

    if operation_status == OperationStatus.GET_FAILURE_NOT_FOUND:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    elif operation_status == OperationStatus.GET_FAILURE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
    return GetCountryResult(data=detail)


@router.patch("/countries/{code:str}")
def update_country(
    code: str,
    country_info: PartialCountryInfo,
    repository: CountriesRepository = Depends(get_countries_repository),
) -> UpdateCountryResult:
    service = CountriesService(repository=repository)

    operation_status, detail = service.update_country(code, country_info)

    if operation_status == OperationStatus.UPDATE_FAILURE_NOTHING_TO_UPDATE:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=detail)
    elif operation_status == OperationStatus.UPDATE_FAILURE_NOT_FOUND:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    elif operation_status == OperationStatus.UPDATE_FAILURE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    return UpdateCountryResult()


@router.delete("/countries/{code:str}")
def delete_country(
    code: str,
    repository: CountriesRepository = Depends(get_countries_repository),
) -> DeleteCountryResult:
    service = CountriesService(repository=repository)

    operation_status, detail = service.delete_country(code)

    if operation_status == OperationStatus.DELETE_FAILURE_NOT_FOUND:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    elif operation_status == OperationStatus.DELETE_FAILURE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    return DeleteCountryResult()
