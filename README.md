🌍 From Oil to Ore: Machine Learning Analysis of Global Mineral Dependency
📌 Overview

The global shift toward renewable energy is often seen as a move away from fossil fuel dependency.
But an important question remains:

Are we replacing oil dependency with an even more concentrated dependency on critical minerals?

This project explores that question using statistical analysis and machine learning techniques applied to global mining data.

🎯 Objectives

Analyze global mineral production patterns (2000–2020)

Identify concentration and dominance in mineral supply

Predict future production trends using machine learning

Detect structural imbalances using clustering techniques

Evaluate risks in the energy transition supply chain

📊 Dataset

Source: Global Coal and Metal Mine Production Dataset (Zenodo)

Scope: Country-level mineral production data

Time Period: 2000–2020

⚙️ Methodology
1. Data Preprocessing

Merged multiple datasets

Cleaned inconsistencies

Removed duplicates

Created structured dataset:
country | year | material | production

2. Noise Injection & Cleaning

Simulated real-world data uncertainty

Added controlled noise (0.8% / 0.3%)

Cleaned using smoothing and clipping techniques

3. Statistical Analysis

Distribution analysis (skewness, concentration)

Country-level aggregation

Trend visualization

4. Supervised Learning

Target: next-year production

Features:

Lag variables (previous years)

Growth rate

Country & material encoding

Models:

Linear Regression

Random Forest

Metrics:

RMSE

R² Score

5. Unsupervised Learning

Aggregated production by country

Applied:

Standardization

K-Means clustering

PCA (for visualization)

Identified structural groups of countries

🔍 Key Findings

Mineral production is highly concentrated

A few countries dominate global supply

Production patterns are stable over time

Clustering reveals structural imbalance

Energy transition may shift dependency, not eliminate it

⚠️ Key Insight

The transition to renewable energy may reduce reliance on fossil fuels,
but it introduces a new dependency on geographically concentrated mineral resources.

📈 Results

High model accuracy (R² ≈ 0.98)

Strong predictive persistence in production

Clear clustering of dominant vs minor producers

PCA visualization highlights global imbalance

🧠 Tools & Technologies

Python (Pandas, NumPy)

Scikit-learn

Matplotlib

Google Colab

📁 Project Structure
├── data/
├── notebooks/
│   └── Final_Project.ipynb
├── outputs/
├── report/
│   └── Final_Report.docx
└── README.md
📚 References

Zenodo Dataset (DOI): https://doi.org/10.5281/zenodo.6325109

IEA Critical Minerals Reports

Scikit-learn Documentation

👥 Authors

Keyur Chaudhari

💡 Final Thought

Clean energy is not just an engineering challenge —
it is also a supply chain problem.
