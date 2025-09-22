from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1> Welcome to my flask App</h1><br><p> This is simple flask application.</p>"
if  __name__== '__main__':
    app.run(debug=True)
