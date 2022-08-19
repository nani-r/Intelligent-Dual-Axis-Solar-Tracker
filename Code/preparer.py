import csv
from datetime import datetime as datetime_datetime, timedelta, date
import datetime
import weather

#Create csv file for past weather data with the headers
def create_csv():
    csvfile = open("weather_data.csv",'w')
    output = csv.writer(csvfile)
    solar_output_headers = ['with_robot_output', 'without_robot_output']
    # solar_output_headers = ['with_robot_output', 'without_robot_output']
    output.writerow(weather.common_headers + weather.hourly_headers 
                    + weather.daily_headers + solar_output_headers)
    return output

def add_one_row(daily_data, row):
    millis = row['time']
    date_time = datetime_datetime.fromtimestamp(millis)
    time_formatted = date_time.strftime("%m/%d/%Y, %H:%M:%S")
    common_row_data = [row['time'], time_formatted, weather.millis_hour(millis), weather.millis_month(millis)]
    hourly_row_data = [len(row.get('icon','')), row.get('precipProbability',''), 
                       row['temperature'], row.get('cloudCover',''), row.get('visibility','')]
    daily_row_data = [daily_data['icon'], daily_data['precipProbability'], daily_data['cloudCover'],
    weather.millis_hour(daily_data['sunriseTime']), weather.millis_hour(daily_data['sunsetTime']), daily_data['visibility'], 
    daily_data['temperatureMin'], weather.millis_hour(daily_data['temperatureMinTime']),
                                  weather.millis_hour(daily_data['temperatureMax']), 
                                  weather.millis_hour(daily_data['temperatureMaxTime'])]
    solar_output_row = solar_output.get(str(millis),{})
    solar_output_row_data = [solar_output_row.get('with_robot_output',0), 
                             solar_output_row.get('without_robot_output',0)]

    row_data = common_row_data + hourly_row_data + daily_row_data + solar_output_row_data
    weather_output.writerow(row_data)    
    
#Add a row with weather and solar output data for each date
def create_csv_rows(all_dates):
    for single_date in all_dates:
        parsed = weather.forecast_response(single_date)
        hourly_data = parsed['hourly']['data']
        daily_data = parsed['daily']['data'][0]
        # Format each row of json response to fit the columns in the csv
        for row in hourly_data:
            add_one_row(daily_data, row)

#Create csv with past solar output
def prepare_past_solar_output():
    solar_dict = {}
    input_file = csv.DictReader(open("solar_output_2020.csv"))
    for row in input_file:
        solar_dict[row['time']] =  {'with_robot_output': row['with_robot_output'], 
                                    'without_robot_output': row['without_robot_output']}      
    return solar_dict

def all_dates():
    all_dates =  [datetime.datetime(2018, 10, 20), datetime.datetime(2018, 10, 21), datetime.datetime(2018, 10, 27)]
    all_dates += [datetime.datetime(2018, 10, 28), datetime.datetime(2018, 10, 29), datetime.datetime(2018, 11, 3)] 
    all_dates += [datetime.datetime(2018, 11, 4), datetime.datetime(2018, 11, 10), datetime.datetime(2018, 11, 11)]
    all_dates += [datetime.datetime(2018, 11, 12), datetime.datetime(2018, 11, 19), datetime.datetime(2018, 11, 20)]
    all_dates += [datetime.datetime(2018, 11, 22), datetime.datetime(2018, 11, 23), datetime.datetime(2018, 11, 24)]
    all_dates +=  [datetime.datetime(2019, 11, 9), datetime.datetime(2019, 11, 10), datetime.datetime(2019, 11, 16)]
    all_dates += [datetime.datetime(2019, 11, 17), datetime.datetime(2019, 11, 18), datetime.datetime(2019, 11, 23)] 
    all_dates += [datetime.datetime(2019, 11, 24), datetime.datetime(2019, 11, 25), datetime.datetime(2019, 11, 30)]
    all_dates += [datetime.datetime(2019, 12, 1)]
    return all_dates

weather_output = create_csv()   
solar_output =  prepare_past_solar_output()
create_csv_rows(all_dates())
