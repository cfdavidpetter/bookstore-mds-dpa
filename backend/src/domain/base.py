from slugify import slugify
from typing import Optional
from pydantic import BaseModel, model_validator

class DomainBase(BaseModel):
  id: int
  title: str
  slug: Optional[str] = None

  @model_validator(mode="before")
  @classmethod
  def generate_slug_if_missing(cls, values: dict):
    if not values.get("slug"):
      values["slug"] = slugify(values.get("title", ""))
    return values