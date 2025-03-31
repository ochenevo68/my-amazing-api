from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class CountryInfo(BaseModel):
    """Schema representing the information about a country.

    Attributes:
        code: Field for country code.
        name: Field for country name.
        capital: Field for country capital.
        population: Field for country population.
    """

    code: Annotated[str, StringConstraints(min_length=3, max_length=3)]
    name: str
    capital: str
    population: int


class PartialCountryInfo(BaseModel):
    """Schema representing partial info about a country.

    Note: Useful when operating on part of the country info only (example: partial update).

    Attributes:
        name: Field for country name.
        capital: Field for country capital.
        population: Field for country population.
    """

    name: Optional[str] = None
    capital: Optional[str] = None
    population: Optional[int] = None


class CreateCountryResult(BaseModel):
    """Schema representing the result of a "create" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
    """

    status: str = "success"


class ListCountriesResult(BaseModel):
    """Schema representing the result of a "list" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
        data: The list of country codes.
    """

    status: str = "success"
    data: list[str] = []


class GetCountryResult(BaseModel):
    """Schema representing the result of a "get" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
        data: The info of the country.
    """

    status: str = "success"
    data: CountryInfo


class UpdateCountryResult(BaseModel):
    """Schema representing the result of an "update" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
    """

    status: str = "success"


class DeleteCountryResult(BaseModel):
    """Schema representing the result of a "delete" operation.

    Attributes:
        status: Post-operation status ("success" if it worked).
    """

    status: str = "success"
