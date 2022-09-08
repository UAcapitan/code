
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from p_2_tdd_example import Batch

from p_5_orm_for_repository import OrderLine
from p_7_repository import SqlAlchemyRepository
from p_4_testing import allocate


# Flask application
get_session = sessionmaker(bind=create_engine("sqlite:///test.db"))
app = Flask(__name__)

@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    session = get_session()

    line = OrderLine("test", "BIG-DESK", 10)
    batches = [Batch("test", "BIG-DESK", 100, None)]

    # batches = SqlAlchemyRepository(session).list()
    # line = OrderLine(
    #     request.json['orderid'],
    #     request.json['sku'],
    #     request.json['qty']
    # )

    batchref = allocate(line, batches)

    return jsonify({"batchref": batchref}), 201


if __name__ == "__main__":
    app.run()
