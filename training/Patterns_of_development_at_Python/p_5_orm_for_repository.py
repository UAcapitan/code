
from sqlalchemy.orm import mapper, sessionmaker
from dataclasses import dataclass
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
import pytest


# New OrderLine
@dataclass(unsafe_hash=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

# Order lines layer for database
metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255))
)

# Function for getting mapper
def start_mappers():
    return mapper(OrderLine, order_lines)

start_mappers()

# Tests
@pytest.fixture
def session():
    engine = create_engine('sqlite:///test.db')
    metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()
    yield Session
    Session.close()

def test_orderline_mapper_can_load_lines(session):
    session.execute(
        'INSERT INTO order_lines (orderid, sku, qty) VALUES '
        '("order1", "RED-CHAIR", 12),'
        '("order2", "RED-TABLE", 13),'
        '("order3", "BLUE-LIPSTICK", 14)'
    )
    expected = [
        OrderLine("order1", "RED-CHAIR", 12),
        OrderLine("order2", "RED-TABLE", 13),
        OrderLine("order3", "BLUE-LIPSTICK", 14)
    ]
    assert session.query(OrderLine).all() == expected

def test_orderline_mapper_can_save_lines(session):
    new_line = OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(new_line)
    session.commit()

    rows = list(session.execute('SELECT orderid, sku, qty FROM order_lines;'))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]

    session.delete(new_line)
    session.commit()
