import copy

class DepthFirst:
    def __init__(self, game):
        self.board = copy.deepcopy(game)
        self.board.generate_moveability()

        self.states = [copy.deepcopy(self.board)]

        # self.grid_memory = []
        self.move_memory = []


    def get_next_state(self):
        return self.states.pop()


    def build_children(self, game):
        options = game.get_all_moves()

        for option in options:
            new_state = copy.deepcopy(board)
            

    def run(self):
        while self.states:
            new_state = self.get_next_state()
