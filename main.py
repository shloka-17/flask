from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> HI THERE</h1>'

@app.route('/info')
def info():
    return 'I am in 9th grade'

if __name__ == "__main__":
    app.run(debug=True)
    '<h1> Home Page'