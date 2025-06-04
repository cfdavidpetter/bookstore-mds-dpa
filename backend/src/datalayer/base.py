from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from src.datalayer.repositories.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, PaginatedResponse



T = TypeVar('T')

class RepositoryInterface(ABC, Generic[T]):
  @abstractmethod
  def get_by_id(self, id: int) -> Optional[T]:
    pass

  @abstractmethod
  def list(self, 
           page: int = DEFAULT_PAGE, 
           page_size: int = DEFAULT_PAGE_SIZE, 
           filters: Optional[dict] = None) -> PaginatedResponse[T]:
    pass

  @abstractmethod
  def create(self, entity: T) -> T:
    pass

  @abstractmethod
  def update(self, id: int, entity: T) -> T:
    pass

  @abstractmethod
  def delete(self, id: int) -> None:
    pass
  