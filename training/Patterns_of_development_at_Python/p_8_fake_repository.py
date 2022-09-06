
from p_6_abc_repository import AbstractRepository
from p_4_testing import Batch

class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)

    def add(self, batch):
        self._batches.add(batch)

    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)

fake_repo = FakeRepository([
    Batch("batch-001", "LITTLE-DESK", qty=100, eta=None),
    Batch("batch-002", "MIDDLE-DESK", qty=90, eta=None),
    Batch("batch-003", "HARD-DESK", qty=110, eta=None)
])