from abc import ABC, abstractmethod


class Gpu(ABC):
    """Interface for different Gpu brands"""

    @abstractmethod
    def assemble(self):
        """Abstract method for assembling a video card"""
