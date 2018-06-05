# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:04:32 2018

@author: 212634012
"""
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import Imputer,StandardScaler, LabelBinarizer
import pandas as pd
import housing_custom_transformer
from sklearn.pipeline import Pipeline
from sklearn import pipeline


class dataFrameSelector(BaseEstimator,TransformerMixin):
    def __init__(self,attr_list):
        self.attr_list=attr_list
    def fit(self,X,y=None):
        pass
    def transform(self,X, y=None):
        return X[self.attr_list].values


housing_data=pd.read_csv('housing.csv')
#pre prcocess numeric data using pipeline
housing_data_num=housing_data.drop('ocean_proximity',axis=1)
num_attr=list(housing_data_num)
num_pipeline=Pipeline([('selector',dataFrameSelector(num_attr)),
                       ('custom_trans',housing_custom_transformer.CustomTransformer(True)),
                       ('imputer',Imputer(strategy='median')),
                       ('std_scalar',StandardScaler())])
# pre process categorical data
cat_attr=['ocean_proximity']
cat_pipeline=Pipeline([('selector',dataFrameSelector(cat_attr)),
                       ('categorical',LabelBinarizer())])

#combine both the array
full_pipeline=pipeline.FeatureUnion(transformer_list=[('num_pipeline',num_pipeline),
                                                      ('cat_pipeline',cat_pipeline)])
housing_data_prep=full_pipeline.fit_transform(housing_data)