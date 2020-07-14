board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!= 0:
                print(" ¦ ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def findEmpty(bo):
    for y in range(len(bo)):
        for x in range(len(bo[0])):
            if(bo[y][x] == 0):
                return (y, x) # return row, col
    return None #if there is no empty case

def checkValid(bo, num, pos):
    #Check if the row is valid
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and  pos[1] != i:
            return False

    #Check if the column is valid
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and  pos[0] != i:
            return False

    #Check if the square is valid
    boxRow = pos[1] // 3
    boxCol = pos[0] // 3

    for i in range(boxCol*3, boxCol*3 + 3):
        for j in range(boxRow*3, boxRow*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    #It passed all the check
    return True


def solve(bo):
    pos = findEmpty(bo)
    if not pos:
        return True

    for num in range(1, 10):
        if checkValid(bo, num, (pos[0], pos[1])):
            bo[pos[0]][pos[1]] = num

            #Check if the board is filled
            if solve(bo):
                return True

            bo[pos[0]][pos[1]] = 0
    return False


printBoard(board)
print("Solving in progress....")
solve(board)
print("")
print("Solving complete")
printBoard(board)