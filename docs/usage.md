## Requirements

You will need:

- `python` 3.11 or newer
- `poetry` (tested with 2.1.1) 
- `docker` (tested with 28.0.1)
- `docker-compose` (tested with 2.33.1)
- `make` (tested with GNU Make 4.4.1)

## How to launch the API

```
make start
```

## How to use the API

- Access the Swagger UI: http://127.0.0.1:8000/docs
- Import data from restcountries.com API
- Play around with the countries CRUD 


## How to stop the API (and other containers too)

```
make stop
```


## How to run tests

```
make test
```


## How to generate the documentation

```
make doc
```