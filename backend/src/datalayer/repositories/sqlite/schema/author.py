from src.datalayer.repositories.sqlite.schema.base import SchemaBase


class Author(SchemaBase):
  id: int
  title: str
  slug: str
  biography: str
