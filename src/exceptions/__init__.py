class CountryAlreadyExistsException(Exception):
    """Exception occurring when trying to create a country that already exists.

    Attributes:
        message: The message associated with this exception.
    """

    message: str = "country already exists"
