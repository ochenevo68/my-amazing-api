from fastapi import FastAPI
from api.v1 import countries, import_data


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I am alive and well!"}


version = "v1"
prefix = f"/{version}"

app.include_router(import_data.router, prefix=prefix, tags=["import"])
app.include_router(countries.router, prefix=prefix, tags=["countries"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
