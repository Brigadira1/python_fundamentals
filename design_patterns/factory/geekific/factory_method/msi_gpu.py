from gpu import Gpu


class MSIGpu(Gpu):
    """This is a concrete MSI Gpu"""

    def assemble(self):
        print("Assembling the MSI Gpu...")
