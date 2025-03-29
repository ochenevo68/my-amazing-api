from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


class BaseModel(DeclarativeBase):
    pass


class DatCountry(BaseModel):
    __tablename__ = "dat_country"

    code = mapped_column(String(3), primary_key=True)
    name = mapped_column(String())
    capital = mapped_column(String())
    population = mapped_column(BigInteger)
