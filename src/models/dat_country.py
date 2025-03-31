from sqlalchemy import BigInteger, String
from sqlalchemy.orm import mapped_column

from models import BaseModel


class DatCountry(BaseModel):
    """Model representing the dat_country table.

    Attributes:
        code: Column for country code.
        name: Column for country name.
        capital: Column for country capital.
        population: Column for country population.
    """

    __tablename__ = "dat_country"

    code = mapped_column(String(3), primary_key=True)
    name = mapped_column(String())
    capital = mapped_column(String())
    population = mapped_column(BigInteger)
