def generate_recommendation(row):
    if row["cluster"] == 2:
        return "Reduce screen time, improve sleep, and minimize distractions"

    elif row["cluster"] == 0:
        return "Increase study time to convert focus into productivity"

    else:
        return "Maintain routine and optimize for consistency"