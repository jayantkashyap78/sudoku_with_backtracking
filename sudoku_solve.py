sod = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def solve(sod):
    find = find_empty(sod)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1 ,10):
        if valid(sod, i, (row, col)):
            sod[row][col] = i

            if solve(sod):
                return True

            sod[row][col] = 0

    return False

  #Find if the current sod is valid
def valid(sod, num, pos):
    #check the number in the row by traversing through each column of the row
    for i in range(len(sod[0])):
        if sod[pos[0]][i] == num and pos[1] != i:
            return False

    #check the number in the column
    for i in range(len(sod)):
        if sod[i][pos[1]] == num and pos[0] != i:
            return False

    #check the 3x3 box
    #divide box in 3x3
    sod_x = pos[1] // 3
    sod_y = pos[0] // 3

    for i in range(sod_y *3, sod_y *3 + 3):
        for j in range(sod_x * 3, sod_x *3 + 3):
            if sod[i][j] == num and (i ,j) != pos:
                return False

    return True


def print_sod(sod):
    for i in range(len(sod)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sod[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sod[i][j])
            else:
                print(str(sod[i][j]) + " ", end="")


def find_empty(sod):  # change the 0 present in the sod  and return an empty space
    for i in range(len(sod)):
        for j in range(len(sod[0])):
            if sod[i][j] == 0:
                return (i, j)  # row, col

    return None
print_sod(sod)
solve(sod)
print("----------------------------")
print("Solved sudoku is below")
print("----------------------------")
print_sod(sod)

