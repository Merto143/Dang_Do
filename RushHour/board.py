from car import Car

#comment
class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.cars = []
        self.grid = []
        self.load_cars(f"gameboards/{filename}.csv")


    def load_cars(self, file):
        with open(file) as f:

            line = f.readline()
            line = f.readline()

            while line != "":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()
