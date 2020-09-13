# My Weather API
This is My Weather API that provides current information of a city's weather that you want.<br>
This service is free and use data from Current Weather API of OpenWeatherMap.

## Prerequisites
* Ubuntu 20.04 LTS
* Python 3.8.2

## Guideline

### 1. Basic system configuration
> Only once before you run the app

1.1 Check if Python and Pip is already installed in your computer.
```
$ python3 --version
```

1.2 If Python isn't installed, please check this [article](https://docs.python-guide.org/starting/install3/linux/).

1.3 Install Python Virtual Environment (a manager of enviroment for Python packages).
```
$ sudo apt-get install python3-venv
```

1.4 In this step, you should be downloaded or clonated this [repository](https://github.com/afforeroc/my-weather-api). :)

### 2. Python enviroment configuration
> Only once before you run the app

2.1 Enter inside app folder.
```
$ cd my-weather-api/api-core/
```

2.2 Create a Python virtual environment.
```
$ python3 -m venv env
```

2.3 Activate the created virtual environment.
```
$ source env/bin/activate
```

2.4 Updating Pip for the virtual environment.
```
$ pip3 install --upgrade pip
```

2.5 Check Pip version of your virtual env.
```
$ pip3 --version
```

2.6 Install the required packages: `flask`, `dotenv` and `flask-caching`.
```
$ pip3 install flask flask-caching python-dotenv
```

2.7 Test in your terminal/console that the flask app is only running.<br>
You can use:
```
$ flask run
```
Or this:
```
$ python3 app.py
```

Check that in your console appears something like that:
```
 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 155-460-756
```
After, that please stop the app with <kbd>ctrl</kbd> + <kbd>C</kbd>.

2.8 Deactivate the virtual env.
```
$ deactivate
```

### 3. Dot enviroment configuration
> Only once before you run the app

3.1 Enter inside app folder.
```
$ cd my-weather-api/api-core/
```

3.2 Edit the `new.env` file and put the requerired `API_URL` and `API_KEY` of your [Current Weather](https://openweathermap.org/current) API of OpenWeatherMap. Here a example, that you can use only for testing purpose.<br>
```
API_URL='http://api.openweathermap.org/data/2.5/weather?q='
API_KEY='130c6e79354386b51a46509341685172'
```

3.3 After that, save it and rename the file like this:
```
[before] new.env -> [after] .new
```

3.4 ALso, if you want to modify the Flask enviroment, only edit the content of `.flaskenv` file.

### 4. Run the app
> Every time when you run the app

4.1 Enter inside app folder.
```
$ cd my-weather-api/api-core/
```

4.2 Activate the environment.
```
$ source env/bin/activate
```

4.3 Run the app with Flask environment variables. 
```
$ flask run
```

4.4 Make your API request.<br>
Please see **5. Make the API request section**.

4.5 Stop the app with <kbd>ctrl</kbd> + <kbd>C</kbd>.

4.6 I recommended deactivate your virtual env, if you are not going to run the application anymore.
```
$ deactivate
```

### 5. Make the API request
> Every time when you run the app

5.1 Edit the following URL template and replace the `<>` fields and put the required args.
```
http://127.0.0.1:5000/weather?city=<>&country=<xx>
```

e.g. city=**Bogota** (Bogotá DC), country=**co** (Colombia).
```
http://127.0.0.1:5000/weather?city=Bogota&country=co
```

5.2 Remember:
* **city**: a string name without numbers or special characters.<br>
* **country**: a string with only two lower letters without numbers or special characters.

Please check the [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) for the available country codes that is possible to use.

5.3 After that, put the URL on your favorite web browser and check the response on JSON format. e.g.<br>
```
{
  "location_name": "Bogotá, CO",
  "temperature": "11 °C",
  "wind": "1.0 m/s, 0 deg",
  "cloudines": "Broken clouds",
  "pressure": "1030 hPa",
  "humidity": "87%",
  "sunrise": "05:48",
  "sunset": "17:58",
  "geo_coordinates": [
    "4.61",
    "-74.08"
  ],
  "requested_time": "2020-09-09 22:45:02"
}
```

5.4 Check by console. e.g.<br>
```
user@user:~$ curl "http://127.0.0.1:5000/weather?city=bogota&country=co"
{
  "location_name": "Bogotá, CO", 
  "temperature": "12 °C", 
  "wind": "0.21 m/s, 115 deg", 
  "cloudines": "Broken clouds", 
  "pressure": "1027 hPa", 
  "humidity": "93%", 
  "sunrise": "05:48", 
  "sunset": "17:57", 
  "geo_coordinates": [
    "4.61", 
    "-74.08"
  ], 
  "requested_time": "2020-09-11 02:23:33"
}
```

```
user@user:~$ curl -s -I "http://127.0.0.1:5000/weather?city=bogota&country=co"
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 330
Server: Werkzeug/1.0.1 Python/3.8.2
Date: Fri, 11 Sep 2020 07:09:45 GMT
```

## Development: features status
Feactures of this weather API.

1. GET /weather?city=$City&country=$Country :heavy_check_mark: :heavy_check_mark:
```
Response:  {
    "location_name": "Bogota, CO",
    "temperature": "17 °C",
    "wind": Gentle breeze, 3.6 m/s, west-northwest",
    "cloudines": "Scattered clouds",
    "presure": "1027 hpa",
    "humidity": "63%",
    "sunrise": "06:07",
    "sunset": "18:00",
    "geo_coordinates": "[4.61, -74.08]",
    "requested_time": "2018-01-09 11:57:00"
}
```
2. City is a string. Example: Bogota :heavy_check_mark: :heavy_check_mark:

3. Country is a country code of two characters in lowercase. Example: co :heavy_check_mark: :heavy_check_mark:

4. This endpoint should use an external API to get the proper info, here is an example: http://api.openweathermap.org/data/2.5/weather?q=Bogota,co&appid=1508a9a4840a5574c822d70ca2132032 :heavy_check_mark: :heavy_check_mark:

5. The data must be human-readable :heavy_check_mark: :heavy_check_mark:

6. Use environment variables for configuration :heavy_check_mark: :heavy_check_mark:

7. Log errors to the terminal using a middleware :heavy_check_mark:

8. The response must include the content-type header (application/JSON) :heavy_check_mark: :heavy_check_mark:

9. Functions must be tested :heavy_check_mark: :heavy_check_mark:

10. Keep a cache of 2 minutes of the data. You can use a persistent layer for this. :heavy_check_mark:


## Reference links
* [Flask Documentation](http://flask.pocoo.org/)
* [PyPI - python-dotenv](https://pypi.org/project/python-dotenv/)
* [OpenWeather - Weather parameters in API response - JSON response](https://openweathermap.org/current#current_JSON)
* [OpenWeather - Current Weather Data API](https://openweathermap.org/current)
* [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
* [Rafael Xavier de Souza - Complete list of github markdown emoji markup](https://gist.github.com/rxaviers/7360908)

<!--
## Information source
* [The Hitchhiker’s Guide to Python - Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)
* [Pythonise - Your first Flask app | Learning Flask Ep. 1](https://pythonise.com/series/learning-flask/your-first-flask-app)
* [Create and configure a Flask app to deploy on Cloud Foundry](https://github.com/afforeroc/flask-cf)
* [freeCodeCamp - How to build a JSON API with Python](https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/)
* [Medium - OSError: [Errno 98] Address already in use Flask error](https://medium.com/@tessywangari05/oserror-errno-98-address-already-in-use-flask-error-ccbff65e2bb5)
* [tutorialspoint - How to convert unix timestamp string to readable date in Python?](https://www.tutorialspoint.com/How-to-convert-unix-timestamp-string-to-readable-date-in-Python#:~:text=How%20to%20convert%20unix%20timestamp%20string%20to%20readable%20date%20in%20Python%3F,-PythonServer%20Side&text=You%20can%20use%20the%20fromtimestamp,object%20corresponding%20to%20the%20timestamp.)
* [GeekforGeeks - Create a Weather app using Flask | Python](https://www.geeksforgeeks.org/create-a-weather-app-using-flask-python/)
* [Stack Overflow - Prevent Flask jsonify from sorting the data](https://stackoverflow.com/questions/43263356/prevent-flask-jsonify-from-sorting-the-data/43263483)
* [Stack Overflow - Multiple parameters in in Flask approute](https://stackoverflow.com/questions/15182696/multiple-parameters-in-in-flask-approute)
* [Stack Overflow - flask restful: passing parameters to GET request](https://stackoverflow.com/questions/30779584/flask-restful-passing-parameters-to-get-request)
* [Stack Overflow - How to check that a string contains only “a-z”, “A-Z” and “0-9” characters](https://stackoverflow.com/questions/57011986/how-to-check-that-a-string-contains-only-a-z-a-z-and-0-9-characters)
* [Stack Overflow - Regex to check if first 2 characters in a string are Alphabets](https://stackoverflow.com/questions/6311030/regex-to-check-if-first-2-characters-in-a-string-are-alphabets/6311081)
* [Stack Overflow - Forcing application/json MIME type in a view (Flask)](https://stackoverflow.com/questions/11945523/forcing-application-json-mime-type-in-a-view-flask)
* [Stack Overflow - Curl show Content-Type only](https://stackoverflow.com/questions/23675967/curl-show-content-type-only/23676198)
* [Stack Overflow - python jsonify dictionary in utf-8](https://stackoverflow.com/questions/14853694/python-jsonify-dictionary-in-utf-8)
* [parisnakitakejser/video-tutorial-python-code](https://github.com/parisnakitakejser/video-tutorial-python-code/tree/master/Flask)
* [Pretty Printed - Intro to Flask-Caching](https://www.youtube.com/watch?v=iO0sL6Vyfps)
* [Stack Overflow - What is the easiest way to get current GMT time in Unix timestamp format?](https://stackoverflow.com/questions/16755394/what-is-the-easiest-way-to-get-current-gmt-time-in-unix-timestamp-format)
-->