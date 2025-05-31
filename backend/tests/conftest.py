import pytest

from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite

@pytest.fixture
def db_sqlite():
    return DatabaseConnectionSqlite('db_test.sqlite')
