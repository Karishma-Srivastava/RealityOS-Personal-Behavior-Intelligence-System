import pandas as pd

df1 = pd.read_csv("dataset/ScreenTime vs MentalWellness.csv", encoding="latin1")
df2 = pd.read_csv("dataset/student_productivity_distraction_dataset_20000.csv", encoding="latin1")

print(df1.head())
print(df2.head())