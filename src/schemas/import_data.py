from typing import Any

from pydantic import BaseModel


class ImportResult(BaseModel):
    """Schema representing the result of an "import" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
        data: Data about what was imported. (Record count)
    """

    status: str = "success"
    data: dict[str, Any]
