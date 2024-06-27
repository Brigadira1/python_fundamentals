import random
import string

from datetime import datetime as dt
from enum import Enum, auto
from dataclasses import dataclass, field


def generate_vehicle_license() -> str:
    """Helper function for generating vehicle license number."""

    digits_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))

    return f"{letter_part_1}-{digits_part}-{letter_part_2}"


def default_accessories():
    return [Accessory.AIRCO, Accessory.NAVIGATION]


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str = field(default_factory=generate_vehicle_license, init=False)
    accessories: list[Accessory] = field(default_factory=default_accessories)
    fuel_type: FuelType = FuelType.ELECTRIC

    def reserve(self, date: dt):
        """Reserve a vehicle for a certain date"""

        print(f"Vehicle is reserved for {date}")


def main() -> None:
    """Create some vehicles and print their details"""

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL,
        ],
    )

    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
    )

    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        fuel_type=FuelType.DIESEL,
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL],
    )

    print(tesla)
    print(volkswagen)
    print(bmw)

    bmw.reserve(dt.now())


if __name__ == "__main__":
    main()
