class ShipGame:
    """The class that handles playing Battleship"""

    def __init__(self):
        """sets all data members to initial values"""
        ''' initialize two boards with identical coordinates 1-10'''
        self.p1_board = [[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["D", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["G", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["H", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["I", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["J", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

        self.p2_board = [[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["D", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["G", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["H", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["I", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["J", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

        self.current_state = "UNFINISHED"

        # we will append p1_locations with a list of coordinates that collectively represent an entire ship
        self.p1_locations = []
        # the list 'p1_attacks_received' holds the coordinates of each torpedo fired against p1
        self.p1_attacks_received = []
        # we will append p2_locations with a list of coordinates that collectively represent an entire ship
        self.p2_locations = []
        # the list 'p2_attacks_received' holds the coordinates of each torpedo fired against p1
        self.p2_attacks_received = []
        self.players_turn = "p1"

        # track number of ships remaining
        self.p1_num_ships_remaining = 0
        self.p2_num_ships_remaining = 0

    def get_letter_to_numbers(self, letter):

        letters_to_numbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
        verified_letter = str(letter.upper())
        if verified_letter in letters_to_numbers.keys():
            return letters_to_numbers[verified_letter]
        else:
            return False

    def set_players_turn(self, player):
        if player == 'first' or player == 'p1':
            self.players_turn = 'p1'

        if player == 'second' or player == 'p2':
            self.players_turn = 'p2'

    def get_players_turn(self):
        return self.players_turn

    def print_board(self, player):
        """prints the board of the player passed"""
        if player == 'first' or player == 'p1':
            print("\n\t\t\tPLAYER ONE BOARD\n\t\t\t*****************\n")
            for row in self.p1_board:
                for square in row:
                    print(square, end="    ")
                print('\n')

        if player == 'second' or player == 'p2':
            print("\n\t\t\tPLAYER TWO BOARD\n\t\t\t*****************\n")
            for row in self.p2_board:
                for square in row:
                    print(square, end="    ")
                print('\n')

    def get_current_state(self):
        return self.current_state

    def get_num_ships_remaining(self, player):
        if player == 'first':
            return int(self.p1_num_ships_remaining)
        if player == 'second':
            return int(self.p2_num_ships_remaining)

        else:
            print("Request for number of ships remaining for player invalid.\nType either 'first' or 'second'.")

    def decrement_num_ships_remaining(self, player):
        if player == 'first' or player == 'p1':
            self.p1_num_ships_remaining -= 1
            return
        if player == 'second' or player == 'p2':
            self.p2_num_ships_remaining -= 1
            return
        else:
            print("Request to decrement # of ships remaining for player invalid.\nType either 'first' or 'second' " +
                  "to decrement the corresponding player's amount of ships remaining.")

    def increment_num_ships_remaining(self, player):
        if player == 'first' or player == 'p1':
            self.p1_num_ships_remaining += 1
            return
        if player == 'second' or player == 'p2':
            self.p2_num_ships_remaining += 1
            return
        else:
            print("Request to increment # of ships remaining for player invalid.\nType either 'first' or 'second' " +
                  "to increment the corresponding player's amount of ships remaining.")

    def place_ship(self, player, ship_length, coordinate, orientation):
        """takes player (strings either 'first' or 'second'), length of the ship (can be int),
        the coordinates of the ship's square coordinates closest to A1, and the ship's coordination
        referred to above as 'orientation' (either string 'R' or 'C' meaning row or column respectively.)"""

        # we will later check if we have all the criteria for a valid ship.  If so, ship will get appended w/coords.
        ship = []

        # input validation clauses for early termination if error in ship_length, orientation, or player input.
        if ship_length < 2:
            print("That's a life-saver, not a boat!! All ships need a minimum length of 2!")
            return False

        orientation = orientation.upper()

        if orientation != "R" and orientation != "C":
            print("Invalid orientation provided.  Choose either R for horizontal or C for vertical")

        if player != 'p1' and player != 'first' and player != 'p2' and player != 'second':
            print("Invalid player.")
            return False

        # Now, we do input validation on coordinate provided
        if len(coordinate) != 2 and len(coordinate) != 3:
            print("invalid coordinate. Letter must be A-J and number must be 1-10")
            return False

        if coordinate[0].isalpha() is False:
            print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
            return False

        if len(coordinate) == 2:
            if coordinate[1].isdigit() is False:
                print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
                return False

        if len(coordinate) == 3:
            if coordinate[1].isdigit() is False or coordinate[2].isdigit() is False:
                print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
                return False

        row_letter = coordinate[0].upper()
        row = self.get_letter_to_numbers(row_letter)
        if row is False:
            print("Invalid letter.  Choose from A-J")
            return False

        col = int(coordinate[1:len(coordinate)])

        if col > 10 or col < 1:
            print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
            return False

        # The coordinate is valid, but we haven't compared it to previous ship(s) coordinates or extended ships from it.

        # check that ship would be on the board coordinate is on the board

        if orientation == 'R':
            endpoint = col - 1 + ship_length
            if endpoint > 10:
                print("Your ship does not fit on the board")
                return False

            else:
                for relative_ship_pos in range(0, ship_length):
                    new_ship_coord = (row, col + relative_ship_pos)
                    ship.append(new_ship_coord)

        if orientation == 'C':
            endpoint = row - 1 + ship_length
            if endpoint > 10:
                print("Your ship does not fit on the board")
                return False
            else:
                for relative_ship_pos in range(0, ship_length):
                    new_ship_coord = (row + relative_ship_pos, col)
                    ship.append(new_ship_coord)

        # now we have a ship that is a list of tuple coordinates in (row, col) pattern

        # check all coordinates to see if we will overlap with a previously placed ship (i.e. crashes not allowed)
        if player == "p1" or player == "first":
            for coord in ship:
                for ship_container in self.p1_locations:
                    for stored_coordinate in ship_container:
                        if coord == stored_coordinate:
                            print("Oops!  Your ships will crash with these overlapping coordinates!\ntry again!")
                            return False

            # At this point we know it is a valid ship.
            # Let us update the px_locations to hold this for checking later
            self.p1_locations.append(ship)
            self.increment_num_ships_remaining('first')

            for ship_coord in ship:
                vis_board_row = ship_coord[0]
                vis_board_col = ship_coord[1]
                self.p1_board[vis_board_row][vis_board_col] = 'S'
            # Now we have successfully added the ship.
            # simply return True
            return True

        if player == "p2" or player == "second":
            for coord in ship:
                for ship_container in self.p2_locations:
                    for stored_coordinate in ship_container:
                        if coord == stored_coordinate:
                            print("Oops!  Your ships will crash with these overlapping coordinates!\ntry again!")
                            return False

            # At this point we know it is a valid ship.
            # Let us update the px_locations to hold this for checking later
            self.p2_locations.append(ship)
            self.increment_num_ships_remaining('second')

            for ship_coord in ship:
                vis_board_row = ship_coord[0]
                vis_board_col = ship_coord[1]
                self.p2_board[vis_board_row][vis_board_col] = 'S'
            # Now we have successfully added the ship.
            # simply return True
            return True

    def fire_torpedo(self, player, torpedo_coordinates):
        """takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates
           of the target square to decide whether hit the target and change the game status accordingly"""
        # If game is already over, return False
        if self.current_state != "UNFINISHED":
            return False

        # make sure the player's turn is correct, return False if not.
        if player == 'first' and self.players_turn != 'p1':
            print("Sorry, Player One!  It is not your turn!")
            return False
        if player == 'second' and self.players_turn != 'p2':
            print("Sorry, Player Two!  It is not your turn!")
            return False

        # validate the torpedo coordinate
        if len(torpedo_coordinates) != 2 and len(torpedo_coordinates) != 3:
            print("invalid coordinate. Letter must be A-J and number must be 1-10")
            return False

        if torpedo_coordinates[0].isalpha() is False:
            print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
            return False

        if len(torpedo_coordinates) == 2:
            if torpedo_coordinates[1].isdigit() is False:
                print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
                return False

        if len(torpedo_coordinates) == 3:
            if torpedo_coordinates[1].isdigit() is False or torpedo_coordinates[2].isdigit() is False:
                print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
                return False

        row_letter = torpedo_coordinates[0].upper()
        row = self.get_letter_to_numbers(row_letter)
        if row is False:
            print("Invalid letter.  Choose from A-J")
            return False

        col = int(torpedo_coordinates[1:len(torpedo_coordinates)])

        if col > 10 or col < 1:
            print("invalid coordinate. Letter must be A-J and number must be 1-10, ex A10")
            return False

        this_attack = (row, col)

        # Case if it was first player's turn
        if player == 'first' or player == 'p1':
            for previous_attack in self.p2_attacks_received:
                # if the player has already hit that spot, just change whose turn it is and return True...
                if previous_attack == this_attack:
                    self.set_players_turn('p2')
                    return True

            # if this is an unseen attack, add the attack to attack history
            self.p2_attacks_received.append(this_attack)

            # check victim's ship data
            for ship in self.p2_locations:
                for ship_coord in ship:
                    # if there is a match, then there was a hit
                    if ship_coord == this_attack:
                        print("DIRECT HIT!!!!")
                        vis_board_row = int(this_attack[0])
                        vis_board_col = int(this_attack[1])
                        # place an 'X' at that coordinate on the actual board
                        self.p2_board[vis_board_row][vis_board_col] = 'X'
                        # if the hit was on this ship, and the ship had one spot left...then px_num_ships_remaining -= 1
                        if len(ship) == 1:
                            self.decrement_num_ships_remaining('second')
                        # remove the coordinate from the internal p2_locations ship data
                        ship.remove(ship_coord)

                        if self.get_num_ships_remaining('second') == 0:
                            self.current_state = "FIRST_WON"
                            return True

                        # update turn and return True
                        self.set_players_turn('p2')
                        return True

            # if no hit, but unique shot, then place an 'O' to represent a miss
            print("Looks like a miss")
            vis_board_row = int(this_attack[0])
            vis_board_col = int(this_attack[1])
            self.p2_board[vis_board_row][vis_board_col] = 'O'
            self.set_players_turn('p2')
            return True

        # Case if it was second player's turn
        if player == 'second' or player == 'p2':
            for previous_attack in self.p1_attacks_received:
                # if the player has already hit that spot, just change whose turn it is and return True...
                if previous_attack == this_attack:
                    self.set_players_turn('p1')
                    return True

            # if this is an unseen attack, add the attack to attack history
            self.p1_attacks_received.append(this_attack)

            # check victim's ship data
            for ship in self.p1_locations:
                for ship_coord in ship:
                    # if there is a match, then there was a hit
                    if ship_coord == this_attack:
                        print("DIRECT HIT!!!!")
                        vis_board_row = int(this_attack[0])
                        vis_board_col = int(this_attack[1])
                        # place an 'X' at that coordinate on the actual board
                        self.p1_board[vis_board_row][vis_board_col] = 'X'
                        # if the hit was on this ship, and the ship had one spot left...then px_num_ships_remaining -= 1
                        if len(ship) == 1:
                            self.decrement_num_ships_remaining('first')
                        # remove the coordinate from the internal p2_locations ship data
                        ship.remove(ship_coord)

                        if self.get_num_ships_remaining('first') == 0:
                            self.current_state = "SECOND_WON"
                            return True

                        # update turn and return True
                        self.set_players_turn('p1')
                        return True

            # if no hit, but unique shot, then place an 'O' to represent a miss
            print("Looks like a miss")
            vis_board_row = int(this_attack[0])
            vis_board_col = int(this_attack[1])
            self.p1_board[vis_board_row][vis_board_col] = 'O'
            self.set_players_turn('p1')
            return True


def main():
    """
    print("****************************************************************************************************")
    print("\t\t\t\t\t\t\t\t\t\t\t\t BATTLESHIP                          -by Xinrui Hou")
    print("HOW TO PLAY: ")
    print("The computer will tell you whose turn it is.  Simply add coordinates in the 'NumberLetter' format.")
    print("ex. A9")
    print("If your torpedo hits, then an X appears on your opponent's board, otherwise a O indicates a miss")
    print("Once all of a player's ships are full of X's the game is over. The player to last fire a torpedo wins!\n")

    game = ShipGame()
    game.p1_board[3][3]= 'S'
    print(game.print_board("p1"))
    game.place_ship('p1', 3, 'C4', "C")
    game.print_board('p1')"""
    game = ShipGame()
    game.place_ship('p1', 2, 'A1', 'C')
    print(f"Player 1 has {game.get_num_ships_remaining('first')} ships remaining")

    game.place_ship('p2', 2, 'H10', 'C')
    print(f"Player 2 has {game.get_num_ships_remaining('second')} ships remaining")

    stop = False
    while stop is False:
        if game.get_players_turn() == 'p1':
            game.print_board('p2')
            print("\n\nFire torpedo Player One!")
            choose_coordinate = input("Choose your coordinates:  ")
            game.fire_torpedo('p1', choose_coordinate)
            game.print_board('p2')
            print(f"Player 2 has {game.get_num_ships_remaining('second')} ships remaining")
            if game.get_current_state() != "UNFINISHED":
                print("PLAYER TWO'S LAST SHIP HAS BEEN SUNK!  PLAYER ONE WINS!!!")
                break

        if game.get_players_turn() == 'p2':
            game.print_board('p1')
            print("\n\nFire torpedo Player Two!")
            choose_coordinate = input("Choose your coordinates:  ")
            game.fire_torpedo('p2', choose_coordinate)
            game.print_board('p1')
            print(f"Player 1 has {game.get_num_ships_remaining('first')} ships remaining")
            if game.get_current_state() != "UNFINISHED":
                print("PLAYER ONE'S LAST SHIP HAS BEEN SUNK!  PLAYER ONE WINS!!!")
                break



if __name__ == '__main__':
    main()