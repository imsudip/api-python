#Coded by Sumanjay on 29th Feb 2020
from flask import Flask, request, jsonify
from weather import getWeather
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)

@app.route('/')
def home():
    return 'News API is UP!<br><br>A part of <a href="https://t.me/sjprojects">Sj Projects</a>'


@app.route('/weather')
def weather():
    if request.method == 'GET':
        return jsonify(getWeather(request.args.get('city')))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)