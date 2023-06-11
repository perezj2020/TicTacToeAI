import math
import random

class player:
    def __init__(self,letter):
    #letter is x or o
        self.letter=letter

    #next move
    def getmove(self,game):
        pass

class NPC(player):
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        if len(game.availablemoves()) == 9:
            square = random.choice(game.availablemoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.currentwin == other_player:
            return {'position': None,
                    'score': 1 * (state.emptysquaresspaces() + 1) if other_player == max_player else -1 * (
                            state.emptysquaresspaces() + 1)}
        elif not state.emptysquares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.availablemoves():
            state.makemove(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.currentwin = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

class HumanPlayer(player):
    def _init_ (self,letter):
        super().__init__(letter)

    def getmove(self, game):
        validsquare= False
        value = None
        while not validsquare:
            square = input(self.letter + '\'s turn. input 0-8:')
            #correct value test
            try:
                value = int(square)
                if value not in game.availablemoves():
                    raise ValueError
                validsquare=True
            except ValueError:
                print('Try again. Not valid square')
        return value

