import re
from typing import Union


def extract_float_from_string(value: str) -> Union[float, None]:
  match = re.search(r'[-+]?\d*\.\d+|\d+', value)
  if match:
    return float(match.group())
  return None

def extract_dict_filters_from_string(value: str) -> Union[dict, None]:
  '''
  column:value;column:value,column.column.column:value;...
  column.column.column:value -> book: { author: { name: value } }
  '''
  if not value:
    return None
  
  def add_filter(filters: dict, column_parts: list, value: str):
    if len(column_parts) == 1:
      filters[column_parts[0]] = value
    else:
      if column_parts[0] not in filters:
        filters[column_parts[0]] = {}
      add_filter(filters[column_parts[0]], column_parts[1:], value) 
  
  filters = {}
  for filter in value.split(';'):
    column, value = filter.split(':')
    if '.' in column:
      column_parts = column.split('.')
      # book.author.name:value -> book: { author: { name: value } }
      add_filter(filters, column_parts, value)
    else:
      filters[column] = value
    
  return filters