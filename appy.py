import os
from os.path import join, dirname
from dotenv import load dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient


client = MongoClient('mongodb+srv://ariefrh208:ariefrh208@cluster0.dezol0o.mongodb.net/')

db = client.cluster0
app = Flask(__name__)

dotenv_path-join(dirname(__file__), '.env')
Load dotenv(dotenv.path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    address_receive = request.form['addres_give']
    size_receive = request.form['size_give']
    doc = {
        'name' : name_receive,
        'addres' : addres_receive,
        'size' : size_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)