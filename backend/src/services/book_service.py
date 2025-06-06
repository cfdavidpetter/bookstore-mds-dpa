from dataclasses import dataclass
from typing import Optional

from src.datalayer.interfaces.book_repository_interface import BookRepositoryInterface
from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, PaginatedResponse
from src.services.base import ServiceBase
from src.domain.book import Book
from src.utils.parsing import extract_dict_filters_from_string


@dataclass
class BookService(ServiceBase):
  repository: BookRepositoryInterface

  def get_by_id(self, id: int) -> Optional[Book]:
    return self.repository.get_by_id(id)
  
  def list(self, 
           page: Optional[int] = DEFAULT_PAGE, 
           page_size: Optional[int] = DEFAULT_PAGE_SIZE,
           filters: Optional[str] = None) -> PaginatedResponse[Book]:
    filters = extract_dict_filters_from_string(filters)
    return self.repository.list(page, page_size, filters)
  
  def create(self, book: dict) -> Book:
    return self.repository.create(Book(**book))
  
  def update(self, id: int, book: dict) -> Book:
    return self.repository.update(id, Book(**book))
  
  def delete(self, id: int) -> None:
    return self.repository.delete(id)