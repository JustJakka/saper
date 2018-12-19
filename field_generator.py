from random import randint


def generate_field():
    field = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    for _ in range(10):
        i = randint(0, 7)
        j = randint(0, 7)
        while field[i][j] != 0:
            i = randint(0, 7)
            j = randint(0, 7)
        field[i][j] = 9

    for i in range(8):
        for j in range(8):
            if field[i][j] == 9:
                if j > 0:
                    if field[i][j - 1] != 9:
                        field[i][j - 1] += 1
                    if i > 0 and field[i - 1][j - 1] != 9:
                        field[i - 1][j - 1] += 1
                    if i < 7 and field[i + 1][j - 1] != 9:
                            field[i + 1][j - 1] += 1
                if j < 7:
                    if field[i][j + 1] != 9:
                        field[i][j + 1] += 1
                    if i > 0 and field[i - 1][j - 1] != 9:
                        field[i - 1][j - 1] += 1
                    if i < 7 and field[i + 1][j - 1] != 9:
                        field[i + 1][j - 1] += 1
                if i > 0 and field[i - 1][j] != 9:
                    field[i - 1][j] += 1
                if i < 7 and field[i + 1][j] != 9:
                    field[i + 1][j] += 1
