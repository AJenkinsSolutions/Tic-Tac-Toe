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


    grid = Grid()
    grid.display_grid()
    # player pawns
    p1_pawn = 'X'
    p2_pawn = '0'

    # some form of user inpout
    usr_pos = 'a0'
    print(grid.position_avaiable(pos=usr_pos))
    grid.place_pawn(usr_pos, p1_pawn)
    grid.display_grid()





    #









if __name__ == "__main__":
    main()