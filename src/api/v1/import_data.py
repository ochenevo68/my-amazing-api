from fastapi import APIRouter

from schemas.import_data import ImportResult
from services.import_service import ImportService

router = APIRouter()


@router.post("/import-data")
async def import_data() -> ImportResult:
    service = ImportService()
    count = await service.import_data()
    status = "success" if count > 0 else "error"
    return ImportResult(data={"count": count}, status=status)
