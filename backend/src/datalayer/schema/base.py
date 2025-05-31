from pydantic import BaseModel


class SchemaBase(BaseModel):
  id: int
