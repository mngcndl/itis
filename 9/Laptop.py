class Laptop:
    def __init__(self, given_name: str, cpu_cores: int, core_power: float):
        """
        Constructor for Laptop class. Inits class properties

        :param given_name: The Laptop brand name
        :param cpu_cores: Number of CPU cores
        :param core_power: Each CPU power in GHz
        """
        self.name = given_name
        self.cpu_cores = cpu_cores
        self.core_power = core_power

    def total_cpu_power(self):
        """
        Calculates total CPU power by multiplication of core power and number of CPUs.
        Lalala. Lalala. Lalala. Lalala. Lalala
        :return: float: Total CPU power
        """
        self.__log("Total CPU power calculating")
        return self.core_power * self.cpu_cores

    def __log(self, value):
        print(value)


my_laptop = Laptop("Apple", 3, 2.7)
print(my_laptop.name)
