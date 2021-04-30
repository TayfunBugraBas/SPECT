import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r'C:\Users\TAYFUN BUĞRA BAŞ\Desktop\odevler vs\Müh Proje')
dataset = pd.read_excel('PythonFeatureları.xlsx')
X = dataset.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]].values
y = dataset.iloc[:, 0].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)



from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

