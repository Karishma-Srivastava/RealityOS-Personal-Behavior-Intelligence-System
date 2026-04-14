def generate_insights(metrics, df):
    insights = []

    if metrics["avg_productivity"] < 55:
        insights.append("Productivity is moderate despite reasonable study hours, indicating inefficiency in time usage")

    if metrics["avg_sleep_hours"] < 7:
        insights.append("Sleep levels are slightly below optimal, potentially reducing cognitive performance")

    if metrics["avg_study_hours"] > 5 and metrics["avg_productivity"] < 55:
        insights.append("Users are investing time but not converting it into productivity effectively")

    # anomaly insight
    anomaly_count = df["anomaly"].sum()

    if anomaly_count > 0:
        insights.append(f"{anomaly_count} users show significantly low productivity patterns, indicating need for targeted intervention")

    return insights