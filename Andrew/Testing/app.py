from flask import Flask
app = Flask(__name__)

#creates the home page and outputs onto it
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '_main_':
    app.run()
