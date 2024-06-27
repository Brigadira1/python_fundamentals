from gpu import Gpu
from company import Company
from asus_manufacturer import AsusManufacturer
from msi_manufacturer import MSIManufacturer


class Main:

    def main(self) -> None:
        asus_manufacturer = AsusManufacturer()
        asus_gpu = asus_manufacturer.assemble_gpu()

        msi_manufacturer = MSIManufacturer()
        msi_gpu = msi_manufacturer.assemble_gpu()


if __name__ == "__main__":
    main = Main()
    main.main()
