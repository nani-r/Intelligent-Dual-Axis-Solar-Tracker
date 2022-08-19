import pandas as pd
import numpy as np

import time
from datetime import datetime
import json
import requests

import serial
import syslog

import weather
import trainer
from sklearn.ensemble import GradientBoostingRegressor

import angle_calculator

#Get current weather forecast and format it using the same columns used for past data
def current_weather_forecast():
    r = requests.get(weather.forecast_weather_url()) 
    json_response = r.text
    parsed = json.loads(json_response)
    currently = parsed['currently']
    daily = parsed['daily']['data'][0]
    return weather.current_forecast(parsed, currently, daily)

#Predict the solar output using the trained model
def predict_output(column_name):
    gbr = GradientBoostingRegressor(n_estimators=600,   
    max_depth=5, 
    learning_rate=0.01, 
    min_samples_split=3)
    regressor = trainer.train_model(gbr, column_name)
    forecast = current_weather_forecast()  
    forecast_df = pd.DataFrame([forecast], 
                    columns = weather.common_headers + weather.hourly_headers + weather.daily_headers)    
    return regressor.predict(forecast_df[trainer.default_predictors])

# Send a signal to arduino
def write_to_arduino():
    port = '/dev/cu.usbmodem14101'
    ard = serial.Serial(port,9600,timeout=5)
    # Serial write section
    ard.flush()
    time.sleep(10)
    time_tp = datetime.today().timetuple()
    angles = angle_calculator.calc(time_tp.tm_yday, time_tp.tm_hour, time_tp.tm_min)
    anglestr = "a:" + str(angles['azimuth']) + "z:" + str(angles['zenith'])
    ard.write(anglestr.encode())
    print ("Python value sent: ")
    print(anglestr)
    time.sleep(10)
    ard.close() 

with_robot_prediction = int(predict_output('with_robot_output'))
without_robot_prediction = int(predict_output('without_robot_output'))
print("with_robot_prediction: " + str(with_robot_prediction))
print("without_robot_prediction: " + str(without_robot_prediction))
# If the model predicts that solar output with robot is greater than consumption
# send a signal to arduino
if ((with_robot_prediction - without_robot_prediction) > 10):
    print("y")
    # write_to_arduino()
else:
    print('n')
