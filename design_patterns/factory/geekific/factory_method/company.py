from abc import ABC, abstractmethod
from gpu import Gpu


class Company(ABC):
    """This is a class that will provide the abstract factory method. Concrete implementations
    of this class will implement it.
    """

    @abstractmethod
    def create_gpu(self) -> Gpu:
        """Should be implemented by the concrete classes that will inherit from Company abstract class"""

    def assemble_gpu(self) -> Gpu:
        gpu = self.create_gpu()
        gpu.assemble()
        return gpu
