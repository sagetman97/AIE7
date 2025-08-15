from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dice_roller import DiceRoller

load_dotenv()

mcp = FastMCP("mcp-server")
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    search_results = client.get_search_context(query=query)
    return search_results

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

"""
Weather API tool - Get real-time weather data from WeatherAPI.com API
"""
@mcp.tool()
def get_weather(city: str, country_code: str = "US") -> str:
    """Get current weather information for a specific city using WeatherAPI.com API"""
    import requests
    
    # WeatherAPI.com API endpoint (free tier)
    api_key = os.getenv("WEATHERAPI_KEY")
    if not api_key:
        return "Error: WEATHERAPI_KEY not found in environment variables. Please add it to your .env file."
    
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": f"{city},{country_code}",
        "aqi": "no"  # Don't include air quality data
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract relevant weather information from WeatherAPI.com response
        location = data["location"]
        current = data["current"]
        
        city_name = location["name"]
        country = location["country"]
        weather_description = current["condition"]["text"]
        temperature_c = current["temp_c"]
        feels_like_c = current["feelslike_c"]
        humidity = current["humidity"]
        wind_speed = current["wind_kph"]
        wind_direction = current["wind_dir"]
        
        weather_info = f"Weather in {city_name}, {country}:\n"
        weather_info += f"• Current: {weather_description}\n"
        weather_info += f"• Temperature: {temperature_c}°C\n"
        weather_info += f"• Feels like: {feels_like_c}°C\n"
        weather_info += f"• Humidity: {humidity}%\n"
        weather_info += f"• Wind: {wind_speed} km/h {wind_direction}"
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"
    except KeyError as e:
        return f"Error parsing weather data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")