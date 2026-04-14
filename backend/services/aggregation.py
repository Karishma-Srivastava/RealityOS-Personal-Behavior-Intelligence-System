def aggregate_metrics(df):
    total_users = len(df)

    avg_study = df["study_hours_per_day"].mean()
    avg_sleep = df["sleep_hours"].mean()
    avg_productivity = df["productivity_score"].mean()

    cluster_counts = df["cluster"].value_counts().to_dict()

    return {
        "total_users": total_users,
        "avg_study_hours": round(avg_study, 2),
        "avg_sleep_hours": round(avg_sleep, 2),
        "avg_productivity": round(avg_productivity, 2),
        "cluster_distribution": cluster_counts
    }