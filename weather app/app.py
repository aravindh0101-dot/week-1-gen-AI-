import requests

# Your OpenWeather API Key
api_key = "365d07a4af1d37aa1a2d8fc034586a43"

# Ask user for city name
city = input("Enter city name: ")

# OpenWeather API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request to API
response = requests.get(url)

# Convert response into JSON
data = response.json()

# Check API response
if data["cod"] == 200:

    # Extract weather details
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    # Print weather details
    print("\nWeather Details")
    print("------------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather}")

else:
    # Print error message
    print("\nError:", data["message"])