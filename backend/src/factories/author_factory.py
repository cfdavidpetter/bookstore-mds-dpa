from src.datalayer.base import RepositoryInterface
from src.services.base import ServiceBase
from src.services.author_service import AuthorService
from src.datalayer.repositories.sqlite.author_repository_sqlite import AuthorRepositorySqlite
from src.datalayer.repositories.sqlite.connection_sqlite import DatabaseConnectionSqlite

class AuthorFactory:

  @staticmethod
  def service() -> AuthorService:
    repository: RepositoryInterface = AuthorRepositorySqlite(DatabaseConnectionSqlite())
    service: ServiceBase = AuthorService(repository=repository)
    return service