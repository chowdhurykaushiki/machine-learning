# -*- coding: utf-8 -*-
import pandas as pd
import os

def load_housing_data(housing_path='C:/KAUSHIKI/Personal/ML/ML_Exercise/HousingPrice'):
    file_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(file_path)

data=load_housing_data()
# see first five rows of dataframe
dataHead=data.head()
# dataframe info : gives infor about the dataframe obj
data.info()
# gives info about the details of the columns
dataDesc=data.describe()
#count of each categorical values
data["ocean_proximity"].value_counts()
#get the unique categorial value
data["ocean_proximity"].unique()
#get the column values using index when you dont know the column name
dataColVal=data.iloc[:,0:3]
#get the column values using column name
datacolVals=data.loc[0:10,"longitude"]
#groupby
#get the avg median housing pricegroup by ocean proximity
dataGroupBy=data.groupby("ocean_proximity").mean()["median_house_value"]
#get mzximum value of a column
data.max()["median_house_value"]
#get count of a colum
data.count()["total_bedrooms"]
data.mean()


#draw a plot
import matplotlib.pyplot as plt
data.head().plot(kind='bar',x="longitude",y="median_house_value")
plt.show()

data.plot(kind='scatter',x='longitude',y='latitude')
plt.show()

#########################################
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np
cnt = 0
smallData=data.head(10)
smallData=smallData.drop("income_cat",axis=1)
#smallData["income_cat"]=np.ceil(smallData["median_income"]/1.5)
smallData['income_cat']=pd.Series([2,2,3,2,3,2,2,3,3,3])
split=StratifiedShuffleSplit(n_splits=10,test_size=0.2,random_state=42)
for train_index,test_index in split.split(smallData,smallData["income_cat"]):
    cnt+=1
    print(train_index)
    print(test_index)
    strat_train_set=smallData.iloc[train_index]
    strat_test_set=smallData.iloc[test_index]
print(cnt)


