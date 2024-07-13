from dataclasses import dataclass


@dataclass(frozen=True)
class Animates:
    """Contains constants for creating animations. Have methods: pair_one(),
     pair_two(). If you want to change something in the fields, you have to
     kill yourself first."""
    fps1: int = 30
    fps2: int = 60
    fr_t1: float = 10/fps1
    fr_t2: float = 10/fps2

    def pair_one(self):
        """Returns a pair: fps-frame time for slow animation(30)"""
        return self.fps1, self.fr_t1

    def pair_two(self):
        """Returns a pair: fps-frame time for normal animation(60)"""
        return self.fps2, self.fr_t2
