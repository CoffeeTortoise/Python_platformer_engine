from dataclasses import dataclass


@dataclass(frozen=True)
class GreenShades:
    """A class that contains basic shades of green as tuples. There is a data class.
        If you want to change something in the fields, you have to kill yourself first."""
    green: tuple[int, int, int] = (0, 255, 0)
    harlequin: tuple[int, int, int] = (68, 148, 74)
    turquoise: tuple[int, int, int] = (48, 186, 143)
    verdict: tuple[int, int, int] = (52, 201, 36)
    michigan: tuple[int, int, int] = (0, 102, 51)
    malachite: tuple[int, int, int] = (11, 218, 81)
    jade: tuple[int, int, int] = (0, 168, 107)
    emerald: tuple[int, int, int] = (80, 200, 120)
