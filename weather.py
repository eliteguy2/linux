import datetime
import requests
import json

def get_time():
    # Get the current time
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_weather(city):
    # Get the weather for a specific city
    api_key = "your_api_key"  # Replace with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Use metric units for temperature
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Check if the response contains the weather data
        if "weather" in data and "main" in data:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"{description.capitalize()} with a temperature of {temperature}°C"
        else:
            return "Weather data is unavailable for this city."
    except requests.exceptions.RequestException as e:
        # Handle network errors or invalid responses
        return f"Unable to fetch weather data. Error: {e}"
    except KeyError:
        # Handle unexpected JSON structure
        return "Unexpected response structure from the weather API."

def main():
    print("Hello! I can tell you the time or the weather.")
    while True:
        query = input("What would you like to know? (Type 'exit' to quit) ").lower()
        if "time" in query:
            time = get_time()
            print(f"The current time is {time}")
        elif "weather" in query:
            city = input("Enter a city: ").strip()
            if city:
                weather = get_weather(city)
                print(f"The weather in {city} is {weather}")
            else:
                print("Please enter a valid city name.")
        elif "exit" in query:
            print("Goodbye!")
            break
        else:
            print("I didn't understand that. Please ask about the 'time' or 'weather'.")

if __name__ == "__main__":
    main()
