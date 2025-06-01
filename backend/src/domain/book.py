from enum import Enum
from typing import Optional

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
  authors: Optional[list[Author]] = None
  isbn13: int
  isbn10: str
  price: Optional[float] = None
  format: BookFormat
  publisher: str
  pubdate: str
  edition: Optional[str] = None
  subjects: Optional[list[Subject]] = None
  lexile: Optional[str] = None
  pages: Optional[int] = None
  dimensions: Optional[str] = None
  overview: Optional[str] = None
  excerpt: Optional[str] = None
  synopsis: Optional[str] = None
  toc: Optional[str] = None
  editorial_reviews: Optional[str] = None
