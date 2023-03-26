import requests

while True:
    # get user input for the city name
    city = input("Enter city name: ")

    # use OpenMeteo API to get city coordinates
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url).json()
    try:
        latitude = response['results'][0]['latitude']
        longitude = response['results'][0]['longitude']
    except KeyError:
        print(f"Could not find city: {city}. Please enter a valid city name.")
        continue

    # use OpenMeteo API to get weather data for the city coordinates
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url).json()


    # get current weather data from the response
    current_weather = response['current_weather']

    # print current weather data
    print(f"Weather for {city}:")
    print(f"Temperature: {current_weather['temperature']}°C")
    print(f"Windspeed: {current_weather['windspeed']} m/s")
    print(f"Wind direction: {current_weather['winddirection']}°")

    # ask if the user wants to enter another city
    answer = input("Do you want to enter another city? (y/n): ")
    if answer.lower() != 'y':
        break
