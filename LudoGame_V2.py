class LudoGame:

    # Constructor Declaration of Class LudoGame
    def __init__(self):
       self.__players = []

    # Gets all players playing the game
    def get_players(self):
        

    # Gets player by their current position
    def get_player_by_position(self, position):
        for player in self.__players:
            #Try using property to set the getter for player
            if player == position:
                return player 

    # Moves player token
    def move_token(self, player, token, steps):
        
    # Moves a specific player to play the game
    def play_game(self, player, turns):
        for gamer in player:
            if gamer >= "A" and gamer <= "D":
                self.__players.append(Player(gamer))
            else:
                raise ValueError("Please input a letter A to D")
        for roll in turns:
            gamer_temp = self.get_player_by_position(roll[0])
            steps = roll[1]
        # Checks whose player turn to move
    

class Player:

    # initial method or the constructor
    def __init__(self, position):
        self.__position = position
        self.__stacked = False
        self.__token_p = Token('p')
        self.__token_q = Token('q')

        #see if conditional works in __init__
        if self.__position == 'A':
            self.__start = 1 
            self.__end = 50
        elif self.__position == 'B':
            self.__start = 15
            self.__end = 8
        elif self.__position == 'C':
            self.__start = 29
            self.__end = 22
        elif self.__position == 'D':
            self.__start = 43
            self.__end = 36

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
        self._player_name = name
        self._step_count = -1

    # gets the number of next steps to go
    def get_step_count(self):
        return self._step_count

    # Moves a player to the next step
    def move(self, steps):

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