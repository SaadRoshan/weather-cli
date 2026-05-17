# Weather CLI 🌤

A command-line weather app built with Python that fetches real-time 
weather data for any city in the world.

## What it does
- Takes a city name as input
- Fetches live weather data from the OpenWeatherMap API
- Displays temperature, conditions, humidity and wind speed

## Demo
Enter city name: Denver
===================================
Weather in Denver, US
Condition   : Clear Sky
Temperature : 22°C
Feels like  : 20°C
Humidity    : 34%
Wind speed  : 5 km/h


## Tech stack
- Python 3.11
- requests
- python-dotenv
- OpenWeatherMap API

## How to run it

1. Clone the repo
   git clone https://github.com/SaadRoshan/weather-cli.git
   cd weather-cli

2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Get a free API key from openweathermap.org
   and add it to a .env file
   OPENWEATHER_API_KEY=your_key_here

5. Run it
   python src/main.py

## What I learned
- Calling a REST API with Python using the requests library
- Handling API keys securely with environment variables
- Parsing JSON responses and extracting specific fields
- Structuring a Python project with virtual environments