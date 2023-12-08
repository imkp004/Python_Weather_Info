import requests
import math 

API_KEY = "38f8fb3682974e0e26a72c704f290384"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter a city name (type 'stop' to exit): ")
    
    if city.lower() == 'stop':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if the user types 'stop'

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    try:
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Convert temperature from Kelvin to Fahrenheit
        temperature_kelvin = data["main"]["temp"]
        temperature_fahrenheit = round((temperature_kelvin - 273) * 9/5 + 32)

        weather = data['weather'][0]['description']

        print("Weather:", weather)
        print("Temperature:", temperature_fahrenheit, "Fahrenheit")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
