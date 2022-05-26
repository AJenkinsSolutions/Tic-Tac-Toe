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
            #row 0
            self.a0 = '  -  '
            self.b0 = '|  -  |'
            self.c0 = '  -  '
            #row 1
            self.a1 = '  -  '
            self.b1 = '|  -  |'
            self.c1 = '  -  '
            #row 2
            self.a2 = '  -  '
            self.b2 = '|  -  |'
            self.c2 = '  -  '

        #Instance Method

        def display_grid(self):

            print(self.margin)
            print(f'{self.a0}{self.b0}{self.c0}')
            print(self.divide)
            print(self.margin)
            print(f'{self.a1}{self.b1}{self.c1}')
            print(self.divide)
            print(self.margin)
            print(f'{self.a2}{self.b2}{self.c2}')
            print(self.margin)

    grid = Grid()
    grid.display_grid()

    # if '-' in grid.a0:
    #     grid.a0 = grid.a0.replace('-', 'X')









if __name__ == "__main__":
    main()