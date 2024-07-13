from dataclasses import dataclass


@dataclass(frozen=True)
class Master:
    """A class that contains ultimate character properties. If you want to change
    something in here 'on fly', you have to kill yourself first"""
    hp: int | float = 1_000_000
    attack: int | float = 1_000_000
