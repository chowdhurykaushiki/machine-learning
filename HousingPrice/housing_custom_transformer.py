# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 22:31:32 2018

@author: 212634012
"""
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
class CustomTransformer(BaseEstimator,TransformerMixin):
    def __init__(self,add_bedrm_per_rm):
        self.add_bedrm_per_rm = True
    def fit(self,X,y=None):
        pass
    def transform(self,X,y=None):
        tot_rm_idx,tot_bedrm_idx,pop_idx,house_hld_idx=3,4,5,6
        rm_per_house_hold=X[:,tot_rm_idx]/X[:,house_hld_idx]
        pop_per_household=X[:,pop_idx]/X[:,house_hld_idx]
        if self.add_bedrm_per_rm:
            bedroom_per_room=X[:,tot_bedrm_idx]/X[:,tot_rm_idx]
            return np.c_[X,rm_per_house_hold,pop_per_household,bedroom_per_room]
        else:
            return np.c_[X,rm_per_house_hold,pop_per_household]


    
housing_dataFrame=pd.read_csv('housing.csv')
add_attr=CustomTransformer(True)
housing_extra_dataFrame=add_attr.transform(housing_dataFrame.values)


