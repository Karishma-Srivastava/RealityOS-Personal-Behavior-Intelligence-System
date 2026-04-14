from fastapi import APIRouter, UploadFile
import pandas as pd

router = APIRouter()

@router.post("/")
async def upload(file: UploadFile):
    df = pd.read_csv(file.file)

    return {
        "rows": len(df),
        "columns": list(df.columns)
    }