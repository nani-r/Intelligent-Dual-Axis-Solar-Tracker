import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import matplotlib.pyplot as plt

import weather

default_predictors = ['hourly_precip_probability', 'hourly_icon', 
'time', 'time_hour', 'hourly_cloud_cover','hourly_temperature']

def train_model(regressor, column_name, predictors = default_predictors):
    x = weather_data_df()[predictors] #setting the col names
    y = weather_data_df()[column_name] #setting the col names
    regressor.fit(x, y)
    return regressor

def test_model(regressor, column_name, predictors = default_predictors):
    x = weather_data_df()[predictors] #setting the col names
    y = weather_data_df()[column_name] #setting the col names

    xtrain, xtest, ytrain, ytest=train_test_split(x, y, random_state=12, 
             test_size=0.2)
    regressor.fit(xtrain, ytrain)
    ypred = regressor.predict(xtest)
    mse = mean_squared_error(ytest,ypred)
    print(regressor.__class__.__name__)
    print("MSE: %.2f" % mse)
    print(regressor.score(xtest, ytest))
    x_ax = range(len(ytest))
    plt.scatter(x_ax, ytest, s=5, color="blue", label="original")
    plt.plot(x_ax, ypred, lw=0.8, color="red", label="predicted")
    plt.legend()
    plt.show()
    

def weather_data_df():
    weather_data_df = pd.read_csv('weather_data.csv')
    weather_data_df.dropna(inplace=True)
    weather_data_df = weather_data_df[~weather_data_df['with_robot_output'].isin([0])]
    return weather_data_df
