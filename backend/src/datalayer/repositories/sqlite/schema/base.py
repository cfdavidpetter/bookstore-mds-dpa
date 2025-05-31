from typing import Optional

from pydantic import BaseModel


class SchemaBase(BaseModel):
  id: Optional[int] = None
