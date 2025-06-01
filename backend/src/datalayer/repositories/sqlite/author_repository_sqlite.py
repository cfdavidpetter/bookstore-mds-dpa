from typing import List, Optional

from src.datalayer.interfaces.author_repository_interface import AuthorRepositoryInterface
from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite
from src.datalayer.repositories.sqlite.schema.author import Author as AuthorSchema
from src.domain.author import Author


class AuthorRepositorySqlite(AuthorRepositoryInterface):
  def __init__(self, db: DatabaseConnectionSqlite):
    self.db = db
    self.columns = AuthorSchema.model_fields.keys()
    self.columns_str = ", ".join(self.columns)


  def get_by_id(self, id: int) -> Optional[Author]:
    if not id:
      return None
    
    result = self.db.execute(
      f"SELECT {self.columns_str} FROM author WHERE id = ?",
      (id,),
      fetch=True
    )
    
    if not result:
      return None
        
    author_data = result[0]
    return Author(
      id=author_data[0],
      title=author_data[1],
      slug=author_data[2],
      biography=author_data[3]
    )


  def list(self) -> List[Author]:
    results = self.db.execute(
      f"SELECT {self.columns_str} FROM author",
      fetch=True
    )
      
    return [
      Author(
        id=author_data[0],
        title=author_data[1],
        slug=author_data[2],
        biography=author_data[3]
      )
      for author_data in results
    ]


  def create(self, entity: Author) -> Author:
    entity.id = self.db.get_next_id("author")
    self.db.execute(
      f"INSERT INTO author ({self.columns_str}) VALUES ({', '.join(['?' for _ in self.columns])})",
      [*entity.model_dump().values()],
      fetch=False
    )
    return entity


  def update(self, id: int, entity: Author) -> Author:
    entity.id = id
    self.db.execute(
      f"UPDATE author SET {', '.join([f'{column} = ?' for column in self.columns])} WHERE id = ?",
      [*entity.model_dump().values(), id],
      fetch=False
    )
    return entity


  def delete(self, id: int) -> None:
    self.db.execute(
      "DELETE FROM author WHERE id = ?",
      (id,),
      fetch=False
    )
