class Car:

    def __init__(self, name: str, orientation: str, col: int, row: int, length: int):
        self.name = name
        self.orientation = orientation
        self.coordinates = [row, col]
        self.length = length


    def __repr__(self):
        return self.name


    def get_position(self):
        return self.coordinates


    # def is_moveable(self):
    #     if self.orientation == "V":
    #         if condition:
    #             return True
    #         else:
    #             return False
    #     elif self.orientation == "H":
    #         if condition:
    #             return True
    #         else:
    #             return False
