import re
from typing import Union


def extract_float_from_string(value: str) -> Union[float, None]:
  match = re.search(r'[-+]?\d*\.\d+|\d+', value)
  if match:
    return float(match.group())
  return None