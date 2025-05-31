
from dataclasses import dataclass
from typing import List, Optional

from src.datalayer.interfaces.author_repository_interface import AuthorRepositoryInterface
from src.services.base import ServiceBase
from src.domain.author import Author


@dataclass
class AuthorService(ServiceBase):
  repository: AuthorRepositoryInterface

  def get_by_id(self, id: int) -> Optional[Author]:
    return self.repository.get_by_id(id)
  
  def list(self) -> List[Author]:
    return self.repository.list()
  
  def create(self, author: dict) -> Author:
    return self.repository.create(Author(**author))
  
  def update(self, id: int, author: dict) -> Author:
    return self.repository.update(id, Author(**author))
  
  def delete(self, id: int) -> None:
    return self.repository.delete(id)