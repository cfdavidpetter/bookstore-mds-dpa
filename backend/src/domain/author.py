from typing import Optional

from src.domain.base import DomainBase


class Author(DomainBase):
  biography: Optional[str] = None
