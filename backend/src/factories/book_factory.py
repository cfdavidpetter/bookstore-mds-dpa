from src.datalayer.base import RepositoryInterface
from src.services.base import ServiceBase
from src.services.book_service import BookService
from src.datalayer.repositories.sqlite.book_repository_sqlite import BookRepositorySqlite
from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite

class BookFactory:

  @staticmethod
  def service() -> BookService:
    repository: RepositoryInterface = BookRepositorySqlite(DatabaseConnectionSqlite())
    service: ServiceBase = BookService(repository=repository)
    return service