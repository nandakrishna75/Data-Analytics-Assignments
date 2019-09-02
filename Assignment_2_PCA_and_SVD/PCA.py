# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:08:45 2019

@author: Hp
"""

import pandas as pd
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:,['target']].values
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['Principal component 1', 'Principal component 2'])
finalDataFrame = pd.concat([principalDf, df[['target']]], axis = 1)
print(finalDataFrame.head())



