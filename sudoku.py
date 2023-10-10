# pylint: disable=missing-docstring

def sudoku_validator(grid):
    '''method to check that the sudoku is valid:
    A row contains all numbers from 1 to 9
    A column contains all numbers from 1 to 9
    Each of the nine 3x3 little squares contains numbers from 1 to 9'''

    super_list = [1,2,3,4,5,6,7,8,9]

    #Check if each row has 1 to 9
    for i in range(9):
        if set(super_list) != set(grid[i]):
            return False
    #print(row_has_all)

    #check if each column has 1 to 9
    for j in range(9):
        each_column = [row[j] for row in grid]
        #print(each_column)
        if set(super_list) != set(each_column):
            return False

    #check if 3*3 tile has 1 to 9
    top_left_grid = grid[0][0:3]+grid[1][0:3]+grid[2][0:3]
    top_middle_grid = grid[0][3:6]+grid[1][3:6]+grid[2][3:6]
    top_right_grid = grid[0][6:9]+grid[1][6:9]+grid[2][6:9]

    middle_left_grid = grid[3][0:3]+grid[4][0:3]+grid[5][0:3]
    middle_middle_grid = grid[3][3:6]+grid[4][3:6]+grid[5][3:6]
    middle_right_grid = grid[3][6:9]+grid[4][6:9]+grid[5][6:9]

    bottom_left_grid = grid[6][0:3]+grid[7][0:3]+grid[8][0:3]
    bottom_middle_grid = grid[6][3:6]+grid[7][3:6]+grid[8][3:6]
    bottom_right_grid = grid[6][6:9]+grid[7][6:9]+grid[8][6:9]

    for small_grid in [top_left_grid, top_middle_grid, top_right_grid,
                    middle_left_grid, middle_middle_grid, middle_right_grid,
                    bottom_left_grid, bottom_middle_grid, bottom_right_grid]:
        if set(small_grid) != set(super_list):
            return False

    return True
