class LudoGame:

    # Constructor Declaration of Class LudoGame
    def __init__(self):
       self.__players = []

    # Gets all players playing the game
    def get_players(self):
        return self.__players

    # Gets player by their current position
    def get_player_by_position(self, position):
        if not position >= "A" and not position <= "D":
            raise ValueError("Player not found!")
        
        for player in self.__players:
            #Try using property to set the getter for player (Nevermind criteria needs get position)
            if player.get_position() == position:
                return player 

    # Moves player token
    def move_token(self, player, token, steps):
        #use method to move tokens from player class
        temp_player = self.get_player_by_position(player)
        if token == 'p':
            temp_player.token_p.move(steps)
        else:
            temp_player.token_q.move(steps)
    

    #Return true if a token is still in base:
    def token_in_home(self, player):
        temp_player = self.get_player_by_position(player)
        if temp_player.get_token_p_step_count() == -1 or temp_player.get_token_q_step_count() == -1:
            return True

    #Returns token in homebase 
    def home_base(self, player):
        temp_player = self.get_player_by_position(player)
        if temp_player.get_token_p_step_count() == -1 and temp_player.get_token_q_step_count() == -1:
            return 'p'
        elif temp_player.get_token_p_step_count() == -1:
            return 'p'
        else:
            return 'q'

    def farther_token(self, player):
        temp_player = self.get_player_by_position(player)
        if temp_player.get_token_p_step_count < temp_player.get_token_q_step_count():
            return 'p'
        else:
            return 'q'

    #Helper function to return farthest in play token outside of base
    def farther_inplay_token(self, player):
        if self.token_in_home(player):
            if self.home_base(player) == 'q':
                return 'p'
            else:
                return 'q'
        else:
            return self.farther_token(player)

    #Returns token based on move priority 
    def move_priority(self, player, roll):
        if roll == 6:
            if self.token_in_home(player):
                self.move_token(player, self.home_base(player), 1)
            #remember to implement reroll feature later 
            else:
                self.move_token(player, self.farther_token(player), 6)
        else:
            self.move_token(player, self.farther_inplay_token(player), roll)
    
    # Moves a specific player to play the game
    def play_game(self, player, turns):
        for gamer in player:
            if gamer >= "A" and gamer <= "D":
                self.__players.append(Player(gamer))
            else:
                raise ValueError("Please input a letter A to D")
        for roll in turns:
            self.move_priority(roll[0],roll[1])
        # Checks whose player turn to move
        board_state = []
        for user in self.__players: 
            board_state.append(user.get_space_name(user.get_token_p_step_count()))
            board_state.append(user.get_space_name(user.get_token_q_step_count()))
        
        return board_state

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
        print("Getting position")
        return self.__position

    # Returns true if player has completed the game
    def get_completed(self):
        if self.get_token_p_step_count() == 57 and self.get_token_q_step_count() == 57:
            return True
        else:
            return False

    def get_token_p_step_count(self):
        return self.__token_p.get_step_count()

    def get_token_q_step_count(self):
        return self.__token_q.get_step_count()

    # Gets the name of the current space
    def get_space_name(self, steps):
        if steps == -1:
            return 'H'
        elif steps == 0:
            return 'R'
        elif steps > 50:
            return '{0}{1}'.format(self.__position, steps - 50)
        elif steps == 57:
            return 'E'
        else:
            if self.__start + steps > 56:
                return (steps + self.__start) - 56
            else:
                return self.__start + steps - 1

    #Stack token bool
    def toggle_stacked(self):
        self.__stacked = not self.__stacked

    #Get stacked bool
    def get_stacked(self):
        return self.__stacked

    @property
    def token_p(self):
        return self.__token_p

    @property
    def token_q(self):
        return self.__token_q


class Token:
    # initial method or the construction of the class Token
    def __init__(self, name):
        self._token_name = name
        self._step_count = -1

    # gets the number of next steps to go
    def get_step_count(self):
        return self._step_count

    @property
    def token_name(self):
        print('getting token name')
        return self._token_name
    
    @token_name.setter
    def token_name(self, new_name):
        print('setting token name')
        self._player_name = new_name

    # Moves a player to the next step
    def move(self, steps):
        if steps + self._step_count > 57:
            self._step_count = 57 - (steps + self._step_count - 57)
        else:
            self._step_count += steps


# =============================== Skeleton Code ============================================

players = ['A','B','C','D']
turns = [('A', 6),('A', 1),('B', 6),('B', 2),('C', 6),('C', 3),('D', 6),('D', 4)]

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