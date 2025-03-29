from external.restcountries import get_data

import polars as pl

from repositories.countries_repository import CountriesRepository


class ImportService:
    def __init__(self, repository: CountriesRepository):
        self._repository = repository

    async def import_data(self) -> int:
        data = await get_data()

        wanted_columns = [
            pl.col("cca3").alias("code"),
            pl.col("name").struct["common"].alias("name"),
            pl.col("capital").list.first(),
            "population",
        ]

        country_infos = pl.DataFrame(data).select(wanted_columns)

        imported_count = self._repository.bulk_import(country_infos.to_dicts())

        return imported_count
