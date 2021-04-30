import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold

paribas_data = pd.read_csv(r"C:\Users\TAYFUN BUĞRA BAŞ\Desktop\odevler vs\Müh Proje\hepsisonuclu.csv", nrows=20000)
paribas_data.shape

num_colums = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numerical_columns = list(paribas_data.select_dtypes(include=num_colums).columns)
paribas_data = paribas_data[numerical_columns]
paribas_data.shape

train_features, test_features, train_labels, test_labels = train_test_split(
    paribas_data.drop(labels=['0', '1'], axis=1),
    paribas_data['0'],
    test_size=0.33,
    random_state=41)

correlated_features = set()
correlation_matrix = paribas_data.corr()
for i in range(len(correlation_matrix .columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.8:
            colname = correlation_matrix.columns[i]
            correlated_features.add(colname)


train_features.drop(labels=correlated_features, axis=1, inplace=True)
test_features.drop(labels=correlated_features, axis=1, inplace=True)

train_features.shape, test_features.shape

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import roc_auc_score

from mlxtend.feature_selection import SequentialFeatureSelector

feature_selector = SequentialFeatureSelector(RandomForestClassifier(n_jobs=-1),
           k_features=15,
           forward=True,
           verbose=2,
           scoring='roc_auc',
           cv=4)

features = feature_selector.fit(np.array(train_features.fillna(0)), train_labels)

filtered_features= train_features.columns[list(features.k_feature_idx_)]
filtered_features

clf = RandomForestClassifier(n_estimators=100, random_state=41, max_depth=3)
clf.fit(train_features[filtered_features].fillna(0), train_labels)

train_pred = clf.predict_proba(train_features[filtered_features].fillna(0))
print('Accuracy on training set: {}'.format(roc_auc_score(train_labels, train_pred[:,1])))

test_pred = clf.predict_proba(test_features[filtered_features].fillna(0))
print('Accuracy on test set: {}'.format(roc_auc_score(test_labels, test_pred [:,1])))