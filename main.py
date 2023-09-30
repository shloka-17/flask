from flask import Flask 

app = Flask(__name__)

@app.route('/')
    return 'I am in 9th grade'

if __name__ == "__main__":
    app.run(debug=True)