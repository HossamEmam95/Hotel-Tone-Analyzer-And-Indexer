from flask import Flask, request, Response
import json
app = Flask(__name__)

HOTEL_DATA = json.load(open("n_h_r.json", 'r'))

@app.route('/hotel_tone', methods=['GET'])
def hotel_tone():
    name = request.args.get('name')
    emotion = HOTEL_DATA[name]
    return json.dumps(emotion)


if __name__ == "__main__":

    # start flask app
    app.run(host="0.0.0.0", port=5000)