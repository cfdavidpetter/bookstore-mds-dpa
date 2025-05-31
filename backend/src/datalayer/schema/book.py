from src.datalayer.schema.base import SchemaBase


class Book(SchemaBase):
  id: int
  title: str
  author: str
  author_id: int
  author_bio: str
  authors: str
  title_slug: str
  author_slug: str
  isbn13: int
  isbn10: str
  price: float
  format: str
  publisher: str
  pubdate: str
  edition: str
  subjects: str
  lexile: str
  pages: int
  dimensions: str
  overview: str
  excerpt: str
  synopsis: str
  toc: str
  editorial_reviews: list[str]

class BookSubjects(SchemaBase):
  id: int
  book: int
  sub_subject: int
  sub_sub_subject: int
