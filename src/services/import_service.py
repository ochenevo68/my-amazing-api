import polars as pl

from external import DataSource
from repositories.countries_repository import CountriesRepository


class ImportService:
    """Service responsible for data import."""

    def __init__(self, repository: CountriesRepository, data_source: DataSource):
        """Initialize the instance with a CountriesRepository and a DataSource.

        Args:
            repository: The CountriesRepository to use for internal data storage.
            data_source: The DataSource to get the data from.
        """
        self._repository = repository
        self._data_source = data_source

    async def import_data(self) -> int:
        """Import data from the DataSource into the internal storage.

        Returns:
            The number of data records (rows) imported.
        """
        data = await self._data_source.get_data()

        wanted_columns = [
            pl.col("cca3").alias("code"),
            pl.col("name").struct["common"].alias("name"),
            pl.col("capital").list.first(),
            "population",
        ]

        country_infos = pl.DataFrame(data).select(wanted_columns)

        imported_count = self._repository.bulk_import(country_infos.to_dicts())

        return imported_count
