from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_clustering(df, features):
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["cluster"] = kmeans.fit_predict(X)

    return df