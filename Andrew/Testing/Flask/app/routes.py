from app import app

@app.route('/')
def index():
        return "Hello, World!"
    
@app.route('/index')
def output():
        return "No"