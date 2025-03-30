from fastapi import APIRouter, Depends

from dependencies import get_countries_repository, get_data_source
from external import DataSource
from repositories.countries_repository import CountriesRepository
from schemas.import_data import ImportResult
from services.import_service import ImportService

router = APIRouter()


@router.post("/import-data")
async def import_data(
    repository: CountriesRepository = Depends(get_countries_repository),
    data_source: DataSource = Depends(get_data_source),
) -> ImportResult:
    service = ImportService(repository=repository, data_source=data_source)
    count = await service.import_data()
    status = "success" if count > 0 else "error"
    return ImportResult(data={"count": count}, status=status)
