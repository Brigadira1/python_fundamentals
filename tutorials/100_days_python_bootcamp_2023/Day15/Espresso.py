from dataclasses import dataclass


@dataclass(frozen=True)
class Espresso:
    water: int = 50
    coffee: int = 18
    milk: int = 0
    cost: float = 1.50
