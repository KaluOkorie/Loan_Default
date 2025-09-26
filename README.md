# Identifying Key Factors Influencing Loan Default

This project tackles a critical question in banking: **Beyond credit scores, what really predicts loan defaults?** While working with the South German Credit dataset, I discovered that traditional risk indicators don't always tell the full story.

As someone passionate about making financial systems more equitable and efficient, I wanted to move beyond surface level analysis to understand the nuanced factors that truly influence repayment behavior.

## Dataset Overview
The dataset used for this study is titled South German Credit [Dataset 2020], sourced from the UCI Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/573/south+german+credit+update). It contains information on 1,000 loan applicants, each described by 21 features relevant to credit risk assessment. Notably, the dataset:
1. Has no missing values
2. Is provided in a .zip archive in .asc format
3. Contains German-language column names, which were translated to English for ease of analysis
  This dataset provides a solid foundation for building and evaluating machine learning models aimed at predicting loan default risk.

## 💡 The Insight That Changed My Perspective

The most surprising finding wasn't which model performed best, but **why** it performed best. Despite achieving 89% cross-validation accuracy, my models consistently dropped to around 71% on test data. This taught me a crucial lesson about the difference between theoretical accuracy and real-world reliability.

I also discovered that medium credit amounts have the highest default rates - challenging the assumption that larger loans are inherently riskier. This suggests that risk assessment needs to consider not just the amount, but the purpose and context of the loan.

### Technical Insights:
- **Random Forests** outperformed Decision Trees and K-NN because they handle feature interactions better in imbalanced datasets
- **Feature selection** (using RFECV) proved more valuable than hyperparameter tuning alone
- The gap between cross-validation and test performance highlighted the importance of **robust validation strategies**

## Approach
**Exploratory Data Analysis (EDA):**
Performed a comprehensive analysis including missing data inspection, imputation, removal of irrelevant features, and visualisation of feature distributions to gain deeper insights into the dataset.
- **Ethical data handling** with sensitive demographic information
- **Comprehensive EDA** with visualizations of outliers and distributions
- **Smart feature engineering** removing redundant variables like telephone numbers
- **Class imbalance handling** using Random OverSampling
  

**Data Cleaning / Pre-processing:**
Addressed class imbalance using RandomOverSampler, applied One-Hot Encoding to categorical features, and scaled numerical data for better model performance.

**Feature Engineering:**
Enhanced the dataset by creating synthetic feature combinations and selected optimal features using Recursive Feature Elimination with Cross-Validation (RFECV).

**Standardization:**
Normalised feature scales using StandardScaler to ensure consistency across models.

**Modelling:**
Built and compared three machine learning models:
Random Forest
K-Nearest Neighbors (KNN)
Decision Tree

**Hyperparameter Tuning:**
Employed GridSearchCV to fine-tune model parameters for improved accuracy and robustness.

**Final Model Selection:**
Based on accuracy scores and visual comparisons:
accuracies = [acc_dt, acc_rf, acc_knn]
the **Random Forest model** was selected for deployment.

## Deployment of the Loan_Default_Prediction App
The selected model (Random Forest Classifier) was retrained with five features carved from its inbuilt feature importance and deployed using Streamlit Cloud.
**Check the live deployment:**  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://loandefaultpredict.streamlit.app/)

[![Loan Default Prediction Demo](demo.gif)](https://loandefaultpredict.streamlit.app/)  
*(Click 👉 [here](https://loandefaultpredict.streamlit.app/) to try the app!)*


## Tech Stack
**Language:** Python

**Libraries & Tools:**

**pandas** – Data manipulation & preprocessing

**numpy** – Numerical computations

**scikit-learn** – Machine learning models & evaluation

**seaborn & matplotlib** – Data visualisation

**streamlit** – Model deployment via interactive web app

## Project Takeaways
Through this project, I demonstrated hands-on experience with:

Data exploration, analysis, and visualization
Data preprocessing and feature engineering
Model training and evaluation
Model deployment using Streamlit

## Study Outcomes and Conclusions

<img width="671" alt="Demographic_default_trend" src="https://github.com/user-attachments/assets/42b67172-ff44-44dc-a615-df9224398e59" />

**1. Demographic Insights:** The study found that, demographically, **females** in younger and middle age groups tend to have a lower loan default rate compared to males. This may be attributed to females generally being supported by their parents, partners, or making more cautious financial decisions. However, as females age, they often begin supporting their families more heavily, which may impact their financial stability and lead to a higher likelihood of default. In contrast, **males** tend to start striving for financial independence earlier, often with little support. If their investments or business ventures succeed, they are able to repay the loan. which often happens due to youthful exuberance or premature understanding of financial systems the risk of default increases. As males grow older, they tend to focus more on personal financial security for the family rather than family immediate support.

<img width="1090" alt="Features_to_consider_before_granting_Loan" src="https://github.com/user-attachments/assets/6a6946fe-5fe1-4018-8a49-9d8d58aac397" />

### Models Compared:
- K-Nearest Neighbors (K-NN)
- Decision Trees  
- Random Forests (best performer)
- Recursive Feature Elimination with Cross-Validation (RFECV)

### Advanced Techniques:
- Hyperparameter tuning with GridSearchCV
- Stratified sampling for better validation
- Feature importance analysis
