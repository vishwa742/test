from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Congratulations! Your part 2 endpoint is working'
