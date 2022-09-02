
from dataclasses import dataclass
from typing import Optional
from datetime import date


# Tests
def get_batch_and_line(sku: str, qty: int, qty_line: int) -> tuple:
    return (
        Batch("batch-001", sku, qty=qty, eta=date.today()),
        OrderLine("order-ref", sku, qty_line)
    )

def test_batch():
    batch, line = get_batch_and_line("SMALL-TABLE", 20, 2)
    batch.allocate(line)
    assert batch.available_quantity == 18

def test_batch_2():
    batch, line = get_batch_and_line("SMALL-TABLE", 15, 5)
    batch.allocate(line)
    assert batch.available_quantity == 10

def test_can_allocation():
    batch, line = get_batch_and_line("SMALL-TABLE", 20, 2)
    assert batch.can_allocate(line)

def test_can_allocation_2():
    batch, line = get_batch_and_line("SMALL-TABLE", 2, 20)
    assert batch.can_allocate(line) is False

def test_can_allocation_3():
    batch, line = get_batch_and_line("SMALL-TABLE", 20, -2)
    assert batch.can_allocate(line) is False

def test_can_allocation_4():
    batch = Batch("batch-001", "SMALL_TABLE", 20, eta=date.today())
    line = OrderLine("order-ref", "EXPENSIVE-TOASTER", 2)
    assert batch.can_allocate(line) is False

def test_deallocate():
    batch, line = get_batch_and_line("SMALL-TABLE", 20, 2)
    batch.deallocate(line)
    assert batch.available_quantity == 20

def test_allocation_is_idempotent():
    batch, line = get_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18


# Emulation of code for application
@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty and line.qty > 0

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity
