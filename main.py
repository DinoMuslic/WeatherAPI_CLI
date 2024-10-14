import os
import sys
import urllib.request, json 

# Key can be generated here: https://www.meteosource.com
API_KEY = "YOUR_API_KEY"


city = sys.argv[1].capitalize()

# -c -> current weather data
# -h -> hourly weather data
# -d -> daily weather data 
flag = sys.argv[2] if len(sys.argv) > 2 else ""

with urllib.request.urlopen(f"https://www.meteosource.com/api/v1/free/point?place_id={city}&sections=all&timezone=auto&language=en&units=metric&key={API_KEY}") as url:
    data = json.load(url)

latitude = data["lat"]
longitude = data["lon"]
timezone = data["timezone"]

temperature = str(data["current"]["temperature"]) + "°C"
weather_description = data["current"]["summary"]

precipitation = str(data["current"]["precipitation"]["total"]) + "%"
wind_speed = str(data["current"]["wind"]["speed"]) + "km/h"
cloud_cover = str(data["current"]["cloud_cover"]) + "%"

city_fixed_width = 12  # Total width for city and weather icon combined
coordinate_fixed_width = 12  # Fixed width for latitude and longitude
timezone_fixed_width = 18  # Fixed width for timezone

os.system("clear")

weather_display = f"""
╭──────────────────────────────────────────╮
│                       │                  │
│   📍{city:<{city_fixed_width}}      │    🌡️ {temperature:<7}     │
│   🌐 {latitude:<{coordinate_fixed_width}}     │    💧 {precipitation:<5}      │
│   🌐 {longitude:<{coordinate_fixed_width}}     │    💨 {wind_speed:<6}    │
│   ⌛{timezone:<{timezone_fixed_width}}│    🌤️  {cloud_cover:<8}   │
│                       │                  │
╰──────────────────────────────────────────╯
"""


if flag == "-c" or flag == "":
    print(weather_display)
    
