import requests

def get_weather(city, api_key):
	base_url = "http://api.openweathermap.org/data/2.5/weather"
	params = {
	"q": city,
	"appid" : api_key,
	"units" : "metric"
	}
	
	try:
		response = requests.get(base_url, params = params)
		response.raise_for_status()
		data = response.json()
		
		if "cod" not in data or int(data["cod"]) != 200:
			print(f"Error: {data.get('message', 'City not found or invalid API key')}")
			return False				
			
		city_name = data.get("name", "Unknown")
		country = data.get("sys", {}).get("country", "Unknown")
		temperature = data.get("main", {}).get("temp", "N/A")
		humidity = data.get("main", {}).get("humidity", "N/A")
		weather_description = data.get("weather", [{}])[0].get("description", "N/A")
		temp_feels = data.get("main", {}).get("feels_like", "N/A")
		temp_min = data.get("main", {}).get("temp_min", "N/A")
		temp_max = data.get("main", {}).get("temp_max", "N/A")
		visibility = data.get("visibility", "N/A")
		wind_speed = data.get("wind", {}).get("speed", "N/A")
		
		print(f"\nWeather in {city_name}, {country}:")
		print(f"Temperature: {temperature}°C")
		print(f"Humidity: {humidity}%")
		print(f"Weather description: {weather_description}")
		print(f"Temperature feels like: {temp_feels}°C")
		print(f"Minimum temperature: {temp_min}°C")
		print(f"Maximum temperature: {temp_max}°C")
		print(f"Visibility: {visibility} metres")
		print(f"Wind speed: {wind_speed} m/s")
		return False
		
	except KeyError as e:
		print(f"Missing key in the response: {e}")
		return False
	except requests.exceptions.RequestException as e:
		print(f"Error: Unable to fetch data.{e}")
		retry = input("\nWould you like to try another city? (Yes/No): ")
		if retry.lower().strip() == "yes":
			return True				
		elif retry.lower().strip() == "no":
			print("***Thanks for using the app***")
			return False
			exit()
		else:
			print("Invalid input! Returning to the main menu.")
			return True	
		
if __name__ == "__main__":
	print("***Welcome to the Weather app***")
	print("Enter \'exit\'' to exit the app!")
	api_key = "c73c791649f916a75baaa2cfb823d7b9"
	while True:
		city = input("\nEnter the name of the city: ")
		if city.lower().strip() == "exit":
			conform = input("Are you sure about exiting the app(Yes/No): ")
			if conform.lower().strip() == "yes":
				print("\n***Thanks for using the app***")
				exit()
			elif conform.lower().strip() == "no":
				print("OK! Continuing...")
				continue
			else:
				print("Invalid input! Please respond with 'yes' or 'no' ")
				continue
		elif city:
			retry = get_weather(city, api_key)
			if retry:
				continue
			else:
				continue
		else:
			print("City name cannot be empty! Please try again.")
		