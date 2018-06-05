# -*- coding: utf-8 -*-
import nltk
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from matplotlib import pyplot as plt

#read the csv file
housing=pd.read_csv("housing.csv")
#print("housing data count: ",housing.count())


#divide into test train set
trains_set,test_set=train_test_split(housing,test_size=.2,random_state=42)

#startified train test set on meian income
housing["income_cat"]=np.ceil(housing["median_income"]/1.5)
print(housing['income_cat'].unique())
housing['income_cat'].where(housing['income_cat']<5,5,inplace=True)
print(housing['income_cat'].unique())
split=StratifiedShuffleSplit(n_splits=1,test_size=.2,random_state=42)
for train_index,test_index in split.split(housing,housing['income_cat']):
    print(train_index)
    print(test_index)
    strat_train_set=housing.iloc[train_index]
    strat_test_set=housing.iloc[test_index]

#remove the income cat column from train set and test set
    #strat_test_set.drop('income_cat',axis=1,inplace=True)
for sets in (strat_train_set,strat_test_set):
    sets.drop('income_cat',axis=1,inplace=True)
#correaltion
housing['rooms_per_household']=housing['total_rooms']/housing['households']
housing['population_per_household']=housing['population']/housing['households']
housing['bedrooms_per_room']=housing['total_bedrooms']/housing['total_rooms']
corr=housing.corr()
corr['median_house_value'].sort_values(ascending=False)

housing.plot(x="latitude", y="longitude", kind="scatter")
housing.plot(x="latitude", y="longitude", kind="scatter",alpha=0.1)

#housing.plot(x="latitude", y="longitude", kind="hist")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""'
sampleTestSet=strat_test_set.copy()

import pandas as pd

sampleTestSet.plot(kind='scatter',x="longitude", y="latitude",alpha=0.1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from pandas.tools.plotting import scatter_matrix
housing_array=['median_income','median_house_value','housing_median_age']
scatter_matrix(sampleTestSet[housing_array],figsize=(12,8))





