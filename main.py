def main():
    class Grid:
        #   Class Attributes
        #   All grids will have the same margin and divide
        margin = '     |     |     '
        divide = '_____|_____|_____'

        #   Instance Attributes
        def __init__(self):

            #   Class Attributes
            self.rows = {
                'a0': '  -  ', 'b0': '|  -  |', 'c0': '  -  ',

                'a1': '  -  ', 'b1': '|  -  |', 'c1': '  -  ',

                'a2': '  -  ', 'b2': '|  -  |', 'c2': '  -  '
            }
            self.winner = None

            self.art = """
                         _______       ______           ______           
                        /_  __(_)___  /_  __/__ _____  /_  __/__  ___    
                         / / / / __/   / / / _ `/ __/   / / / _ \/ -_)   
                        /_/ /_/\__/   /_/  \_,_/\__/   /_/  \___/\__/                                      
            """

        # Instance Method
        def display_grid(self):
            """
            Displays the visual representation of the current grid
            :return: Nothing
            """
            print(self.margin)
            print(f'{self.rows["a0"]}{self.rows["b0"]}{self.rows["c0"]}')
            print(self.divide)
            print(self.margin)
            print(f'{self.rows["a1"]}{self.rows["b1"]}{self.rows["c1"]}')
            print(self.divide)
            print(self.margin)
            print(f'{self.rows["a2"]}{self.rows["b2"]}{self.rows["c2"]}')
            print(self.margin)

        def pos_available(self, pos):
            """
            If '-' is in selected position>> then position is available.
            If !'-' position is unavailable/ occupied.
            :param pos: User input. for desired pawn placement
            :return: True or False
            """
            if '-' in grid.rows[pos]:
                # print('Debug:position available ')
                return True
            else:
                # print('Debug:position occupied')
                return False

        def place_pawn(self, pos, pawn):
            """
            Takes current players chosen position and Pawn, updates Grid Boxes.
            :param pos: Player chosen position
            :param pawn: Players Pawn
            :return:
            """
            self.rows[pos] = self.rows[pos].replace('-', pawn)
            return  # display grid ?

        def calculate_win(self, pawn):
            """
            Takes player pawn attribute. Runs three functions to check for a winning combination
            :param pawn: player pawn
            :return: True or false
            """
            if self.horizontal_win(pawn):
                return True
            elif self.vertical_win(pawn):
                return True
            elif self.diagonal_win(pawn):
                return True
            else:
                # print('No winning moves')
                return False

        def horizontal_win(self, pawn):
            """
            Condition 1:Pawn in the middle row(top, middle, bottom)
            Conditon 2:Pawn in both adjacent position from previous middle
            :param pawn: current players pawn 'X' or 'O'
            :return: True or False
            """
            # top row check
            if pawn in self.rows['b0']:
                # print('in top middle true ')
                # now check outter edges
                if pawn in self.rows['a0'] and pawn in self.rows['c0']:
                    # print('out edges true ')
                    # print('horizontal win top row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False
            # Check row 2
            elif pawn in self.rows['b1']:
                # print('in middle middle true ')
                # now check outter edges
                if pawn in self.rows['a1'] and pawn in self.rows['c1']:
                    # print('out edges true ')
                    # print('horizontal win middle row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False
            # Check Bottom Row
            elif pawn in self.rows['b2']:
                # print('in bottom middle true ')
                # now check outter edges
                if pawn in self.rows['a2'] and pawn in self.rows['c2']:
                    # print('out edges true ')
                    # print('horizontal win bottom row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False

            else:
                # print('Debug: No horizontal win')
                return False

        def vertical_win(self, pawn):
            """
            Condition 1: Player pawn must be present within the middle box of columns (a Or b Or c)
                            Example a1, b1, c1.
            Condition 2: player pawn must be present at either vertical side of middle box
                            Example pawn at 'a1' pawns must be present at 'a0' and a2>>
            :param pawn: player pawn
            :return: True or False
            """
            # Check middle position across board
            if pawn in self.rows['a1']:
                # print('in col a  middle true ')
                if pawn in self.rows['a0'] and pawn in self.rows['a2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            elif pawn in self.rows['b1']:
                # print('in col b  middle true ')
                if pawn in self.rows['b0'] and pawn in self.rows['b2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            elif pawn in self.rows['c1']:
                # print('in col c  middle true ')
                if pawn in self.rows['c0'] and pawn in self.rows['c2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            else:
                # print('Debug: No Vertical win')
                return False

        def diagonal_win(self, pawn):
            """
            Condition 1: Pawn must be present in middle box for any diagonal win
            Condition 2: Pawns must be present diagonal adjacent to middle boz to win
            :param pawn: player pawn
            :return: True or False
            """
            #   pawn in center box
            if pawn in self.rows['b1']:
                # print('pawn in center box')

                #   Left to right diagonal
                if pawn in self.rows['a0'] and pawn in self.rows['c2']:
                    # print('Diagonal winner left to right')
                    return True
                elif pawn in self.rows['c0'] and pawn in self.rows['a2']:
                    # print('Diagonal winner right to left')
                    return True
                else:
                    # print('no diagonal winner')
                    return False
            else:
                # print('No diagonal Win')
                return False

        def show_winner(self):
            print(f'Winner: {self.winner}')

        def get_input(self, choice):
            if len(choice) == 2:
                if choice[0] not in alpha or choice[1] not in numberic:
                    print('Invalid Input: only a,b,c and 0, 1, 2')
                    return False
                else:
                    return True
            elif len(choice) < 2:
                print('To Short: Choice must me 2 Characters long\n Using only a,b,c and 1,2,3')
                return False
            elif len(choice) > 2:
                print('To Long: Choice must me 2 Characters long\n Using only a,b,c and 1,2,3')
                return False

    class Player:
        def __init__(self, name):
            self.name = name
            self.active = None
            self.pawn = None
            self.position_selection = None
            self.winner = None

        def activate(self):
            self.active = True

        def deactivate(self):
            self.active = False

    alpha = ['a', 'b', 'c']
    numberic = ['0', '1', '2']

    game_on = True
    game_menu_on = True
    picks = 0

    while game_menu_on:

        # Initialize Grid
        grid = Grid()
        # Initialize Players
        player1 = Player('player1')
        player1.pawn = 'X'
        player2 = Player('player2')
        player2.pawn = 'O'

        # Welcome message
        # print('                     TIC TAC TOE\n')
        print(f'{grid.art}')
        print('How to play:\nSelect a box using its Column letter and row number')
        print('Columns: a,b,c Rows: 1, 2, 3\n')
        while game_on and picks < 9:
            active_player = player1 if picks % 2 == 0 else player2

            # Game View
            print('Picks:', picks)
            print(f'Turn: {active_player.name}')
            grid.display_grid()

            answer_good = False
            while not answer_good:
                # Get input
                choice = input('Please select a box !').lower().strip()
                # Evaluate Answer
                answer_good = grid.get_input(choice)

            # Assign User Choice to class
            active_player.pos_selection = choice

            # Check if position available
            if grid.pos_available(pos=active_player.pos_selection):
                # Place pawn
                grid.place_pawn(active_player.pos_selection, active_player.pawn)
                # Show updated grid
                # Move result in win ?
                if grid.calculate_win(active_player.pawn):
                    # Update winner
                    active_player.winner = True
                    grid.winner = 'Player 1'
                    # Update Game Status
                    game_on = False
                else:
                    picks += 1
                    continue
                    # return to main loop

        # Exit Clean up
        grid.display_grid()
        grid.show_winner()
        picks = 0
        play_again = input('Would you like to play again ? y/n').lower()
        if play_again == 'n':
            game_menu_on = False
            print('Thank you for playing\n Goodbye')
        else:
            game_on = True
            game_menu_on = True


if __name__ == "__main__":
    main()
