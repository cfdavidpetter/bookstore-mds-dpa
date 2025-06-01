from typing import List

from src.datalayer.repositories.sqlite.schema.book import Book as BookSchema
from src.domain.author import Author
from src.domain.book import Book
from src.utils.parsing import extract_float_from_string


class BookAdapter:
  @staticmethod
  def schema_to_domain(book_data: tuple) -> Book:
    return Book(
      id=book_data[0],
      title=book_data[1],
      slug=book_data[6],
      author=Author(
        id=book_data[3],
        title=book_data[2],
        slug=book_data[7],
        biography=book_data[4]
      ),
      authors=[],
      isbn13=int(book_data[8]),
      isbn10=book_data[9],
      price=extract_float_from_string(book_data[10]) if book_data[10] else None,
      format=book_data[11],
      publisher=book_data[12],
      pubdate=book_data[13],
      edition=book_data[14],
      subjects=[],
      lexile=book_data[16],
      pages=int(book_data[17]) if book_data[17] else None,
      dimensions=book_data[18],
      overview=book_data[19],
      excerpt=book_data[20],
      synopsis=book_data[21],
      toc=book_data[22],
      editorial_reviews=book_data[23]
    )
  

  @staticmethod
  def schema_list_to_domain_list(books_data: List[tuple]) -> List[Book]:
    return [BookAdapter.schema_to_domain(book_data) for book_data in books_data]
  

  @staticmethod
  def domain_to_schema(book: Book) -> BookSchema:
    if book.authors:
      authors = ', '.join([author.title for author in book.authors])
    else:
      authors = book.author.title

    return BookSchema(
      id=book.id,
      title=book.title,
      author=book.author.title,
      author_id=book.author.id,
      author_bio=book.author.biography,
      authors=authors,
      title_slug=book.slug,
      author_slug=book.author.slug,
      isbn13=book.isbn13,
      isbn10=book.isbn10,
      price=f"${book.price:.2f}" if book.price else None,
      format=book.format.value,
      publisher=book.publisher,
      pubdate=book.pubdate,
      edition=book.edition,
      subjects=', '.join([subject.title for subject in book.subjects]) if book.subjects else None,
      lexile=book.lexile,
      pages=book.pages,
      dimensions=book.dimensions,
      overview=book.overview,
      excerpt=book.excerpt,
      synopsis=book.synopsis,
      toc=book.toc,
      editorial_reviews=book.editorial_reviews
    )

