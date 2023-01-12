 def welcome():
    print("--------------------------------------")
    print("      Добро пожаловать в игру:")
    print("        Кристики нолики 1.0")
    print("--------------------------------------")
    print(" Ход выполняется по двум координатам! ")
    print("--------------------------------------")



def game_board():
    print()
    print("            | 0 | 1 | 2 |")
    print("          ---------------")
    for i in range(3):
        print(f"          {i} | {board[i][0]} | {board[i][1]} | {board[i][2]} | ")
        print("          ---------------")
        print()


def entry():
    while True:
        cords = input("       Введите координаты:").split()

        if len(cords) != 2:
            print("Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if board[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

victory_comb = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))

def check_win():
    win_cord = victory_comb
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выйграл игрок №1!!!")
            print("Поздравляем!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл игрок №2!")
            print("Поздравляем!")
            return True
    return False

welcome()
board = [[" ", " ", " "] for i in range(3)]
move = 0

while True:
    move += 1

    game_board()

    if move % 2 == 1:
        print("Игрок 1 ставит X")
    else:
        print("Игрок 2 ставит 0")
    x, y = entry()

    if move % 2 == 1:
        board[x][y] = "x"
    else:
        board[x][y] = "0"
    if check_win():
        break
    if move == 9:

        print("Ничья")
        break