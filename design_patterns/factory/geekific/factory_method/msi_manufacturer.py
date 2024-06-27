from company import Company
from msi_gpu import MSIGpu
from design_patterns.factory.geekific.factory_method.gpu import Gpu


class MSIManufacturer(Company):
    """A class, which implements the abstract factory method from Company abstract class"""

    def create_gpu(self) -> Gpu:
        return MSIGpu()
