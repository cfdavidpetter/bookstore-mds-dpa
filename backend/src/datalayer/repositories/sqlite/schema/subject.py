from src.datalayer.repositories.sqlite.schema.base import SchemaBase


class Subject(SchemaBase):
  id: int
  title: str
  slug: str
