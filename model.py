# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle as pkl
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
exp=np.random.randint(1,10,10)
score=np.random.randint(1,10,10)
Sal=np.random.randint(5000,10000,10)
salary=pd.DataFrame({'Exp':exp,'Score':score,'Sal':Sal})

X=salary.iloc[:,0:2]
y=salary['Sal']
"Model Bulding"
model=LinearRegression()
regression=model.fit(X,y)

"Dumping Model Using the Pickle"
pkl.dump(regression,open('model.pkl','wb'))

"Reloading the model and testing with values"
modelpckl=pkl.load(open('model.pkl','rb'))
modelpckl.predict(['values of columns'])
