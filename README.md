# Student-Performance-Prediction-and-Early-Intervention
This section of the project focuses on Exploratory Data Analysis (EDA) to understand the dataset before building predictive models. The goal is to identify patterns, detect anomalies, test hypotheses, and check assumptions using summary statistics and visualizations.

Student Performance Prediction — UCI Dataset
This folder contains the exploratory data analysis performed on the UCI Student Performance dataset (Math course, n = 395) prior to model training.

Objective
Understand the structure, distributions, relationships, and anomalies in the dataset before building predictive models. EDA informed feature selection, preprocessing decisions, and model design.

EDA steps performed
1. Dataset inspection

Loaded dataset and checked shape, dtypes, and sample rows using df.info() and df.describe()
Confirmed no missing values across all 26 features
Identified 13 binary/categorical columns and 13 numeric columns

2. Target variable analysis

Visualized pass/fail class distribution using a countplot
Found a mild class imbalance: ~60.5% pass vs ~39.5% fail
This informed the decision to use AUC-ROC alongside accuracy as the evaluation metric

3. Grade distribution (G1, G2, G3)

Plotted histograms for G1, G2, and final grade G3
All three grades follow a roughly normal distribution centered around 10–12
G1 and G2 show strong positive correlation with G3 (r ≈ 0.85)
Students with G3 < 10 are labeled as fail (target = 0)
