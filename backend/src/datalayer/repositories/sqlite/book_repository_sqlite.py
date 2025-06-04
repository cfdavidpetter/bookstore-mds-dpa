import logging
from typing import Optional

from src.datalayer.interfaces.book_repository_interface import BookRepositoryInterface
from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite
from src.datalayer.repositories.sqlite.schema.book import Book as BookSchema
from src.datalayer.repositories.sqlite.adapter.book_adapter import BookAdapter
from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, PaginatedResponse
from src.domain.book import Book

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


  def list(self, 
           page: int = DEFAULT_PAGE, 
           page_size: int = DEFAULT_PAGE_SIZE,
           filters: Optional[dict] = None) -> PaginatedResponse[Book]:
    offset = (page - 1) * page_size
    
    query = f"SELECT {self.columns_str} FROM book"
    where = ""

    if filters:
      schema_data_filters = BookAdapter.dev_to_schema_from_filters(filters)
      where = " WHERE "
      for key, value in schema_data_filters.items():
        if value:
          where += f"{key} like '%{value}%' AND "
      where = where[:-5]
      query += where + f" LIMIT {page_size} OFFSET {offset}"
    else:
      query += f" LIMIT {page_size} OFFSET {offset}"

    total_count = self.db.get_total_count("book", where)
    results = self.db.execute(
      query,
      fetch=True
    )

    return PaginatedResponse[Book](
      data=BookAdapter.schema_list_to_domain_list(results),
      total=total_count,
      per_page=page_size,
      from_index=offset,
      current_page=page,
    )


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
