# write a pythone code to create two classes bmw and ferrari  with similar methodes and imbliment polymorhisim on them
# Parent class (optional but good for beginners)
class Car:
    def start_engine(self):
        pass
class BMW(Car):
    def start_engine(self):
        print("BMW engine started with a smooth purr.")

class Ferrari(Car):
    def start_engine(self):
        print("Ferrari engine started with a loud roar!")

def test_drive(car):
    car.start_engine()

bmw_car = BMW()
ferrari_car = Ferrari()

test_drive(bmw_car)
test_drive(ferrari_car)
