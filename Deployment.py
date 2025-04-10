import numpy as np
import pandas as pd
import pickle 

df=pd.read_csv(r"C:\Users\Digvijay Patil\Downloads\diabetes.csv")

df=df.rename(columns={'DiabetesPedigreeFunction':'DPF'})

df_copy=df.copy(deep=True)
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']]=df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

# Replacing NaN value by mean, median depending upon distribution
# df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace=True)
# df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace=True)
# df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median(), inplace=True)
# df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace=True)
# df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace=True)

df_copy.fillna({
    'Glucose': df_copy['Glucose'].mean(),
    'BloodPressure': df_copy['BloodPressure'].mean(),
    'SkinThickness': df_copy['SkinThickness'].median(),
    'Insulin': df_copy['Insulin'].median(),
    'BMI': df_copy['BMI'].median()
}, inplace=True)

from sklearn.model_selection import train_test_split
X=df_copy.drop(columns='Outcome')
y=df_copy['Outcome']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=20,random_state=0)
classifier.fit(X_train,y_train)

filename='diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier,open(filename,'wb'))
