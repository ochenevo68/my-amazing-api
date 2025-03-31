## The API

| API endpoint URL                          | Method | Effect                                                       |
|:------------------------------------------|:------:|:-------------------------------------------------------------|
| http://127.0.0.1:8000/v1/import-data      |  POST  | Import data from restcountries.com API                       |
| http://127.0.0.1:8000/v1/countries        |  GET   | List country codes of countries currently stored             |
| http://127.0.0.1:8000/v1/countries        |  POST  | Create country with given parameter information              |
| http://127.0.0.1:8000/v1/countries/{code} |  GET   | Get info about currently stored country with given code      |
| http://127.0.0.1:8000/v1/countries/{code} | PATCH  | Update some info of currently stored country with given code |
| http://127.0.0.1:8000/v1/countries/{code} | DELETE | Delete currently stored country with given code              |
