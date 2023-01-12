from car import Car

#comment
class Board:

    def __init__(self, dim: int, filename: str) -> None:
        self.dim = dim
        self.cars = []
        self.grid = np.full((dim, dim), "O")
        self.load_cars(f"gameboards/{filename}.csv")
        self.add_cars_to_grid()
        self.cars[0].get_car_spaces()


    def load_cars(self, file):
        with open(file) as f:

            line = f.readline()
            line = f.readline()

            while line != "":
                line = line.split(",")
                car = Car(line[0], line[1], line[2], line[3], line[4])
                self.cars.append(car)

                line = f.readline()

    def add_cars_to_grid(self):
        for car in self.cars:
            spaces = car.get_car_spaces()

            for i in range(car.length):
                space = spaces[i]
                self.grid[space[0] - 1][space[1] - 1] = car.name

        print(self.grid)
