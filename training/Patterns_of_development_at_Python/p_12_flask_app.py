
import requests
from flask import Flask, jsonify
import multiprocessing
import os
import pytest

from p_2_tdd_example import Batch
from p_5_orm_for_repository import OrderLine
from p_4_testing import OutOfStock, allocate


# Batch
class Batch(Batch):
    def __lt__(self, obj):
        if self.eta == None and self.eta == None: return True
        return self.eta < self.eta

# Flask application
app = Flask(__name__)

def valid_sku(sku, batches):
    return sku in {b.sku for b in batches}

@app.route("/allocate", methods=["POST"])
def allocate_endpoint():

    line = OrderLine("test", "BIG-DESK", 10)
    batches = [
        Batch("test", "BIG-DESK", 100, None),
        Batch("test2", "MIDDLE-DESK", 50, None),
        Batch("test3", "LITTLE-DESK", 30, None)
    ]

    if not valid_sku(line.sku, batches):
        return jsonify({"mesage": "No item in batches"}), 400

    try:
        batchref = allocate(line, batches)
    except OutOfStock as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"batchref": batchref}), 201

if __name__ == "__main__":
    app.run()