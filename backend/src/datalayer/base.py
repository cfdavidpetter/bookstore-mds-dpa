from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')

class RepositoryInterface(ABC, Generic[T]):
  @abstractmethod
  def get_by_id(self, id: int) -> Optional[T]:
    pass

  @abstractmethod
  def list(self) -> List[T]:
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
  