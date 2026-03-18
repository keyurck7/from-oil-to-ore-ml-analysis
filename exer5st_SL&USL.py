import pandas as pd

# 1. Load the dataset  ---------------
csv_path = "C:\\Users\\keyur\\Downloads\\archive (1)\\global_leader_ideologies.csv"
df = pd.read_csv(csv_path)

print("Full dataset shape:", df.shape)
print("\nFirst 5 rows of the full dataset:")
print(df.head())

print("\nInfo of full dataset:")
print(df.info())

print("\nBasic statistics (numeric columns only):")
print(df.describe())


#Define feature and target columns for supervised learning -----
feature_cols = ["hog_right", "hog_left", "hog_center",
                "hog_noinfo", "hog_ideomiss"]
target_col = "democracy"

# Keep only rows where target is known
sup_df = df[feature_cols + [target_col]].dropna(subset=[target_col])

# Encode target: 'yes' -> 1, 'no' -> 0
sup_df[target_col] = sup_df[target_col].map({"yes": 1, "no": 0})

print("\n=== DATASET A: Supervised (Classification) ===")
print("Shape (rows, columns):", sup_df.shape)

print("\nFirst 5 rows (features + label):")
print(sup_df.head())

print("\nInfo of supervised dataset:")
print(sup_df.info())

print("\nBasic statistics of supervised features:")
print(sup_df[feature_cols].describe())
