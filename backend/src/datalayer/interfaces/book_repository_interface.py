from src.datalayer.base import RepositoryInterface
from src.domain.book import Book

class BookRepositoryInterface(RepositoryInterface[Book]):
  pass