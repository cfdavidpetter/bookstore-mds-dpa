from src.domain.book import BookFormat
from src.services.book_service import BookService
from src.datalayer.repositories.sqlite.book_repository_sqlite import BookRepositorySqlite


def _create_book_data(suffix=""):
  return {
    "title": f"book {suffix}".strip(),
    "author": {
        "title": f"author {suffix}".strip()
    },
    "subjects": [
        {
            "title": "Literary Criticism"
        },
        {
            "title": "American"
        }
    ],
    "isbn13": f"87654321{suffix}",
    "isbn10": f"87654321{suffix}",
    "price": 11.99,
    "format": "Hardcover",
    "publisher": "publisher",
    "pubdate": "October 2007",
    "edition": f"2th Edition {suffix}".strip()
  }


def test_should_list_books(db_sqlite):
  repository = BookRepositorySqlite(db_sqlite)
  service = BookService(repository=repository)

  response = service.list()

  assert len(response.data) > 0  
  assert isinstance(response.data[0].id, int)
  assert response.data[0].title is not None
  assert response.data[0].author.title is not None
  assert response.data[0].author.slug is not None


def test_should_create_book(db_sqlite):
    repository = BookRepositorySqlite(db_sqlite)
    service = BookService(repository=repository)

    book = _create_book_data("01")
    response = service.create(book)

    assert isinstance(response.id, int)
    assert response.title == "book 01"
    assert response.author.title == "author 01"
    assert response.author.slug == "author-01"
    assert response.subjects[0].title == "Literary Criticism"
    assert response.subjects[1].title == "American"
    assert response.isbn13 == 8765432101
    assert response.isbn10 == "8765432101"
    assert response.price == 11.99
    assert response.format == BookFormat.HARDCOVER


def test_should_update_book(db_sqlite):
    repository = BookRepositorySqlite(db_sqlite)
    service = BookService(repository=repository)

    book = _create_book_data()
    response = service.create(book)

    assert isinstance(response.id, int)
    assert response.title == "book"
    assert response.author.title == "author"
    assert response.author.slug == "author"
    assert response.subjects[0].title == "Literary Criticism"
    assert response.subjects[1].title == "American"
    assert response.isbn13 == 87654321
    assert response.isbn10 == "87654321"
    assert response.price == 11.99
    assert response.format == BookFormat.HARDCOVER

    updated_book = _create_book_data("02")
    updated_book["format"] = 'Compact Disc'
    response = service.update(response.id, updated_book)

    assert isinstance(response.id, int)
    assert response.title == "book 02"
    assert response.author.title == "author 02"
    assert response.author.slug == "author-02"
    assert response.subjects[0].title == "Literary Criticism"
    assert response.subjects[1].title == "American"
    assert response.isbn13 == 8765432102
    assert response.isbn10 == "8765432102"
    assert response.price == 11.99
    assert response.format == BookFormat.COMPACT_DISC
