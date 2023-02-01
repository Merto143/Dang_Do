from codefiles.algorithms.algorithms import random_only_legal_moves_memory_algorithm
from codefiles.algorithms.breadth_first import *
from codefiles.classes.board import Board


class BreadthFirstRandomStates(BreadthFirst):
    def __init__(self, game, random_repeats):
            super().__init__(game)
            self.reps = random_repeats

            # first run random
            self.run_random()

            # reset the board after running random
            self.game = Board(self.game.dim, self.game.filename)

            self.game.generate_moveability()
            self.cars = self.game.get_moveable_cars()
            self.enque_movable_cars()

    def run(self):
        """Run the breadth first random states algorithm on the given board. """

        while not self.game.is_solved():
            # deque and apply the next move
            self.move = self.queue.dequeue()
            self.game.id = self.id_memory[self.move[2]][0]
            self.game.get_board_with_id()

            self.game.move_car(self.move[0], self.move[1])

            # check if we find a solution that is not in the random memory
            if self.game.is_solved():
                self.add_state_to_memory()
                self.node += 1

            # check if the state is not yet visited and in the random memory
            if self.state_not_in_memory() and self.state_in_random_memory():
                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()

        # print the solution when its found
        self.print_solution()


    def run_random(self):
        """Run the random algorithm self.reps amount of times. """
        self.random_memory = random_only_legal_moves_memory_algorithm(self.game, self.reps)

    def state_in_random_memory(self):
        """Check if the current state is in the random memory. """

        id = self.game.get_id()
        if id in self.random_memory:
            return True

        return False
