import keyword
from collections import namedtuple
import re
from string import digits
from typing import Any


def dict_to_namedtuple(
    dic: dict, name: str = "data", startwith: str = "aa_"
) -> namedtuple:
    dicn = {}
    for key, item in dic.items():
        dicn[create_valid_identifier(key, startwith)] = item
    return namedtuple(name, dicn.keys())(**dicn)


def create_valid_identifier(variable: Any, startwith: str = "aa_") -> str:
    v = re.sub(r"[^0-9a-zA-Z_]+", "_", str(variable))
    v = v.strip("_")
    if v[0] in digits:
        v = startwith + v
    if keyword.iskeyword(v):
        v = startwith + v
    return v


