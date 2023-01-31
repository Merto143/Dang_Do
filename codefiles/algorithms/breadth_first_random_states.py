from codefiles.algorithms.algorithms import random_only_legal_moves_memory_algorithm
from codefiles.algorithms.breadth_first import *
from codefiles.classes.board import Board


class BreadthFirstRandomStates(BreadthFirst):

    def run(self):
        self.run_random()

        self.game = Board(self.game.dim, self.game.filename)

        self.game.generate_moveability()
        self.cars = self.game.get_moveable_cars()
        self.enque_movable_cars()

        while not self.game.is_solved():
            self.move = self.queue.dequeue()
            self.game.grid = copy.deepcopy(self.grid_memory[self.move[2]][0])
            self.game.set_car_coordinates()

            self.game.move_car(self.move[0], self.move[1])

            if self.game.is_solved():
                self.add_state_to_memory()
                self.node += 1

            if self.state_not_in_memory() and self.state_in_random_memory():
                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()

        self.print_solution()


    def run_random(self):
        self.random_memory = random_only_legal_moves_memory_algorithm(self.game)

    def state_in_random_memory(self):
        id = self.game.get_id()
        if id in self.random_memory:
            return True

        return False

    def get_solution(self):
        return self.solution

    def get_visited_states(self):
        return self.grid_memory
