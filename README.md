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

4. Correlation analysis

Generated a full correlation heatmap for numeric features

6. Categorical feature analysis

Bar charts for school, sex, address, internet access, romantic relationship, etc.
GP school students make up 77% of the dataset
Urban students (address = U) pass at a higher rate than rural
Internet access at home positively associated with passing

7. Outlier detection

Used IQR method on numeric columns
absences had the most outliers (students with 30–40 absences)
age had a few outliers (students aged 20–22)
Outliers were retained as they represent genuine real-world cases

8. Pairplot (multivariate)

Pairplot of G1, G2, G3, absences, studytime coloured by pass/fail
Clear linear separation between pass/fail along the G1/G2/G3 axes
No clear separation on studytime or absences alone — these are weaker signals
