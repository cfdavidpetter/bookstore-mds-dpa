import sqlite3

from contextlib import contextmanager
from typing import Generator, Optional, List, Any


class DatabaseConnectionSqlite:
  def __init__(self, db_path: str = 'db.sqlite'):
    self.db_path = db_path

  @contextmanager
  def get_connection(self) -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(self.db_path)
    try:
      yield conn
    finally:
      conn.close()

  def execute(self, query: str, params: tuple = (), fetch: bool = True) -> Optional[List[Any]]:
    with self.get_connection() as conn:
      cursor = conn.cursor()
      cursor.execute(query, params)
      
      if fetch:
        return cursor.fetchall()
      else:
        conn.commit()
        return None
      
  def get_next_id(self, table: str) -> int:
    return self.execute(f"SELECT MAX(id) + 1 FROM {table}", fetch=True)[0][0]

  def get_total_count(self, table: str) -> int:
    return self.execute(f"SELECT COUNT(*) FROM {table}", fetch=True)[0][0]
