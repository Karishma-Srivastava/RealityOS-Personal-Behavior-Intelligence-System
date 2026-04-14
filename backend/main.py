from fastapi import FastAPI
from backend.routes.upload import router as upload_router
from backend.routes.summary import router as summary_router

app = FastAPI()

app.include_router(upload_router, prefix="/upload")
app.include_router(summary_router, prefix="/summary")

@app.get("/")
def home():
    return {"message": "RealityOS API running"}