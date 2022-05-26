def main():
    #   Grid Structure
    # margin
    # row
    # divide
    # margin
    # row
    # divide
    # margin
    # row
    # margin
    DIVIDE = '_____|_____|_____'
    MARGIN = '     |     |     '
    a0 = '  -  '
    b0 = '|  -  |'
    c0 = '  -  '
    row_0 = [a0, b0, c0]
    #Row 1
    a1 = '  -  '
    b1 = '|  -  |'
    c1 = '  -  '
    #Row 2
    a2 = '  -  '
    b2 = '|  -  |'
    c2 = '  -  '


    class Grid:
        #Class Attributes
        #All grids will have the same margin and divide this does not change
        margin = '     |     |     '
        divide = '_____|_____|_____'
        #Instance Methods
        def __init__(self):
            #Class Attributes
            self.rows = {
                'a0': '  -  ', 'b0': '|  -  |', 'c0': '  -  ',

                'a1': '  -  ', 'b1': '|  -  |', 'c1': '  -  ',

                'a2': '  -  ', 'b2': '|  -  |', 'c2': '  -  '
            }

        #Instance Method
        def display_grid(self):
            """
            Displays the repersentation of the current grid
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

        def position_avaiable(self, pos):
            """
            If '-' is in selected position>> then position is available.
            If !'-' position is unavailable/ occupied.
            :param pos: User input. for desired pawn placement
            :return: True or False
            """
            if '-' in grid.rows[pos]:
                print('Debug:position available ')
                return True
            else:
                print('Debug:position occupied')
                return False

        def place_pawn(self, pos, pawn):
            self.rows[pos] = self.rows[pos].replace('-', pawn)
            return  #display grid ?

        def calculate_win(self, pawn):
            """
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
                print('No winning moves')
                return False

        def horizontal_win(self,pawn):
            """
            Condition 1: players pawn in the middle row(top,middle, bottom)>> else no horizontal win
            Conditon 2: players pawn in both adjcent position from pervious middle>> else no horizontal win
            :param pawn: current players pawn type. 'X' or 'O'
            :return: True or False
            """
            #top row check
            if pawn in self.rows['b0']:
                print('in top middle true ')
                #now check outter edges
                if pawn in self.rows['a0'] and pawn in  self.rows['c0']:
                    print('out edges true ')
                    print('horizontal win top row')
                    return True
                else:
                    print('Debug: No horizontal win')
                    return False
            #Check row 2
            elif pawn in self.rows['b1']:
                print('in middle middle true ')
                #now check outter edges
                if pawn in self.rows['a1'] and pawn in self.rows['c1']:
                    print('out edges true ')
                    print('horizontal win middle row')
                    return True
                else:
                    print('Debug: No horizontal win')
                    return False
            #Check Bottom Row
            elif pawn in self.rows['b2']:
                print('in bottom middle true ')
                #now check outter edges
                if pawn in self.rows['a2'] and pawn in self.rows['c2']:
                    print('out edges true ')
                    print('horizontal win bottom row')
                    return True
                else:
                    print('Debug: No horizontal win')
                    return False

            else:
                print('Debug: No horizontal win')
                return False

        def vertical_win(self, pawn):
            """
            Condition 1: Player pawn must be present within the middle box of columns (a,b,c)
            example a1, b1, c1>> if not no vertical win is possible
            Condition 2: player pawn must be present at either verticle side of middle box
            example pawn at 'a1'>>> pawns must be present at 'a0' and a2>> if not no vertical win is possible


            :param pawn: player pawn
            :return: True or False
            """
            #check middle position across board
            if pawn in self.rows['a1']:
                print('in col a  middle true ')
                if pawn in self.rows['a0'] and pawn in self.rows['a2']:
                    print('top and bottom edges true')
                    print('Vertical win true ')
                    return True
                else:
                    print('No veritcal win')
                    return False
            elif pawn in self.rows['b1']:
                print('in col b  middle true ')
                if pawn in self.rows['b0'] and pawn in self.rows['b2']:
                    print('top and bottom edges true')
                    print('Vertical win true ')
                    return True
                else:
                    print('No veritcal win')
                    return False
            elif pawn in self.rows['c1']:
                print('in col c  middle true ')
                if pawn in self.rows['c0'] and pawn in self.rows['c2']:
                    print('top and bottom edges true')
                    print('Vertical win true ')
                    return True
                else:
                    print('No veritcal win')
                    return False
            else:
                print('Debug: No Vertical win')
                return False

        def diagonal_win(self, pawn):
            """
            Condition 1: player pawn must be present is middle box for any diagonal win:>>> if not return false
            Conditon 2: player pawns must be present diagonal adjcent to middle boz to win: >>> if not return false
            :param pawn: player pawn
            :return: True or False
            """
            # pawn in center box
            if pawn in self.rows['b1']:
                print('pawn in center box')
                #Left to right diagonal
                if pawn in self.rows['a0'] and pawn in self.rows['c2']:
                    print('Diagonal winner left to right')
                    return True
                elif pawn in self.rows['c0'] and pawn in self.rows['a2']:
                    print('Diagonal winner right to left')
                    return True
                else:
                    print('no diagonal winner')
                    return False

            else:
                print('No diagonal Win')
                return False


    class Player:
        def __init__(self):
            self.active = None
            self.pawn = None
            self.position_selection = None
            self.winner = None

        def activate(self):
            self.active = True

        def deactivate(self):
            self.active = False

    grid = Grid()
    # player pawns
    p1_pawn = 'X'
    p2_pawn = '0'
    # some form of user inpout
    usr_pos = 'a0'
    game_on = True

    round = 0
    print('round', round)

    player1 = Player()
    player1.pawn = 'X'
    player2 = Player()
    player2.pawn = 'O'


    #Welcome message
    print('Welcome to TIC TAC TOE')

    while game_on:
        print('round',round)

        if round % 2 == 0:
            player1.active = True
            player2.active = False
            grid.display_grid()
            player1.position_selection = input('please select a box').lower()
            #check if position ok
            if grid.position_avaiable(pos=player1.position_selection):
                # place pawn
                grid.place_pawn(player1.position_selection, player1.pawn)
                #show players the grid
                grid.display_grid()
                # see if move results in win
                if grid.calculate_win(player1.pawn):
                    player1.winner = True
                    print('Winner PLAYER 1')
                    game_on = False
                else:
                    round += 1
                    # return to main loop



        else:
            print('round', round)
            player2.active = True
            player1.active = False
            grid.display_grid()

            player2.position_selection = input('please select a box').lower()
            # check if position ok
            if grid.position_avaiable(pos=player2.position_selection):
                # place pawn
                grid.place_pawn(player2.position_selection, player2.pawn)
                # show players the grid
                grid.display_grid()
                # see if move results in win
                if grid.calculate_win(player2.pawn):
                    player2.winner = True
                    print('Winner PLAYER 1')
                    game_on = False
                else:
                    round += 1
                    # return to main loop

if __name__ == "__main__":
    main()