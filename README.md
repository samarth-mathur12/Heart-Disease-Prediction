# About DataSet:
This dataset contains the medical records of 5000 patients who had heart failure, collected during their follow-up period, where each patient profile has 13 clinical features.

## Attribute Information:
  1) age: age of the patient (years)
  2) anaemia: decrease of red blood cells or hemoglobin (boolean)
  3) creatinine phosphokinase (CPK): level of the CPK enzyme in the blood (mcg/L)
  4) diabetes: if the patient has diabetes (boolean)
  5) ejection fraction: percentage of blood leaving the heart at each contraction (percentage)
  6) high blood pressure: if the patient has hypertension (boolean)
  7) platelets: platelets in the blood (kiloplatelets/mL)
  8) sex: woman or man (binary)
  9) serum creatinine: level of serum creatinine in the blood (mg/dL)
  10) serum sodium: level of serum sodium in the blood (mEq/L)
  11) smoking: if the patient smokes or not (boolean)
  12) time: follow-up period (days)
  13) DEATH_EVENT: if the patient died during the follow-up period (boolean)

## Model
  The model used for this project is a RandomForestClassifier from the Scikit-Learn library. The model was selected because it achieved the highest cross-validation score during the model selection process.

## Libraries Used
  pandas for data manipulation and analysis
  matplotlib.pyplot and Seaborn for data visualization
  sklearn (Scikit-Learn) for machine learning algorithms and tools
## Preprocessing
  MinMaxScaler from sklearn.preprocessing was used to normalize the data values between 0 and 1.

## Model Selection
We used GridSearchCV to perform hyperparameter tuning for the RandomForestClassifier. The parameters tuned and their respective ranges were:
  n_estimators: [50, 100, 150]
  max_depth: [3, 5, 7]
  min_samples_split: [2, 3, 4]
  
## Contact 
Created by Samarth Mathur - samarthmathur199@gmail.com
