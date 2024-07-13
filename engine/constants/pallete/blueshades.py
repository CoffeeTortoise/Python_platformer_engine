from dataclasses import dataclass


@dataclass(frozen=True)
class BlueShades:
    """A class that contains basic shades of blue as tuples. There is a data class.
        If you want to change something in the fields, you have to kill yourself first."""
    blue: tuple[int, int, int] = (0, 0, 255)
    cyan: tuple[int, int, int] = (66, 170, 255)
    aspid: tuple[int, int, int] = (106, 90, 205)
    berlin: tuple[int, int, int] = (0, 49, 83)
    diamond: tuple[int, int, int] = (62, 95, 138)
    cornflower: tuple[int, int, int] = (100, 149, 237)
    cobalt: tuple[int, int, int] = (0, 71, 171)
    frosty: tuple[int, int, int] = (0, 191, 255)
    sapphire: tuple[int, int, int] = (8, 37, 103)
    aqua: tuple[int, int, int] = (0, 140, 240)
