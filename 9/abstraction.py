from abc import abstractmethod, ABC


class Transport(ABC):
    def __init__(self, ram_weight: float, wheel_weight: float):
        """
        Constructs Transport class
        :param ram_weight: The ram weight
        :param wheel_weight: Single wheel weight
        """
        self.ram_weight = ram_weight
        self.wheel_weight = wheel_weight

    @abstractmethod
    def calculate_weight(self):
        """
        Calculate weight of current transport
        :return: float
        """
        pass


class Bicycle(Transport):
    number_of_wheels = 2

    def calculate_weight(self):
        return self.ram_weight + Bicycle.number_of_wheels * self.wheel_weight


class MotoTransport(Transport, ABC):
    def __init__(self, ram_weight: float, wheel_weight: float, engine_weight: float):
        """
        Constructs Transport class
        :param ram_weight: The ram weight
        :param wheel_weight: Single wheel weight
        :param engine_weight: The engine weight
        """
        super().__init__(ram_weight, wheel_weight)
        self.engine_weight = engine_weight


class MotoBike(MotoTransport):
    number_of_wheels = 2

    def calculate_weight(self):
        return self.ram_weight + MotoBike.number_of_wheels * self.wheel_weight + self.engine_weight


class Car(MotoTransport):
    number_of_wheels = 4

    def __init__(self, ram_weight: float, wheel_weight: float, engine_weight: float, cabin_weight: float):
        """
        The Car constructor

        :param ram_weight:
        :param wheel_weight:
        :param engine_weight:
        :param cabin_weight:
        """
        super().__init__(ram_weight, wheel_weight, engine_weight)
        self.cabin_weight = cabin_weight

    def calculate_weight(self):
        return self.ram_weight + Car.number_of_wheels * self.wheel_weight + self.engine_weight + self.cabin_weight


def utilisation(ts: Transport):
    print(ts.calculate_weight())
    print("It's destroyed")

transport_list = []
bicycle = Bicycle(10, 5)
transport_list.append(bicycle)
moto = MotoBike(20, 10, 25)
transport_list.append(moto)
car = Car(200, 20, 500, 400)
transport_list.append(car)
for transport in transport_list:
    print(transport.calculate_weight())
    utilisation(transport)

