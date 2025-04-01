## Requirements

You will need:

- `python` 3.11 or newer
- `poetry` (tested with 2.1.1)
- `docker` (tested with 28.0.1)
- `docker-compose` (tested with 2.33.1)
- `make` (tested with GNU Make 4.4.1)

## How to

### 1. Setup

```
make setup
```

### 2. Launch the API

```
make start
```

### 3. Use the API

- Access the Swagger UI: http://127.0.0.1:8000/docs
- Import data from `restcountries.com` API
- Play around with the countries CRUD


### 4. Stop the API

```
make stop
```

### 5. Run tests

```
make test
```

### 6. Generate the documentation

```
make doc
```
The documentation will be generated in the `site` directory.
