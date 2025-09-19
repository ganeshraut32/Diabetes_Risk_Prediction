import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("Diabetes_cleaned.csv")

X=df[["Glucose","BloodPressure","SkinThickness","Insulin","BMI","Pregnancies","Age","DiabetesPedigreeFunction"]]
y=df["Outcome"]
regressor_model = DecisionTreeClassifier()
regressor_model.fit(X,y)

pickle.dump(regressor_model, open('regressor_model.pkl', 'wb'))