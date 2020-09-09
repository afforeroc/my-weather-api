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
// 20200909183346
// http://127.0.0.1:5000/

{
  "base": "stations",
  "clouds": {
    "all": 49
  },
  "cod": 200,
  "coord": {
    "lat": 4.61,
    "lon": -74.08
  },
  "dt": 1599694362,
  "id": 3688689,
  "main": {
    "feels_like": 283.25,
    "grnd_level": 749,
    "humidity": 86,
    "pressure": 1014,
    "sea_level": 1014,
    "temp": 284.54,
    "temp_max": 284.54,
    "temp_min": 284.54
  },
  "name": "Bogotá",
  "sys": {
    "country": "CO",
    "sunrise": 1599648520,
    "sunset": 1599692318
  },
  "timezone": -18000,
  "visibility": 10000,
  "weather": [
    {
      "description": "scattered clouds",
      "icon": "03n",
      "id": 802,
      "main": "Clouds"
    }
  ],
  "wind": {
    "deg": 125,
    "speed": 1.58
  }
}
```

## Reference links
* [The Hitchhiker’s Guide to Python - Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)
* [Pythonise - Your first Flask app | Learning Flask Ep. 1](https://pythonise.com/series/learning-flask/your-first-flask-app)
* [Create and configure a Flask app to deploy on Cloud Foundry](https://github.com/afforeroc/flask-cf)
* [freeCodeCamp - How to build a JSON API with Python](https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/)


## Information links
* [Flask Documentation](http://flask.pocoo.org/)
* [PyPI - python-dotenv](https://pypi.org/project/python-dotenv/)