from typing import List, Optional
import logging

from src.datalayer.interfaces.book_repository_interface import BookRepositoryInterface
from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite
from src.datalayer.repositories.sqlite.schema.book import Book as BookSchema
from src.domain.book import Book
from src.datalayer.repositories.sqlite.adapter.book_adapter import BookAdapter


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BookRepositorySqlite(BookRepositoryInterface):
  def __init__(self, db: DatabaseConnectionSqlite):
    self.db = db
    self.columns = BookSchema.model_fields.keys()
    self.columns_str = ", ".join(self.columns)


  def get_by_id(self, id: int) -> Optional[Book]:
    if not id:
      return None
    
    result = self.db.execute(
      f"SELECT {self.columns_str} FROM book WHERE id = ?",
      (id,),
      fetch=True
    )
    
    if not result:
      return None
    
    return BookAdapter.schema_to_domain(result[0])


  def list(self) -> List[Book]:
    results = self.db.execute(
      f"SELECT {self.columns_str} FROM book",
      fetch=True
    )
      
    return BookAdapter.schema_list_to_domain_list(results)


  def create(self, entity: Book) -> Book:
    entity.id = self.db.get_next_id("book")
    schema_data = BookAdapter.domain_to_schema(entity)

    self.db.execute(
      f"INSERT INTO book ({self.columns_str}) VALUES ({', '.join(['?' for _ in self.columns])})",
      [*schema_data.model_dump().values()],
      fetch=False
    )
    return entity


  def update(self, id: int, entity: Book) -> Book:
    entity.id = id
    schema_data = BookAdapter.domain_to_schema(entity)

    self.db.execute(
      f"UPDATE book SET {', '.join([f'{column} = ?' for column in self.columns])} WHERE id = ?",
      [*schema_data.model_dump().values(), id],
      fetch=False
    )
    return entity


  def delete(self, id: int) -> None:
    self.db.execute(
      "DELETE FROM book WHERE id = ?",
      (id,),
      fetch=False
    )
