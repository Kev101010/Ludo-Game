class LudoGame:

    # Constructor Declaration of Class LudoGame
    def __init__(self):
       

    # Gets all players playing the game
    def get_players(self):
        

    # Gets player by their current position
    def get_player_by_position(self, position):
        
    # Moves player token
    def move_token(self, player, token, steps):
        
    # Moves a specific player to play the game
    def play_game(self, player, turns):
        # Checks whose player turn to move
        


class Player:

    # initial method or the constructor
    def __init__(self, position, start, end, stacked):
        

    # gets a position of a player
    def get_position(self):
        

    # Returns true if a move is successful completed
    def get_completed(self):
        
    def get_token_p_step_count(self):
        

    def get_token_q_step_count(self):
        

    # Gets the name of the current space
    def get_space_name(self, steps):

    @property
    def token_p(self):
        return self._token_p

    @property
    def token_q(self):
        return self._token_q


class Token:
    # initial method or the construction of the class Token
    def __init__(self, name):
        self._board = Board()
        self._player_name = name
        self._step_count = -1
        self._current_space = "R"

    # gets the number of next steps to go
    def get_step_count(self):
        return self._step_count

    # Moves a player to the next step
    def move(self, steps):
        self._step_count += steps
        if self._step_count > 57:
            self._step_count = 57 - (self._step_count - 57)

    @property
    def current_space(self):
        return self._current_space

    # counts and return number of steps
    @property
    def step_count(self):
        return self._step_count


# =============================== Skeleton Code ============================================

players = ['A','B']
turns = [('B', 6),('B', 4),('B', 5),('B', 4),('B', 4),('B', 3),('B', 4),('B', 5),('B', 4),('B', 4),('B', 5),('B', 4),('B', 1),('B', 4),('B', 5),('B', 5),('B', 5)]


# Object instantiation
game = LudoGame()
current_tokens_space = game.play_game(players, turns)

for pla in players:
    print(pla)
    player = game.get_player_by_position(str(pla))
    print(player.get_completed())
    print(player.get_token_p_step_count())
    print(current_tokens_space)
    print(player.get_space_name(55))