from codefiles.algorithms.breadth_first import *
from operator import itemgetter
import random
import copy

class BeamSearch(BreadthFirst):
    def __init__(self, game, beam):
        super().__init__(game)
        self.beam = beam
        self.solution_found = False
        print(self.game.grid)
        print(self.game.object_function())


    def run2(self):
        while not self.game.is_solved():
            self.scores_in_gen = []

            while self.queue.list != []:
                print("Hoi")
                self.move = self.queue.dequeue()
                self.game.id = self.id_memory[self.move[2]][0]
                self.game.get_board_with_id()

                self.game.move_car(self.move[0], self.move[1])

                score = self.game.object_function()
                id = self.game.get_id()
                id_score = [id, score]
                self.scores_in_gen.append(id_score)

            self.highest_scores = self.get_highest_scores()
            self.choose_scores()

            for id in self.chosen_ids:
                self.game.id = id
                self.game.get_board_with_id()

                self.add_state_to_memory()
                self.node += 1

                self.create_children()
                self.enque_movable_cars()


        print("game is solved")
        # self.print_solution()

    #
    # def run(self):
    #     while not self.game.is_solved():
    #         random.shuffle(self.queue.list)
    #         self.chosen_states = []
    #
    #         for move in self.queue.list[:self.beam]:
    #             self.chosen_states.append(move)
    #
    #         self.queue = Queue()
    #
    #         for state in self.chosen_states:
    #             self.game.grid = copy.copy(state[1])
    #             self.game.set_car_coordinates()
    #             self.move = state[0]
    #             self.game.move_car(self.move[0], self.move[1])
    #
    #             self.node += 1
    #
    #             self.create_children()
    #             print(self.cars)
    #             self.enque_movable_cars()
    #             print(self.game.grid)
    #             if self.game.is_solved():
    #                 print("game is solved")
    #                 self.print_solution()
    #                 break

    # def enque_movable_cars(self):
    #     """Add the moveable cars and their possible directions to the queue. """
    #     for car in self.cars:
    #         for direction in car.get_legal_moves():
    #             new_move = [[car, direction, self.node, self.gen_new], copy.copy(self.game.grid)]
    #             self.queue.enqueue(new_move)

    def get_visited_states(self):
        return self.node

    def get_solution(self):
        return self.solution


    def choose_scores(self):
        if len(self.highest_scores) <= self.beam:
            self.chosen_ids = list(zip(*self.highest_scores))[0]
        else:
            random.shuffle(self.highest_scores)
            print(list(zip(*self.highest_scores))[1])
            self.chosen_ids = list(zip(*self.highest_scores))[0][self.beam:]

    def get_highest_scores(self):
        highest_scores = []
        sorted(self.scores_in_gen, key=itemgetter(1))
        self.scores_in_gen.reverse()

        if len(self.scores_in_gen) >= self.beam:
            for item in range(self.beam):
                highest_scores.append(self.scores_in_gen[item])

            if not item == len(self.scores_in_gen) - 1:
                while self.scores_in_gen[item + 1][1] == self.scores_in_gen[item][1]:
                    highest_scores.append(self.scores_in_gen[item + 1])
                    item += 1

                    if item == len(self.scores_in_gen) - 1:
                        break
        else:
            highest_scores = copy.copy(self.scores_in_gen)
        return highest_scores
