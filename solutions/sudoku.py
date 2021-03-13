import sys
print() # This is to print a blank line
print("Welcome to Mbali's Sudoku Puzzle Solver. \nThis is the puzzle we will be solving today:")
print() # This is to print a blank line
problem = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [1, 2, -1, -1, -1, -1, -1, 8, 4],
        [-1, 3, -1, -1, -1, -1, -1, 7, -1],
        [-1, -1, 4, -1, -1, -1, 6, -1, -1],
        [-1, -1, -1, 2, -1, 3, -1, -1, -1],
        [-1, -1, 5, -1, -1, -1, 9, -1, -1],
        [-1, -1, 6, -1, 9, -1, 5, -1, -1],
        [-1, 7, -1, -1, -1, -1, -1, 2, -1],
        [-1, -1, -1, -1, 5, -1, -1, -1, -1]]
def add_borders(prob):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - - ")
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print(" | ", end="")
            if column == 8:
                print(prob[row][column])
            else:
                print(str(prob[row][column]) + " ", end="")
def empty_space(prob):
    for row in range(9):
        for column in range(9):
            if prob[row][column] == -1:
                return (row, column)
    print("Solution!!!")
def possible_number(prob, number, position):
    for row in range(9):
        if prob[position[0]][row] == number and position[1] != row:
            return False
    for column in range(9):
        if prob[column][position[1]] == number and position[0] != column:
            return False
    box_1 = position[1] // 3
    box_2 = position[0] // 3
    for row in range(box_2 * 3, box_2 * 3 + 3):
        for column in range(box_1 * 3, box_1 * 3 + 3):
            if prob[row][column] == number and (row, column) != position:
                return False
    return True
def solve_sudoku(puzzle):
    find = empty_space(puzzle)
    if not find:
        return True
    else:
        row, column = find
    for number in range(1, 10):
        if possible_number(puzzle, number, (row, column)):
            puzzle[row][column] = number
            if solve_sudoku(puzzle):
                return True
            else:
                puzzle[row][column] = -1
    return False
    print("No Solution?")
add_borders(problem)
print("_______________________________")
print()
solve_sudoku(problem)
print()
add_borders(problem)
# The following will output the Sudoku solution to a text file.
sys.stdout = open("Sudoku Solution.txt", "w")
print(add_borders(problem))
sys.stdout.close()


