from enum import Enum
from src.domain.base import DomainBase
from src.domain.author import Author
from src.domain.subject import Subject

class BookFormat(str, Enum):
  PAPERBACK = "Paperback"
  HARDCOVER = "Hardcover"
  LIBRARY_BINDING = "Library Binding"
  COMPACT_DISC = "Compact Disc"
  MASS_MARKET_PAPERBACK = "Mass Market Paperback"
  OTHER_FORMAT = "Other Format"
  MULTIMEDIA = "Multimedia"

class Book(DomainBase):
  author: Author
  authors: list[Author]
  isbn13: int
  isbn10: str
  price: float
  format: BookFormat
  publisher: str
  pubdate: str
  edition: str
  subjects: list[Subject]
  lexile: str
  pages: int
  dimensions: str
  overview: str
  excerpt: str
  synopsis: str
  toc: str
  editorial_reviews: str
