import pandas as pd
from flask import Flask, request, Response
import json
import requests

app = Flask(__name__)


def add_raw(raw):
    url = "http://localhost:9200/hotel_index/node-1"
    payload = raw
    # print(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    res = requests.request("POST", url, headers=headers, data=payload)
    



@app.route('/hotel_index', methods=['GET'])
def post_raw():
    data = pd.read_csv("hotel_dataset.csv")
    data = data.reset_index() 

    for index, raw in data.iterrows():
        raw = raw.to_json()
        add_raw(raw)
    return json.dumps({"status": "created" })

@app.route('/get_hotel', methods=['GET'])
def get_hotel():
    name = request.args.get('name')
    url = f"http://localhost:9200/_search?q=name:\"{name}\""

    payload={}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.dumps(response.text)



if __name__ == "__main__":

    # start flask app
    app.run(host="0.0.0.0", port=5000)