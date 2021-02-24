from flask import Flask, request, jsonify
from weather import getWeather
from zedge import zGetTrendingRintones,zGetSearchResultsRingtones,zGetRelatedSearches
from ring import ringtone as r
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)


@app.route('/')
def home():
    return "API is UP!<br><br>A part of @imsudip's project"

# ringtone.net api
@app.route('/ringtonesHome')
def ringtonesHome():
    if request.method == 'GET':
        return jsonify(r.getTrendingRingtones())

@app.route('/ringtones')
def ringtones():
    if request.method == 'GET':
        return jsonify(r.getRingtonesFromCat(request.args.get('q'), request.args.get('page')))

# weather api
@app.route('/weather')
def weather():
    if request.method == 'GET':
        return jsonify(getWeather(request.args.get('city')))

# zedge ringtone api

@app.route('/zedgeRingtonesAll')
def zedgeRingtonesAll():
    if request.method == 'GET':
        return jsonify(zGetTrendingRintones(request.args.get('page')))

@app.route('/zedgeSearch')
def zedgeSearch():
    if request.method == 'GET':
        return jsonify(zGetSearchResultsRingtones(request.args.get('q'),request.args.get('page')))

@app.route('/zedgeRelatedSearches')
def zedgeRelatedSearches():
    if request.method == 'GET':
        return jsonify(zGetRelatedSearches(request.args.get('q')))



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
