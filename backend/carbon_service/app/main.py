from fastapi import FastAPI

app = FastAPI(title="EcoLearn Carbon Service")

@app.get("/health")
def health():
    return {"status": "carbon service up"}
