import pandas as pd  
import numpy as np    
import matplotlib.pyplot as plt

def get_data(ds, date):

    data = pd.read_csv(r"dataset/"+ds+".csv")  
    return {"open": pred(data,4,date), "high": pred(data,5,date), "low": pred(data,6,date), "close": pred(data,8,date)}

def pred(data, val, date):
    x = data.iloc[:,:1].values    
    y = data.iloc[:, val].values
    from sklearn.model_selection import train_test_split    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
    from sklearn.linear_model import LinearRegression    
    regressor = LinearRegression()    
    regressor.fit(x_train, y_train)
    line = regressor.coef_*x+regressor.intercept_  
    from counter import days
    return regressor.predict([[float(days(date))]])

# a = get_data('RELIANCE', '2027-10-12')
