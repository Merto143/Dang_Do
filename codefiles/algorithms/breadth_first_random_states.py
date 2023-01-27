from codefiles.algorithms.algorithms import random_only_legal_moves_algorithm
from codefiles.algorithms.breadth_first import *
from codefiles.classes.board import Board


class BreadthFirstRandomStates(BreadthFirst):

    def run(self):
        self.run_random()
        game = Board(self.game.dim, self.game.filename)

        while (self.queue.list != []):
            self.move = self.queue.dequeue()
            self.game.grid = copy.deepcopy(self.grid_memory[self.move[-1]][0])
            self.game.set_car_coordinates()

            self.game.move_car(self.move[0], self.move[1])
            self.memories = list(zip(*self.grid_memory))[0]

            if (not any(np.array_equal(self.game.grid, item) for item in self.memories)) and any(np.array_equal(self.game.grid, item) for item in self.random_memory):
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

    def run_random(self):
        self.random_memory = random_only_legal_moves_algorithm(self.game)
