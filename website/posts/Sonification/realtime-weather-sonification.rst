.. title: Realtime Weather Sonification
.. slug: realtime-weather-sonification
.. date: 2020-11-05 13:47:51 UTC
.. tags: 
.. category: basics:sonification
.. link: 
.. description: 
.. type: text
.. has_math: true
.. data:


OpenWeatherMap
--------------

This first, simple Web Audio sonification application makes use
of the  Weather API for real-time, browser-based sonification
of weather data.
For fetching data, a free subscription is necessary:
https://home.openweathermap.org

Once subscribed, the API key can be used to get current weather
information in the browser:

   https://api.openweathermap.org/data/2.5/weather?q=Potsdam&appid=eab7c410674e15bfdd841f66941a92c2

JSON Data Structure
-------------------
   
The resulting output in JSON looks like this:

.. code-block:: json

  {
    "coord": {
      "lon": 13.41,
      "lat": 52.52
    },
    "weather": [
      {
	"id": 804,
	"main": "Clouds",
	"description": "overcast clouds",
	"icon": "04d"
      }
    ],
    "base": "stations",
    "main": {
      "temp": 9.74,
      "feels_like": 6.57,
      "temp_min": 9,
      "temp_max": 10.56,
      "pressure": 1034,
      "humidity": 93
    },
    "visibility": 8000,
    "wind": {
      "speed": 4.1,
      "deg": 270
    },
    "clouds": {
      "all": 90
    },
    "dt": 1604655648,
    "sys": {
      "type": 1,
      "id": 1275,
      "country": "DE",
      "sunrise": 1604643143,
      "sunset": 1604676458
    },
    "timezone": 3600,
    "id": 2950159,
    "name": "Berlin",
    "cod": 200
  }


------

All entries of this data structure can be used as
synthesis parameters in a sonification system with
Web Audio.


Temperatures to Frequencies
---------------------------

Mapping
=======

In this example we are using a simple freuency modulation
formula for turning temperature and humidity
into more or less pleasing (annoying) sounds.
The frequency of a first oscillator is derived
from the temperature:

:math:`\displaystyle f_1 = 10 \frac{1}{{T^2 / C^{\circ} }}`

The modulator frequency is controlled by the humidity :math:`H`:
      
:math:`y = sin(2 \pi (f_1 + 100*sin(2 \pi H t))t)`

-----

The Result
----------

The resulting app fetches the weather data of a chosen city,
extracts temperature and humidity and sets the parameters
of the audio processes:

.. raw:: html
   :file: /media/anwaldt/ANWALDT_2TB/WORK/TEACHING/Computer_Music_Basics/webaudio/weather/weather.html



-----

      
Code
====

.. listing:: weather/weather.html html


Links and More Examples
=======================

Using the API in JavaScript is thoroughly explained here:
https://bithacker.dev/fetch-weather-openweathermap-api-javascript

