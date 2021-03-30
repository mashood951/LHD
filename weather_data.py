import pyowm

api_key = 'df2c8cb21024af815ad7d4b7dece7de0'
owm = pyowm.OWM(api_key)

city = input("Enter city name: ")

try:
    weather_mgr = owm.weather_manager()
    loc = weather_mgr.weather_at_place(city)
    weather = loc.weather

    temp = weather.temperature(unit='celsius')
    temp_list = temp.items()

    avg_temp = list(temp.values())[0]
    temp_max = list(temp.values())[1]
    temp_min = list(temp.values())[2]
    feels_like = list(temp.values())[3]

    weather_status = weather.detailed_status
    humidity = weather.humidity

    if (humidity < 30 or humidity > 60):
        print("Sorry to say but you have to wait at home")

    else:
        if (avg_temp < 4):
            print("It's cold outside. Better to stay at home")

        if (avg_temp > 4 and weather_status == 'sunny day'):
            print("Cold outside but you can go as it's sunny day")
        
        if (avg_temp < 40 and avg_temp > 30):
            print("Hot outside better to stay in shades")
        
        if (avg_temp > 10 and avg_temp < 30):
            print("Go out for picnic!")

        else:
            print("It's hot outside better to stay at home")

except:
    print("City does not exist in Earth! Maybe you live in another planet :D")
