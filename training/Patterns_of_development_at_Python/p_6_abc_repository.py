
import abc
from p_4_testing import Batch

class AbstractRepository(abc.ABC):

    @abc.abstractclassmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractclassmethod
    def get(self, reference: str) -> Batch:
        raise NotImplementedError
