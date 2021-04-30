
# Feature Selection with Univariate Statistical Tests
from pandas import read_csv
from numpy import set_printoptions
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r'C:\Users\TAYFUN BUĞRA BAŞ\Desktop\odevler vs\Müh Proje')
dataset = pd.read_csv('hepsisonuclu.csv')
X = dataset.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]].values
y = dataset.iloc[:, 0].values
import mlxtend
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs

from sklearn.linear_model import LogisticRegression
# Sequential Forward Selection(sfs)
sfs = SFS(LogisticRegression(),
           k_features=30,
           forward=True,
           floating=False,
           scoring = 'accuracy',
           cv = 0)
sfs1=sfs.fit(X, y)
fig1 = plot_sfs(sfs1.get_metric_dict(), kind='std_dev')
result_LR = pd.DataFrame.from_dict(sfs1.get_metric_dict(confidence_interval=0.90)).T
result_LR.sort_values('avg_score', ascending=0, inplace=True)
result_LR.head()

best_features_LR = result_LR.feature_idx.head(1).tolist()
