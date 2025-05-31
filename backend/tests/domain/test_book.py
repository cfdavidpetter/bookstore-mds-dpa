from src.domain.book import Book, BookFormat
from src.domain.author import Author
from src.domain.subject import Subject


def test_should_create_book():
  book: Book = Book(
    id=1, 
    title="The Great Gatsby",
    author=Author(id=1, title="F. Scott Fitzgerald", biography="A novel by F. Scott Fitzgerald"),
    authors=[],
    isbn13=1234567890,
    isbn10="1234567890",
    price=10.99,
    format=BookFormat.PAPERBACK,
    publisher="Scribner",
    pubdate="1925",
    edition="1st",
    subjects=[Subject(id=1, title="Romance Books")],
    lexile="800L",
    pages=180,
    dimensions="6x9",
    overview="A novel by F. Scott Fitzgerald",
    excerpt="I'm a writer and I'm a writer",
    synopsis="A novel by F. Scott Fitzgerald",
    toc="A novel by F. Scott Fitzgerald",
    editorial_reviews="A novel by F. Scott Fitzgerald",
  )

  assert book.id == 1
  assert book.title == "The Great Gatsby"
  assert book.slug == "the-great-gatsby"
  assert book.author.slug == "f-scott-fitzgerald"
  assert book.subjects[0].slug == "romance-books"
