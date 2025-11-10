from abc import ABC,abstractmethod
class vehicle():
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
    def fuel_status(self):
        print('fuel level is good')
class Car(vehicle):
    def start_engine(self):
        print('car engine is started')
    def stop_engine(self):
        print('car engine is stoped')
class Bike(vehicle):
    def start_engine(self):
        print('bike engine is started')
    def stop_engine(self):
        print('bike engine is stopped')
car=Car()
bike=Bike()

car.start_engine()
car.stop_engine()
car.fuel_status()

bike.start_engine()
bike.fuel_status()
bike.stop_engine()

