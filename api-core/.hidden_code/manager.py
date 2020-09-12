from flask import Flask
from flask_script import Manager, Server

def custom_call():
    #Your code
    pass

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        custom_call()
        #Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)

app = Flask(__name__)
@app.route('/weather', methods=['GET'])
def weather():
    return 0
manager = Manager(app)

# Remeber to add the command to your Manager instance
manager.add_command('runserver', CustomServer())

if __name__ == "__main__":
    manager.run()