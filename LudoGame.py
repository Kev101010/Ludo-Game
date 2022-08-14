class LudoGame:

    # Constructor Declaration of Class LudoGame
    def __init__(self):
        self._players = []
        self._board = Board()

    # Gets all players playing the game
    def get_players(self):
        return self._players

    # Gets player by their current position
    def get_player_by_position(self, position):
        for player in self._players:
            if player.get_position() == position:
                return player
    # Moves player token
    def move_token(self, player, token, steps):
        if token == 'p':
            player.token_p.move(steps)
        elif token == 'q':
            player.token_q.move(steps)

    # Moves a specific player to play the game
    def play_game(self, player, turns):
        # Checks whose player turn to move
        for position in player:
            if position == "A":
                self._players.append(Player('A', 1, 50))
            elif position == "B":
                self._players.append(Player('B', 15, 8))
            elif position == "C":
                self._players.append(Player('C', 29, 22))
            elif position == "D":
                self._players.append(Player('D', 43, 36))
        for roll in turns:
            player_temp = self.get_player_by_position(roll[0])
            steps = roll[1]
            if roll[1] == 6:
                if player_temp.token_p._step_count == -1:
                    self.move_token(player_temp, 'p', 1)
                elif player_temp.token_q._step_count == -1:
                    self.move_token(player_temp, 'q', 1)
                else:
                    if player_temp.token_p._step_count > player_temp.token_q.step_count:
                        self.move_token(player_temp, 'q', 6)
                    else:
                        self.move_token(player_temp, 'p', 6)
            else:
                if player_temp.token_p._step_count >= 0 and player_temp.token_q.step_count >= 0:
                    if player_temp.token_p._step_count > player_temp.token_q.step_count:
                        self.move_token(player_temp, 'q', roll[1])
                    else:
                        self.move_token(player_temp, 'p', roll[1])
                elif player_temp.token_p._step_count >= 0:
                    self.move_token(player_temp, 'p', roll[1])
                elif player_temp.token_q._step_count >= 0:
                    self.move_token(player_temp, 'q', roll[1])

        temp_array = []
        
        for player_grid in self._players:
            temp_array.append(player_grid.get_space_name(player_grid.token_p._step_count))
            temp_array.append(player_grid.get_space_name(player_grid.token_q._step_count))
        
        return temp_array
        #return ["'{0}','{1}'".format(player.get_space_name(player.token_p._step_count), player.get_space_name(player.token_q._step_count)) for player in self._players]


class Player:

    # initial method or the constructor
    def __init__(self, position, start, end, stacked):
        self._board = Board()
        self.start = start
        self.end = end
        self._position = position
        self._stacked = stacked 
        self._token_p = Token('p')
        self._token_q = Token('q')

    # gets a position of a player
    def get_position(self):
        return self._position

    # Returns true if a move is successful completed
    def get_completed(self):
        if self._token_p.current_space == "E" and self._token_q.current_space == "E":
            return True
        else:
            return False

    def get_token_p_step_count(self):
        return self._token_p.step_count

    def get_token_q_step_count(self):
        return self._token_q.step_count

    # Gets the name of the current space
    def get_space_name(self, steps):
        print(steps)
        if steps == -1:
            return "H"
        elif steps == 0:
            return "R"
        elif steps > 50 and steps < 57:
            return "{0}{1}".format(self._position, steps - 50)
        elif steps == 57:
            return "E"
        else:
            return str(self.start + steps - 1)

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

# Create a class Board
# Creates all the spaces of a board
class Board:
    # Constructor Declaration
    def __init__(self):
        #initiate all the spaces of a board
        self._spaces = ["A1", "A2", "A3", "A4", "A5", "A6",
                        "B1", "B2", "B3", "B4", "B5", "B6",
                        "C1", "C2", "C3", "C4", "C5", "C6",
                        "D1", "D2", "D3", "D4", "D5", "D6",
                        "E1", "E2", "E3", "E4", "E5", "E6",
                        "F1", "F2", "F3", "F4", "F5", "F6",
                        "G1", "G2", "G3", "G4", "G5", "G6",
                        "H1", "H2", "H3", "H4", "H5", "H6",
                        "I1", "I2", "I3", "I4", "I5", "I6",
                        "K1", "K2", "K3", "K4", "K5", "K6"]

    @property
    def spaces(self):
        return self._spaces


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