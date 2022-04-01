from app import app

#creates the home page and outputs Hello World to it
@app.route('/')
def index():
        return "Hello, World!"
    
@app.route('/index')
def output():
        return "No"
