# My Weather API
This is my weather API that uses data from OpenWeatherMap service.

## Prerequisites
* Ubuntu 20.04 LTS

### 1. Basic software configuration
1.1 Check if Python 3 is already installed in your Operative System.
```
$ python3 --version
```
```
$ pip3 --version
```

1.2 If Python 3 isn't installed, please check this [article](https://docs.python-guide.org/starting/install3/linux/).

1.3 Install Python Virtual Environment.
```
$ sudo apt-get install python3-venv
```

1.4 Install 'dotenv' library.
```
$ pip3 install python-dotenv
```

### 2. Virtual Env and Flask Configuration
2.1 Enter inside app folder.
```
$ cd first-poc/
```

2.2 Create a Python virtual environment.
```
$ python3 -m venv env
```

2.3 Activate the environment.
```
$ source env/bin/activate
```

2.4 Updating pip.
```
$ pip3 install --upgrade pip
```

2.5 Installing Flask and check the associated packages.
```
$ pip3 install flask
```
```
$ pip3 list
```

2.6 Check first app running.
```
$ python3 app.py
```

2.7 Config Flask environment variables.
```
export FLASK_APP=app.py
export FLASK_ENV=development
```

## 3. Running app
3.1 Run the app with Flask environment variables. 
```
flask run
```

> Stop the app with <kbd>ctrl</kbd> + <kbd>C</kbd>.

> If you need deactivate your virtual env.
```
deactivate
```

3.2 Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and you should see data like this:
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

## Reference links
* [The Hitchhiker’s Guide to Python - Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)
* [Pythonise - Your first Flask app | Learning Flask Ep. 1](https://pythonise.com/series/learning-flask/your-first-flask-app)
* [Create and configure a Flask app to deploy on Cloud Foundry](https://github.com/afforeroc/flask-cf)
* [freeCodeCamp - How to build a JSON API with Python](https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/)
* [Medium - OSError: [Errno 98] Address already in use Flask error](https://medium.com/@tessywangari05/oserror-errno-98-address-already-in-use-flask-error-ccbff65e2bb5)
* [tutorialspoint - How to convert unix timestamp string to readable date in Python?](https://www.tutorialspoint.com/How-to-convert-unix-timestamp-string-to-readable-date-in-Python#:~:text=How%20to%20convert%20unix%20timestamp%20string%20to%20readable%20date%20in%20Python%3F,-PythonServer%20Side&text=You%20can%20use%20the%20fromtimestamp,object%20corresponding%20to%20the%20timestamp.)
* [GeekforGeeks - Create a Weather app using Flask | Python](https://www.geeksforgeeks.org/create-a-weather-app-using-flask-python/)
* [stackoverflow - Prevent Flask jsonify from sorting the data](https://stackoverflow.com/questions/43263356/prevent-flask-jsonify-from-sorting-the-data/43263483)
* [stackoverflow - Multiple parameters in in Flask approute](https://stackoverflow.com/questions/15182696/multiple-parameters-in-in-flask-approute)


## Information links
* [Flask Documentation](http://flask.pocoo.org/)
* [PyPI - python-dotenv](https://pypi.org/project/python-dotenv/)
* [OpenWeather - Weather parameters in API response - JSON response](https://openweathermap.org/current#current_JSON)