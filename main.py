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
                'a0': '  x  ', 'b0': '|  -  |', 'c0': '  -  ',

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

    grid = Grid()
    grid.display_grid()

    p1_pawn = 'X'
    p2_pawn = '0'
    usr_pos = 'a0'
    print(grid.position_avaiable(pos=usr_pos))






    # if '-' in grid.a0:
    #     grid.a0 = grid.a0.replace('-', 'X')










if __name__ == "__main__":
    main()