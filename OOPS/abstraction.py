from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def accelerate(self):

        pass

    @abstractmethod
    def stop(self):

        pass

    
class Hunter(Bike):

    def start(self):

        print("Hunter Start Method")

    def accelerate(self):

        print("Hunter accelerate Method")

    def stop(self):

        print("Hunter Stop Method")


hunter_instance=Hunter()

hunter_instance.start()