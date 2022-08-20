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
        if temp_player.get_token_p_step_count() < temp_player.get_token_q_step_count():
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

    #Returns true if a player token has an exact roll for 57
    def token_exact(self, player, roll):
        if self.get_player_by_position(player).get_token_p_step_count() == (57-roll) or self.get_player_by_position(player).get_token_q_step_count() == (57-roll):
            print("exact")
            return True
        else:
            return False
    
    #Returns token with exact roll needed:
    def token_exact_helper(self, player, roll):
        if self.get_player_by_position(player).get_token_p_step_count() == (57-roll):
            return 'p'
        else:
            return 'q'
    
    #Returns true if a token can land on another opponent
    def token_can_attack(self, player, roll):
        temp_player = self.get_player_by_position(player)
        p_potential_spot = temp_player.get_space_name(temp_player.get_token_p_step_count() + roll)
        q_potential_spot = temp_player.get_space_name(temp_player.get_token_q_step_count() + roll)

        for gamer in self.__players:
            if gamer != temp_player:
                gamers_space_p = gamer.get_space_name(gamer.get_token_p_step_count())
                gamers_space_q = gamer.get_space_name(gamer.get_token_q_step_count())

                if gamers_space_p == p_potential_spot or gamers_space_p == q_potential_spot:
                    return True
                elif gamers_space_q == p_potential_spot or gamers_space_q == q_potential_spot:
                    return True

        return False 

    #Returns token that can attack
    def token_can_attack_helper(self, player, roll):
        temp_player = self.get_player_by_position(player)
        p_potential_spot = temp_player.get_space_name(temp_player.get_token_p_step_count() + roll)
        q_potential_spot = temp_player.get_space_name(temp_player.get_token_q_step_count() + roll)

        q_can_attack = False
        p_can_attack = False

        for gamer in self.__players:
            if gamer != temp_player:
                gamers_space_p = gamer.get_space_name(gamer.get_token_p_step_count())
                gamers_space_q = gamer.get_space_name(gamer.get_token_q_step_count())
                
                if p_potential_spot == gamers_space_p or p_potential_spot == gamers_space_q:
                    p_can_attack = True
                
                if q_potential_spot == gamers_space_q or q_potential_spot == gamers_space_q:
                    q_can_attack = True
        
        if q_can_attack and p_can_attack:
            return self.farther_inplay_token(player)
        elif q_can_attack:
            return 'q'
        elif p_can_attack:
            return 'p'

    #Returns token based on move priority 
    def move_priority(self, player, roll):
        if roll == 6:
            #Priority 1
            if self.token_in_home(player):
                self.move_token(player, self.home_base(player), 1)
            #remember to implement reroll feature later 
            else:
                if self.get_player_by_position(player).get_stacked():
                    self.move_token(player, 'p', 6)
                    self.move_token(player, 'q', 6)
                    self.token_on_token(player, 'p')
                else:
                    #Priority 2
                    if self.token_exact(player, 6):
                        self.move_token(player, self.token_exact_helper(player, 6), 6)
                    else:
                        #Priority 3
                        if self.token_can_attack(player, 6):
                            temp_token = self.token_can_attack_helper(player, 6)
                            self.move_token(player, temp_token, 6)
                            self.token_on_token(player, temp_token)
                        else:
                            #Priority 4
                            temp_token = self.farther_token(player)
                            self.move_token(player, temp_token, 6)
                            self.token_on_token(player, temp_token)
        else:
            if self.get_player_by_position(player).get_stacked():
                self.move_token(player, 'p', roll)
                self.move_token(player, 'q', roll)
                self.token_on_token(player, 'p')
            else:
                if self.token_exact(player, roll):
                    self.move_token(player, self.token_exact_helper(player, roll), roll)
                else:
                    if self.token_can_attack(player, roll):
                        temp_token = self.token_can_attack_helper(player, roll)
                        self.move_token(player, temp_token, roll)
                        self.token_on_token(player, temp_token)
                    else:
                        temp_token = self.farther_inplay_token(player)
                        self.move_token(player, temp_token, roll)
                        self.token_on_token(player, temp_token)

    #Stack soft reset helper function
    def token_stack_reset(self, player):
        temp_player = self.get_player_by_position(player)
        temp_player.toggle_stacked()
        #resets token back to home base and toggles stacked
        self.move_token(player, 'p', -1 * (temp_player.get_token_p_step_count() + 1))
        self.move_token(player, 'q', -1 * (temp_player.get_token_q_step_count() + 1))

    #Checks if player has landed on another token
    def token_on_token(self, player, token):
        temp_player = self.get_player_by_position(player)
        #print('token:')
        #print(token)
        if token == 'p':
            temp_space = temp_player.get_space_name(temp_player.get_token_p_step_count())
            #Only checks for stacking on viable spots
            if temp_space != 'R' and temp_space != 'H' and temp_space != 'E':
                print('viable')
                #Toggles stacked if a token lands on the same spot as another token
                if temp_space == temp_player.get_space_name(temp_player.get_token_q_step_count()) and temp_player.get_stacked() != True:
                    temp_player.toggle_stacked()
        
                #Check every players token to see if token argument is on the same spot 
                for gamer in self.__players:
                    if temp_player != gamer:
                        if temp_space == gamer.get_space_name(gamer.get_token_p_step_count()):
                            if gamer.get_stacked():
                                self.token_stack_reset(gamer.get_position())
                            else:
                                self.move_token(gamer.get_position(), 'p', -1 * (gamer.get_token_p_step_count() + 1))
                        elif temp_space == gamer.get_space_name(gamer.get_token_q_step_count()):
                            self.move_token(gamer.get_position(), 'q', -1 * (gamer.get_token_q_step_count() + 1))
        else:
            temp_space = temp_player.get_space_name(temp_player.get_token_q_step_count())
            
            #Only checks for stacking on viable spots
            if temp_space != 'R' and temp_space != 'H' and temp_space != 'E':

                if temp_space == temp_player.get_space_name(temp_player.get_token_p_step_count()) and temp_player.get_stacked() != True: 
                    temp_player.toggle_stacked()
            
                for gamer in self.__players:
                    if temp_player != gamer:
                        if temp_space == gamer.get_space_name(gamer.get_token_p_step_count()):
                            if gamer.get_stacked():
                                self.token_stack_reset(gamer.get_position())
                            else:
                                self.move_token(gamer.get_position(), 'p', -1 * (gamer.get_token_p_step_count() + 1))
                        elif temp_space == gamer.get_space_name(gamer.get_token_q_step_count()):
                            self.move_token(gamer.get_position(), 'q', -1 * (gamer.get_token_p_step_count() + 1))
    
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
        elif steps > 50 and steps < 57:
            return '{0}{1}'.format(self.__position, steps - 50)
        elif steps == 57:
            return 'E'
        else:
            if self.__start + steps > 56:
                return str((steps + self.__start) - 56)
            else:
                return str(self.__start + steps - 1)

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

players = ['A','B']
turns = [('A', 6),('A', 4),('A', 4),('A', 4),('A', 6),('A', 5),('A', 3),('B', 6),('B', 2),('A', 2),('A', 4)]

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