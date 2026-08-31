"""
Fetch live weather from a web API and read the JSON it sends back.

This is the payoff for the requests module we installed with pip in Week 7.
Three steps, and each one is a single line:

1. requests.get sends the request and hands back a response object.
2. response.status_code tells us whether the server was happy. Always check
   it before you trust the body: a 404 page is not the data you asked for.
3. response.json() converts the JSON body straight into a Python dict, so
   we never have to call json.loads ourselves.

The API is Open-Meteo, which is free and needs no key and no sign-up. Never
paste an API key into a file you are going to commit; Week 12 shows how to
keep secrets in a .env file instead.
"""

import requests

VANCOUVER_LATITUDE = 49.2827
VANCOUVER_LONGITUDE = -123.1207

# The World Meteorological Organization publishes these codes. This dict
# covers the ones Vancouver actually sees; the full table is much longer.
WEATHER_CODES = {
    0: 'clear sky',
    1: 'mainly clear',
    2: 'partly cloudy',
    3: 'overcast',
    45: 'fog',
    48: 'freezing fog',
    51: 'light drizzle',
    53: 'drizzle',
    55: 'heavy drizzle',
    61: 'light rain',
    63: 'rain',
    65: 'heavy rain',
    71: 'light snow',
    73: 'snow',
    75: 'heavy snow',
    80: 'light rain showers',
    81: 'rain showers',
    82: 'violent rain showers',
    95: 'thunderstorm',
}


def build_url(latitude: float, longitude: float) -> str:
    """
    Build the Open-Meteo request URL for one location.

    :param latitude: a float degree of latitude
    :param longitude: a float degree of longitude
    :precondition: latitude is a float between -90 and 90
    :precondition: longitude is a float between -180 and 180
    :return: the request URL as a str

    >>> build_url(0.0, 0.0)
    'https://api.open-meteo.com/v1/forecast?latitude=0.0&longitude=0.0&current=temperature_2m,weather_code'
    >>> build_url(49.2827, -123.1207).startswith('https://')
    True
    """
    return (f'https://api.open-meteo.com/v1/forecast'
            f'?latitude={latitude}&longitude={longitude}'
            f'&current=temperature_2m,weather_code')


def fetch_weather(url: str) -> dict:
    """
    Download the JSON document at url and return it as a Python dict.

    Notice there is no json.loads here. The response object already knows how
    to parse its own body, so response.json() does that work for us.

    :param url: a str containing a URL that returns JSON
    :precondition: url is a str
    :precondition: the machine running this program is online
    :return: the parsed JSON document as a dict
    :raises ValueError: if the server answers with any status other than 200
    """
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise ValueError(f'the server answered {response.status_code}')
    return response.json()


def describe_weather_code(code: int) -> str:
    """
    Translate a World Meteorological Organization weather code into English.

    :param code: an int weather code sent by the API
    :precondition: code is an int
    :return: a str describing the weather, or a fallback for unknown codes

    >>> describe_weather_code(0)
    'clear sky'
    >>> describe_weather_code(65)
    'heavy rain'
    >>> describe_weather_code(9999)
    'weather code 9999'
    """
    return WEATHER_CODES.get(code, f'weather code {code}')


def main():
    """
    Drive the program.
    """
    url = build_url(VANCOUVER_LATITUDE, VANCOUVER_LONGITUDE)
    print('Asking:', url)

    try:
        forecast = fetch_weather(url)
    except ValueError as error:
        print('The request failed:', error)
        return
    except requests.RequestException as error:
        print('Could not reach the server:', error)
        return

    now = forecast['current']
    units = forecast['current_units']
    print('\nCurrent weather in Vancouver')
    print(f"  observed at {now['time']}")
    print(f"  temperature {now['temperature_2m']}{units['temperature_2m']}")
    print(f"  conditions  {describe_weather_code(now['weather_code'])}")


if __name__ == '__main__':
    main()
