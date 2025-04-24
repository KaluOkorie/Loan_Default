# Loan_Default
Banks deal with different types of risks, like credit risk, market risk, and Operational risk. This project is tasked with identifying the key factors influencing loan default

# Objectives 
1. What attributes should credit providers consider to best predict and
2. identify potential loan default?

# Dataset Overview
The dataset used for this study is titled South German Credit [Dataset 2020], sourced from the UCI Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/573/south+german+credit+update). It contains information on 1,000 loan applicants, each described by 21 features relevant to credit risk assessment. Notably, the dataset:
1. Has no missing values
2. Is provided in a .zip archive in .asc format
3. Contains German-language column names, which were translated to English for ease of analysis
  This dataset provides a solid foundation for building and evaluating machine learning models aimed at predicting loan default risk.

## Approach
**Exploratory Data Analysis (EDA):**
Performed a comprehensive analysis including missing data inspection, imputation, removal of irrelevant features, and visualisation of feature distributions to gain deeper insights into the dataset.

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

# Deployment:

## 🎯 Loan Default Prediction App

The selected model (Random Forest Classifier) was retrained with five features carved from its inbuilt feature importance and deployed using Streamlit Cloud.

<p align="center">
  <a href="https://loandefaultpredict.streamlit.app/" target="_blank">
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2I1cnZib2ZkMndpZnJ5aDRqa2UxeW9nNTdwY3g4Zm02Mjdobmx6YSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ohhwn9cHEZ4WwQxIY/giphy.gif" alt="Streamlit App Demo" width="600"/>
  </a>
</p>

👉 To check the deployment, click [HERE](https://loandefaultpredict.streamlit.app/)



# Loan Default Prediction Project

The selected model (Random Forest Classifier) was retrained with **five features** curated from its built-in feature importance analysis and deployed using Streamlit Cloud.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://loandefaultpredict.streamlit.app/)

**Check the live deployment:**  
[![Loan Default Prediction Demo](demo.gif)](https://loandefaultpredict.streamlit.app/)  
*(Click the GIF or [here](https://loandefaultpredict.streamlit.app/) to try the app!)*


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

**Key Loan Factors:**
Credit Amount, Employment History, and Credit History are the top factors influencing loan approval and default risk.
**Credit Amount** is crucial because larger loan amounts necessitate more stringent vetting processes to prevent defaults.
**Credit History** reflects an individual's past loan repayment behavior, making it an essential factor in predicting future default risks.
**Employment History** plays a significant role in determining an applicant's financial stability and ability to repay the loan.
These findings align with common lending practices, where higher loan amounts require more thorough assessments, and past behavior (in terms of credit and employment) is used to predict future behavior.

**🤝 Contributing**
Contributions to improve the model or extend the project are highly welcome!
Whether it’s bug fixes, feature enhancements, dataset expansion, or new model experiments — feel free to fork this repository, create a branch, make your changes, and submit a pull request

