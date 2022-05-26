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
            if self.horizontal_win(pawn):
                return True


        def horizontal_win(self,pawn):
            """
            takes current players pawn as input
            Condition 1: players pawn in the middle row(top,middle, bottom)>> else no horizontal win
            Conditon 2: players pawn in both adjcent position from pervious middle>> else no horizontal win
            :param pawn: current players pawn type. 'X' or 'O'
            :return: True or False
            """
            #top row check
            if pawn in self.rows['b0']:
                print('in top middle true ')
                #now check outter edges
                if pawn in self.rows['a0'] and self.rows['c0']:
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
                if pawn in self.rows['a1'] and self.rows['c1']:
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
                if pawn in self.rows['a2'] and self.rows['c2']:
                    print('out edges true ')
                    print('horizontal win bottom row')
                    return True
                else:
                    print('Debug: No horizontal win')
                    return False

            else:
                print('Debug: No horizontal win')
                return False






    class Player:
        def __init__(self):
            self.active = None
            self.pawn = None
            self.position_selection = None

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

    player1 = Player()
    player1.pawn = 'X'
    player2 = Player()
    player2.pawn = 'O'


    #Welcome message
    print('Welcome to TIC TAC TOE')

    round = 0
    print('round', round)

    if round % 2 == 0:
        player1.active = True
        player2.active = False
        print('player1', player1.active, player1.pawn)
        print('player2', player2.active, player2.pawn)
        grid.display_grid()
        player1.position_selection = input('please select a box').lower()

        if grid.position_avaiable(pos=player1.position_selection):

            grid.place_pawn(player1.position_selection, player1.pawn)

            grid.calculate_win(player1.pawn)
            grid.display_grid()

    else:
        player2.active = True
        player1.active = False
        print('player2', player2.active, player2.pawn)
        print('player1', player1.active, player1.pawn)





    # if grid.position_avaiable(pos=position_selection):
    #
    #     grid.place_pawn(usr_pos, p1_pawn)
    # grid.display_grid()





if __name__ == "__main__":
    main()