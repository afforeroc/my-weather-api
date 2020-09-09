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

2.8 Run more easier.
```
flask run
```

> Stop the app with <kbd>ctrl</kbd> + <kbd>C</kbd>.

> If you need deactivate your virtual env.
```
deactivate
```

## Reference links
* [The Hitchhiker’s Guide to Python - Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)
* [Pythonise - Your first Flask app | Learning Flask Ep. 1](https://pythonise.com/series/learning-flask/your-first-flask-app)
* [Create and configure a Flask app to deploy on Cloud Foundry](https://github.com/afforeroc/flask-cf)
* [freeCodeCamp - How to build a JSON API with Python](https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/)


## Information links
* [Flask Documentation](http://flask.pocoo.org/)


