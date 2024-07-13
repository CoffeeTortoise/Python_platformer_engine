from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Constant:
    """A class that can be used for storing variables as a constants"""
    val: Any = None
