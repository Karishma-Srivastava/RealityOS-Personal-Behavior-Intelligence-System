import numpy as np

def detect_anomaly(series):
    mean = np.mean(series)
    std = np.std(series)

    return series < (mean - 2 * std)