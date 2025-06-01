import math

from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, model_validator


T = TypeVar('T')

DEFAULT_PAGE_SIZE = 15
DEFAULT_PAGE = 1


class PaginatedResponse(BaseModel, Generic[T]):
  data: List[T]
  total: int
  per_page: int
  from_index: int
  current_page: int
  next_page: Optional[int]
  previous_page: Optional[int]
  last_page: Optional[int]

  @model_validator(mode="before")
  @classmethod
  def add_pagination_info(cls, values: dict):
    page = values.get("current_page")
    page_size = values.get("per_page")
    total_count = values.get("total")

    if not values.get("next_page"):
      values["next_page"] = page + 1 if page < math.ceil(total_count / page_size) else None

    if not values.get("previous_page"):
      values["previous_page"] = page - 1 if page > 1 else None

    if not values.get("last_page"):
      values["last_page"] = math.ceil(total_count / page_size)

    return values
