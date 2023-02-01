import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DF_heur(DepthFirst):

    def create_next_moves(self):
        moves = []
        for car in self.board.get_moveable_cars():
            for direction in car.get_legal_moves():
                self.board.move_car(car, direction)
                self.board.generate_moveability()
                score = self.board.number_of_cars_moveable()
                print(score)
                move = [car, direction, self.node, self.depth + 1, score]
                moves.append(move)


        moves.sort(key=lambda move: move[4])
        print(moves)

        for item in moves:
                self.stack.append(item)
