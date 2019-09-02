# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:43:56 2019

@author: Hp
"""
from sklearn.decomposition import TruncatedSVD
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
svd = TruncatedSVD(2)
principalComponents = svd.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['Principal component 1', 'Principal component 2'])
finalDataFrame = pd.concat([principalDf, df[['target']]], axis = 1)
print(finalDataFrame.head())

