from dataclasses import dataclass


@dataclass(frozen=True)
class Capuccinno:
    water: int = 250
    milk: int = 100
    coffee: int = 24
    cost: float = 3.00
