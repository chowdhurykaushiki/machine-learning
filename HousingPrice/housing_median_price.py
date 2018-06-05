# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelBinarizer

#read file into dataframe
housing=pd.read_csv('housing.csv')

#replace the missing value for numeric attributes
housing_new=housing.drop('ocean_proximity',axis=1)
imputer=Imputer(strategy='median')
housing_new_imputed=imputer.fit_transform(housing_new)
housing_new=pd.DataFrame(housing_new_imputed,columns=housing_new.columns)

#encode the text attributes to numeric
encoder=LabelBinarizer()
housing_new_encoded=encoder.fit_transform(housing['ocean_proximity'])
housing_new_enc_df=pd.DataFrame(housing_new_encoded,columns=['prox1','prox2','prox3','prox4','prox5'])

#create startified train and test set
housing_new['income_cat']= np.ceil(housing_new['median_income']/1.5)
housing_new['income_cat'].unique()
housing_new['income_cat'].where(housing_new['income_cat']<5,5,inplace=True)
housing_new['income_cat'].unique()
split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(housing_new,housing_new['income_cat']):
    strat_train_set=housing.iloc[train_index]
    strat_test_set=housing.iloc[test_index]









