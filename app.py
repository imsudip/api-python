# Coded by Sumanjay on 29th Feb 2020
from flask import Flask, request, jsonify
from weather import getWeather
from zedge import zGetTrendingRintones,zGetSearchResultsRingtones
from ringtone import getTrendingRingtones,getRingtonesFromCat
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)


@app.route('/')
def home():
    return "API is UP!<br><br>A part of @imsudip's project"


@app.route('/ringtonesHome')
def ringtonesHome():
    if request.method == 'GET':
        return jsonify(getTrendingRingtones())

@app.route('/zedgeRingtonesAll')
def zedgeRingtonesAll():
    if request.method == 'GET':
        return jsonify(zGetTrendingRintones(request.args.get('page')))
@app.route('/zedgeSearch')
def zedgeSearch():
    if request.method == 'GET':
        return jsonify(zGetSearchResultsRingtones(request.args.get('q'),request.args.get('page')))

@app.route('/ringtones')
def ringtones():
    if request.method == 'GET':
        return jsonify(getRingtonesFromCat(request.args.get('q'), request.args.get('page')))


@app.route('/weather')
def weather():
    if request.method == 'GET':
        return jsonify(getWeather(request.args.get('city')))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
