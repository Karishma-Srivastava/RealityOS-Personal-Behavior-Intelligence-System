from fastapi import APIRouter
import pandas as pd

from backend.ml.clustering import run_clustering
from backend.ml.anomaly import detect_anomaly
from backend.services.recommendation import generate_recommendation
from backend.services.aggregation import aggregate_metrics
from backend.services.insights import generate_insights

router = APIRouter()

@router.get("/")
def summary():
    df = pd.read_csv("data/dataset.csv")

    features = ["study_hours_per_day", "sleep_hours", "focus_score", "productivity_score"]

    df = run_clustering(df, features)

    df["anomaly"] = detect_anomaly(df["productivity_score"])
    df["recommendation"] = df.apply(generate_recommendation, axis=1)

    metrics = aggregate_metrics(df)
    insights = generate_insights(metrics, df)

    return {
        "metrics": metrics,
        "insights": insights,
        "sample_data": df.head(5).to_dict(orient="records")
    }