import copy
from codefiles.classes.queue import Queue
import numpy as np

class BreadthFirst:
    def __init__(self, game):
        self.game = game
        self.grid_memory = []
        self.move_memory = []
        self.node = 0
        self.queue = Queue()
        self.solution = []

        self.game.generate_moveability()

        self.grid = copy.deepcopy(self.game.grid)
        self.grid_memory.append([self.grid, "-"])

        self.carX = self.game.get_cars()[-1]
        self.cars = self.game.get_moveable_cars()
        self.enque_movable_cars()

    def run(self):
        while (self.queue.list != []):
            self.move = self.queue.dequeue()
            self.game.grid = copy.deepcopy(self.grid_memory[self.move[-1]][0])
            self.game.set_car_coordinates()

            self.game.move_car(self.move[0], self.move[1])
            self.memories = list(zip(*self.grid_memory))[0]

            if not any(np.array_equal(self.game.grid, item) for item in self.memories):
                self.add_state_to_memory()
                self.node += 1

                self.game.generate_moveability()
                self.cars = self.game.get_moveable_cars()

                self.enque_movable_cars()

            if self.game.is_solved():
                print("game is solved")
                break
        print(f"In total we visited {self.node} different states")
        print("The optimal solution is:")
        for move in self.create_solution():
            print(move)
        print(len(self.create_solution()))

    def create_solution(self):
        self.solution.insert(0, [self.grid_memory[-1][1][0], self.grid_memory[-1][1][1]])
        self.grid_memory[-1][0]
        self.node = self.grid_memory[-1][1][2]

        while self.node != 0:
                self.solution.insert(0, [self.grid_memory[self.node][1][0], self.grid_memory[self.node][1][1]])
                new_node = self.grid_memory[self.node][1][2]
                self.node = new_node

        return self.solution

    def add_state_to_memory(self):
        self.move_memory.append(self.move)
        self.grid_memory.append([copy.deepcopy(self.game.grid), self.move])

    def enque_movable_cars(self):
        for car in self.cars:
            for direction in car.get_legal_moves():
                new_move = [car, direction, self.node]
                self.queue.enqueue(new_move)
