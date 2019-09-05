def square(sudoku):
    for i in range(3):
        for j in range(3):
            add = []
            for r in range(3):
                for c in range(3):
                    add.append(sudoku[r + i*3][c + j*3])
            if sorted(add) != number:
                return 0
    return 1


def row(sudoku):
    for i in range(9):
        add = []
        for j in range(9):
            add.append(sudoku[i][j])
        if sorted(add) != number:
            return 0
    return 1


def col(sudoku):
    for i in range(9):
        add = []
        for j in range(9):
            add.append(sudoku[j][i])
        if sorted(add) != number:
            return 0
    return 1

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if square(sudoku) == 1 and row(sudoku) == 1 and col(sudoku) == 1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))