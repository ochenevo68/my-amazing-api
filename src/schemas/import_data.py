from typing import Any

from pydantic import BaseModel


class ImportResult(BaseModel):
    status: str = "success"
    data: dict[str, Any]
