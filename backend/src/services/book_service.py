
from dataclasses import dataclass
from typing import List, Optional

from src.datalayer.interfaces.book_repository_interface import BookRepositoryInterface
from src.services.base import ServiceBase
from src.domain.book import Book


@dataclass
class BookService(ServiceBase):
  repository: BookRepositoryInterface

  def get_by_id(self, id: int) -> Optional[Book]:
    return self.repository.get_by_id(id)
  
  def list(self) -> List[Book]:
    return self.repository.list()
  
  def create(self, book: dict) -> Book:
    return self.repository.create(Book(**book))
  
  def update(self, id: int, book: dict) -> Book:
    return self.repository.update(id, Book(**book))
  
  def delete(self, id: int) -> None:
    return self.repository.delete(id)