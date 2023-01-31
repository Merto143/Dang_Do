import copy
import numpy as np

from codefiles.algorithms.depth_first import DepthFirst

class DepthFirst_depth(DepthFirst):
    
    def __init__(self, game):
        self.board = game
        self.board.generate_moveability()
        self.node = -1

        self.solution = []

        self.cars = self.board.get_moveable_cars()

        self.depth = 0
        self.visited = []
        self.nr_moves = 0
        self.stack = [[copy.deepcopy(self.board), "-"]]
        self.nodes = []
        self.best_solution = 0
