
import pytest
from p_4_testing import Batch
from p_6_abc_repository import AbstractRepository
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, create_engine
from sqlalchemy.orm import mapper, sessionmaker


# Tests
@pytest.fixture
def session():
    engine = create_engine('sqlite:///test.db')
    metadata.create_all(engine)
    Session = sessionmaker(bind=engine)()
    yield Session
    Session.close()

def test_repository_can_save_a_batch(session):
    batch = Batch('batch1', 'RUSTY-SOAPDISH', 100, eta=None)

    repo = SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()

    rows = list(session.execute(
        'SELECT reference, sku, _purchased_quantity, eta FROM "batches"'
    ))

    session.delete(batch)
    session.commit()

    assert rows == [("batch1", "RUSTY-SOAPDISH", 100, None)]

def insert_batch(session, batch_id):
    session.execute(
        'INSERT INTO batches (reference, sku, _purchased_quantity, eta)'
        ' VALUES (:batch_id, "GENERIC-SOFA", 100, Null)',
        dict(batch_id=batch_id)
    )
    [[batch_id]] = session.execute(
        'SELECT id FROM batches WHERE reference=:batch_id AND sku="GENERIC-SOFA"',
        dict(batch_id=batch_id)
    )
    return batch_id

def test_repository_can_retrieve_a_batch(session):
    insert_batch(session, "batch1")
    insert_batch(session, "batch2")

    repo = SqlAlchemyRepository(session)
    retrieved = repo.get("batch1")
    
    expected = Batch("batch1", "GENERIC-SOFA", 100, eta=None)

    print(retrieved.reference, retrieved.sku, retrieved._purchased_quantity, retrieved.eta)
    print(expected.reference, expected.sku, expected._purchased_quantity, expected.eta)

    assert retrieved == expected

# Batches for database
metadata = MetaData()

batches = Table(
    'batches', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('reference', String(255)),
    Column('sku', String(255)),
    Column('_purchased_quantity', Integer, nullable=False),
    Column('eta', Date, nullable=True)
)

def start_mappers():
    return mapper(Batch, batches)

start_mappers()

# Realization
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(Batch).all()
