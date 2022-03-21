# Hotel-Tone-Analyzer-And-Indexer

### The Endpoints for both tasks are in the `app.py` file

### the tone aggrigation and association is Done on the `model.ipynb` notebook, also the normalised results for each hotel can be ofund in the `n_h_r.json` file. 

### this project assume you have ElasticSearch server installed and running on port 9200, with a cluster called `hotel_index` and a node called `node-1`

## Get Hotel Normilised tone
use the `localhost:5000/hotel_tone?name=<hotel-name>` API  

## Index All Hotels
use the `localhost:5000/hotel_index` API

## Get Document for a Hotel
use the `localhost:5000/get_hotel?name=<hotel-name>` API 

