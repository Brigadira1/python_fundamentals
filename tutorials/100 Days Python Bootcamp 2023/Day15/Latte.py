from dataclasses import dataclass


@dataclass(frozen=True)
class Latte:
    water: int = 200
    milk: int = 150
    coffee: int = 24
    cost: float = 2.50
