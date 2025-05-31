from src.datalayer.repositories.sqlite.author_repository_sqlite import AuthorRepositorySqlite
from src.services.author_service import AuthorService


def test_should_list_authors(db_sqlite):
  repository = AuthorRepositorySqlite(db_sqlite)
  service = AuthorService(repository=repository)

  response = service.list()

  assert len(response) > 0
  assert isinstance(response[0].id, int)
  assert response[0].title is not None
  assert response[0].slug is not None
  assert response[0].biography is not None


def test_should_create_author(db_sqlite):
  repository = AuthorRepositorySqlite(db_sqlite)
  service = AuthorService(repository=repository)

  author = {
    "title": "Guilherme",
    "slug": "gui@gui.com",
    "biography": "123456",
  }

  response = service.create(author)
  print(response)

  assert isinstance(response.id, int)
  assert response.title == "Guilherme"
  assert response.slug == "gui@gui.com"
  assert response.biography == "123456"


def test_should_update_author(db_sqlite):
  repository = AuthorRepositorySqlite(db_sqlite)
  service = AuthorService(repository=repository)

  author = {
    "title": "Guilherme",
    "slug": "gui@gui.com",
    "biography": "123456",
  }

  response = service.create(author)
  print(response)

  assert isinstance(response.id, int)
  assert response.title == "Guilherme"
  assert response.slug == "gui@gui.com"
  assert response.biography == "123456"

  author = {
    "title": "Guilherme 2",
    "slug": "gui_2@gui.com",
    "biography": "123456 2",
  }

  response = service.update(response.id, author)
  print(response)

  assert isinstance(response.id, int)
  assert response.title == "Guilherme 2"
  assert response.slug == "gui_2@gui.com"
  assert response.biography == "123456 2"
