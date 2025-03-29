from fastapi import APIRouter, Depends

from dependencies import get_countries_repository
from repositories.countries_repository import CountriesRepository
from schemas.import_data import ImportResult
from services.import_service import ImportService

router = APIRouter()


@router.post("/import-data")
async def import_data(
    repository: CountriesRepository = Depends(get_countries_repository),
) -> ImportResult:
    service = ImportService(repository=repository)
    count = await service.import_data()
    status = "success" if count > 0 else "error"
    return ImportResult(data={"count": count}, status=status)
