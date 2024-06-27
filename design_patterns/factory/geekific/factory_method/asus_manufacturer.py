from company import Company
from gpu import Gpu
from asus_gpu import AsusGpu


class AsusManufacturer(Company):
    """Class, which implements the abstract factory method from the Company abstract class"""

    def create_gpu(self) -> Gpu:
        return AsusGpu()
