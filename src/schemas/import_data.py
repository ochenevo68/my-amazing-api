from typing import Any

from pydantic import BaseModel, Field


class ImportResult(BaseModel):
    status: str = Field("success")
    data: dict[str, Any] = Field(...)
