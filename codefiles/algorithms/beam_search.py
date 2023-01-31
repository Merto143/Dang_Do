from codefiles.algorithms.breadth_first import *
from operator import itemgetter
import random

class BeamSearch(BreadthFirst):
    def __init__(self, game, beam):
        super().__init__(game)
        self.beam = beam
        print("Begin")
        self.game.get_id()
        print("END")

    def run2(self):
        while not self.game.is_solved():
            self.scores_in_gen = []

            while (self.queue.list != []):
                self.move = self.queue.dequeue()

                self.game.grid = copy.copy(self.grid_memory[self.move[2]][0])
                self.game.set_car_coordinates()

                self.game.move_car(self.move[0], self.move[1])
                self.memories = list(zip(*self.grid_memory))[0]
                score = self.game.get_score()
                grid = copy.deepcopy(self.game.grid)
                state_score = [grid, score]
                self.scores_in_gen.append(state_score)
            random.shuffle(self.scores_in_gen)
            # sorted(self.scores_in_gen, key=itemgetter(1))

            if len(self.scores_in_gen) < self.beam:
                self.best_grids = list(zip(*self.scores_in_gen))[0]
            else:
                self.best_grids = list(zip(*self.scores_in_gen))[0][-self.beam:]

            for grid in self.best_grids:
                self.game.grid = copy.copy(grid)
                self.game.set_car_coordinates()
                self.memories = list(zip(*self.grid_memory))[0]

                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()

        print("game is solved")
        self.print_solution()


    def run(self):
        while not self.game.is_solved():
            random.shuffle(self.queue.list)
            self.chosen_states = []

            for move in self.queue.list[:self.beam]:
                self.chosen_states.append(move)

            self.queue = Queue()

            for state in self.chosen_states:
                self.game.grid = copy.copy(state[1])
                self.game.set_car_coordinates()
                self.move = state[0]
                self.game.move_car(self.move[0], self.move[1])

                self.node += 1

                self.create_children()
                print(self.cars)
                self.enque_movable_cars()
                print(self.game.grid)
                if self.game.is_solved():
                    print("game is solved")
                    self.print_solution()
                    break

    def enque_movable_cars(self):
        """Add the moveable cars and their possible directions to the queue. """
        for car in self.cars:
            for direction in car.get_legal_moves():
                new_move = [[car, direction, self.node, self.gen_new], copy.copy(self.game.grid)]
                self.queue.enqueue(new_move)
