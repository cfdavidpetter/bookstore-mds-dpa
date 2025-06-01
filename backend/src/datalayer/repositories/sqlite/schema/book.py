from typing import Optional

from src.datalayer.repositories.sqlite.schema.base import SchemaBase


class Book(SchemaBase):
  id: int
  title: str
  author: Optional[str] = None
  author_id: Optional[int] = None
  author_bio: Optional[str] = None
  authors: Optional[str] = None
  title_slug: str
  author_slug: Optional[str] = None
  isbn13: int
  isbn10: str
  price: Optional[str] = None
  format: str
  publisher: str
  pubdate: str
  edition: Optional[str] = None
  subjects: Optional[str] = None
  lexile: Optional[str] = None
  pages: Optional[int] = None
  dimensions: Optional[str] = None
  overview: Optional[str] = None
  excerpt: Optional[str] = None
  synopsis: Optional[str] = None
  toc: Optional[str] = None
  editorial_reviews: Optional[str] = None

class BookSubjects(SchemaBase):
  id: int
  book: int
  sub_subject: int
  sub_sub_subject: int
