from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"name": "subbu", "Course": "Python"}


# uvicorn my_api:app --reload