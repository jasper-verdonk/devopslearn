import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=33.5228587&lon=-86.8077052")

soup = BeautifulSoup(page.content, 'html.parser')
seven_day_forcast = soup.find(id="seven-day-forecast")
forecast_items = seven_day_forcast.find_all(class_="tombstone-container")

period_tags = seven_day_forcast.select(".tombstone-container .period-name")
short_descs = [sd.get_text() for sd in seven_day_forcast.select(".tombstone-container .short-desc")] 
temps = [t.get_text() for t in seven_day_forcast.select(".tombstone-container .temp")] 
descs = [d['title'] for d in seven_day_forcast.select(".tombstone-container img")] 

weather = pd.DataFrame({"period": period_tags, "short_desc": short_descs, "temp": temps, "descs": descs})

print(weather)