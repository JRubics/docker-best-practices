from flask import Flask, jsonify
from flask_cors import CORS
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", port='6379', db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)
CORS(app)

@app.route("/api")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    return jsonify(
        name=os.getenv("PERSON", "world"),
        visits=visits
    )