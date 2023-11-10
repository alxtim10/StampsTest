import requests
from datetime import datetime

predictions = []

uri = "http://api.openweathermap.org/geo/1.0/direct?q=Jakarta&limit=1&appid=7a509615117fe7945e40b1cd0d6cf915"
response = requests.get(uri)
x = response.json()
lat = x[0]['lat']
lon = x[0]['lon']
uri2 = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=7a509615117fe7945e40b1cd0d6cf915'
response2 = requests.get(uri2)
y = response2.json()

for i in range(0, 40):
    date = y['list'][i]['dt_txt']
    date_format = '%Y-%m-%d %H:%M:%S'
    date_obj = datetime.strptime(date, date_format)
    finaldate = date_obj.strftime('%a, %d %b %Y')
    
    temps = y['list'][i]['main']['temp']
    celcius = float(temps) - 273.15
    finalcel = "%.2f" % celcius
    curr = finaldate + ": " + finalcel + " °C"
    
    substrdate = curr[:16]
    if any(substrdate in x for x in predictions):
        continue
    else:
        predictions.append(curr)
        
print("Weather Forecast: ")
for i in predictions:
    print(i)