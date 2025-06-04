from dataclasses import dataclass
from typing import Optional

from src.datalayer.interfaces.author_repository_interface import AuthorRepositoryInterface
from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, PaginatedResponse
from src.services.base import ServiceBase
from src.domain.author import Author
from src.utils.parsing import extract_dict_filters_from_string


@dataclass
class AuthorService(ServiceBase):
  repository: AuthorRepositoryInterface

  def get_by_id(self, id: int) -> Optional[Author]:
    return self.repository.get_by_id(id)
  
  def list(self, 
           page: Optional[int] = DEFAULT_PAGE, 
           page_size: Optional[int] = DEFAULT_PAGE_SIZE,
           filters: Optional[str] = None) -> PaginatedResponse[Author]:
    filters = extract_dict_filters_from_string(filters)
    return self.repository.list(page, page_size, filters)
  
  def create(self, author: dict) -> Author:
    return self.repository.create(Author(**author))
  
  def update(self, id: int, author: dict) -> Author:
    return self.repository.update(id, Author(**author))
  
  def delete(self, id: int) -> None:
    return self.repository.delete(id)