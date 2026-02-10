from fastapi import FastAPI

app = FastAPI(title="EcoLearn Learning Service")

@app.get("/health")
def health():
    return {"status": "learning service up"}
