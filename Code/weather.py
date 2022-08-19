import requests
import json
import csv
from datetime import datetime as datetime_datetime, timedelta, date
import time
import datetime

common_headers = ['time','time_formatted', 'time_hour', 'time_month']
hourly_headers = ['hourly_icon', 'hourly_precip_probability', 'hourly_temperature', 
                  'hourly_cloud_cover', 'hourly_visibility']
daily_headers =  ['daily_icon', 'daily_precip_probability', 'daily_cloud_cover', 
                  'daily_sunrise_hour', 'daily_sunset_hour', 
                  'daily_visibility','daily_temp_low', 'daily_temp_low_hour', 
                  'daily_temp_high', 'daily_temp_high_hour' ]

def base_url():
    secret_key = '1b6fd0e44eae21e7b9598c8875382483'
    latitude = '33.0198'
    longitude = '-96.6989'
    base_url = 'https://api.darksky.net/forecast/'
    return base_url + secret_key + '/' + latitude + ',' + longitude 

def timemachine_weather_url(time): 
    exclude_list = 'flags, currently'
    return base_url() + ','  + str(time) + '?exclude=' + exclude_list

def forecast_weather_url():
    return base_url()

def millis_hour(millis):
    date_time = datetime_datetime.fromtimestamp(millis)
    return int(date_time.time().hour)

def millis_month(millis):
    date_time = datetime_datetime.fromtimestamp(millis)
    return int(date_time.date().month)    

def forecast_response(one_date):
     # Call the api to get weather data, parse the json response
    timems = int(time.mktime(one_date.timetuple()))
    r = requests.get(timemachine_weather_url(timems)) 
    json_response = r.text
    parsed = json.loads(json_response)
    return parsed

#Format current forecast
def current_forecast(parsed, currently, daily): 
    millis = currently['time']
    date_time = datetime_datetime.fromtimestamp(millis)
    time_formatted = date_time.strftime("%m/%d/%Y, %H:%M:%S") 
    common_row_data = [currently['time'], time_formatted, millis_hour(millis), millis_month(millis)]
    hourly_row_data = [len(currently.get('icon','')), currently.get('precipProbability',''),
                       currently['temperature'], currently.get('cloudCover',''), 
                       currently.get('visibility','')]
    daily_row_data = [daily['icon'], daily['precipProbability'], daily['cloudCover'],
                      millis_hour(daily['sunriseTime']), millis_hour(daily['sunsetTime']),  
                      daily['visibility'], daily['temperatureMin'], 
                      millis_hour(daily['temperatureMinTime']), daily['temperatureMax'], 
                      millis_hour(daily['temperatureMaxTime'])]
    row_data = common_row_data + hourly_row_data + daily_row_data
    return row_data

print(forecast_weather_url())
print(forecast_response(date.today()))
