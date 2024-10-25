# -*- coding: utf-8 -*-
"""diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10AFYBOF6HFbTaid1l0rAWOahfkYcK2hS
"""

print("Rajarshee")



import pandas as pd

Diabetes=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Diabetes.csv')

Diabetes.head()

Diabetes.info()

Diabetes.describe()

Diabetes.columns

y=Diabetes['diabetes']



X=Diabetes[['pregnancies', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi',
       'dpf', 'age', ]]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X,y,random_state=2529)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression(max_iter=500)

model.fit(X_train,y_train)

y_predict=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_predict)

