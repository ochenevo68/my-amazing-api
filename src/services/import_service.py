from external.restcountries import get_data

import polars as pl


class ImportService:
    @staticmethod
    async def import_data():
        data: list[dict] = await get_data()

        wanted_columns = [
            pl.col("cca3").alias("code"),
            pl.col("name").struct["common"].alias("name"),
            pl.col("capital").list.first(),
            "population",
        ]

        df = pl.DataFrame(data).select(wanted_columns)

        print(df)

        return len(data)
