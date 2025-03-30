from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            + ", ".join(
                [f"{k}={v}" for k, v in self.__dict__.items() if not k.startswith("_")]
            )
            + ")"
        )
