import pandas as pd

# load your dataset (student productivity one)
df = pd.read_csv(r"C:\realityos_you day analyzer\data\dataset\student_productivity_distraction_dataset_20000.csv", encoding="latin1")

# clean
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
df = df.dropna()

# save final dataset for your project
df.to_csv("data/dataset.csv", index=False)

print("dataset.csv created successfully!")