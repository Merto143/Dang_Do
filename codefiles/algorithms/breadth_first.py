import copy
from codefiles.classes.queue import Queue
import numpy as np

class BreadthFirst:
    def __init__(self, game):
        self.game = game
        self.id_memory = []
        self.move_memory = []
        self.node = 0
        self.queue = Queue()
        self.solution = []
        self.gen_prev = 0
        self.gen_next = 1
        self.gen_new = 1

        # add the first state to the memory
        self.game.generate_moveability()
        self.id_memory.append([self.game.get_id(), "-"])

        # define the red car and
        self.carX = self.game.get_cars()[-1]

        # add the moveable cars to the queue
        self.cars = self.game.get_moveable_cars()
        self.enque_movable_cars()


    def run(self):
        """Run the breadth first algorithm on the given board. """

        while not self.game.is_solved():
            # deque and apply the next move
            self.move = self.queue.dequeue()
            self.game.id = self.id_memory[self.move[2]][0]
            self.game.get_board_with_id()

            self.game.move_car(self.move[0], self.move[1])

            # check if the state is already visited
            if self.state_not_in_memory():
                self.node += 1

                self.add_state_to_memory()
                self.create_children()
                self.enque_movable_cars()

        # print the solution when it's found
        self.print_solution()


    def state_not_in_memory(self):
        """Return True if the current grid is not yet visited. """
        # get a list of id's that are already visited
        self.memories = list(zip(*self.id_memory))[0]

        # check if the current grid id is already visited
        if not self.game.get_id() in self.memories:
            return True

        return False


    def print_solution(self):
        """Print the amount of states visited, the optimal solution and the
         amount of moves of this solution. """

        print("Game is solved.")
        print(f"In total we visited {self.node} different states")
        print("The optimal solution is:")

        for move in self.create_solution():
            print(move)

        print(f"It took {int(len(self.create_solution())/2)} moves to solve the puzzle")


    def create_children(self):
        """Get all moveable cars from a given state and update the generation if
        necessary. """
        self.game.generate_moveability()
        self.cars = self.game.get_moveable_cars()
        self.gen_next = self.move[-1]

        if self.gen_prev != self.gen_next:
            self.gen_prev = self.gen_next
            self.gen_new += 1


    def create_solution(self):
        """Go through the memory to get retrieve the moves that were made to
        get to the solution. """
        self.solution.insert(0, [self.id_memory[-1][1][0], self.id_memory[-1][1][1]])
        self.id_memory[-1][0]
        self.node = self.id_memory[-1][1][2]

        while self.node != 0:
                self.solution.insert(0, [self.id_memory[self.node][1][0], self.id_memory[self.node][1][1]])
                new_node = self.id_memory[self.node][1][2]
                self.node = new_node

        return self.solution


    def add_state_to_memory(self):
        """Add the current state to the memory. """
        self.move_memory.append(self.move)
        self.id_memory.append([self.game.get_id(), self.move])


    def enque_movable_cars(self):
        """Add the moveable cars and their possible directions to the queue. """
        for car in self.cars:
            for direction in car.get_legal_moves():
                new_move = [car, direction, self.node, self.gen_new]
                self.queue.enqueue(new_move)

    def get_solution(self):
        """Return the found solution of the problem. """
        return self.solution

    def get_visited_states(self):
        """Return the visited states. """
        return self.id_memory
