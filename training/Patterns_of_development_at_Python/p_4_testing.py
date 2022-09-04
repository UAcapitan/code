
from p_2_tdd_example import Batch, OrderLine
from datetime import date
import pytest


# Updated Batch class
class Batch(Batch):
    def __lt__(self, obj):
        if self.eta is None:
            return False
        if obj.eta is None:
            return True
        if isinstance(obj.eta, int):
            return self.eta < obj.eta

    def __eq__(self, obj):
        return self.reference == obj.reference

# Error - Out of stock
class OutOfStock(Exception):
    pass

# Function for allocation
def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
    except StopIteration:
        raise OutOfStock
    batch.allocate(line)
    return batch.reference

# Tests
today: int = 0
tommorow: int = 1
later: int = 3

def test_current_stock():
    in_stock = Batch("in_stock", "RETRO-CLOCK", 100, eta=date.today)
    shipment = Batch("shipment", "RETRO-CLOCK", 100, eta=None)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock, shipment])

    assert in_stock.available_quantity == 90
    assert shipment.available_quantity == 100

def test_current_stock_2():
    easiest = Batch("speedy", "RETRO-CLOCK", 100, eta=today)
    middle = Batch("normal", "RETRO-CLOCK", 100, eta=tommorow)
    latest = Batch("slow", "RETRO-CLOCK", 100, eta=later)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [easiest, middle, latest])

    assert easiest.available_quantity == 90
    assert middle.available_quantity == 100
    assert latest.available_quantity == 100

def test_returns_allocated():
    in_stock = Batch("in_stock", "RETRO-CLOCK", 100, eta=today)
    shipment = Batch("shipment", "RETRO-CLOCK", 100, eta=None)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocation = allocate(line, [in_stock, shipment])

    assert allocation == in_stock.reference

def test_out_of_stock():
    in_stock = Batch("in_stock", "RETRO-CLOCK", 10, eta=today)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock])

    with pytest.raises(OutOfStock):
        allocate(OrderLine("test", "RETRO-CLOCK", 1), [in_stock])
