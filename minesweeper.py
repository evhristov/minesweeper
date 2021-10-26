from random import randint
from collections import deque
from string import ascii_uppercase


def generate_field(size, mines):

    field = [[0]*size for _ in range(size)]
    for _ in range(mines):
        while True:
            x = randint(0, size-1)
            y = randint(0, size-1)
            if field[x][y] != "*":
                break

        field[x][y] = "*"

        for i in range(-1,2):
            if 0 <= x+i <= size - 1:
                for j in range(-1,2):
                    if 0 <= y+j <= size - 1:
                        if not field[x+i][y+j] == "*":
                            field[x+i][y+j] += 1

    # for _ in field:
    #     _ = [str(x) for x in _]
    #     print(" ".join(_))

    return field


def make_selection(x_input,y_input):
    cleared = set()
    if field[x_input][y_input] == "*":
        print("BOOM")
        return True
    else:
        player_field[x_input][y_input] = field[x_input][y_input]
        cleared.add((x_input,y_input))
        cleared.update(show_all_zero(x_input,y_input))
        return False, len(cleared)


def show_all_zero(x_input,y_input):
    cleared_0 = set()
    zero_stack = deque()
    zero_done = []
    for i in range(-1, 2):
        if 0 <= x_input + i <= size - 1:
            for j in range(-1, 2):
                if 0 <= y_input + j <= size - 1:
                    if field[x_input + i][y_input + j] == 0:
                        zero_stack.append((x_input + i, y_input + j))

    while zero_stack:
        x, y = zero_stack.popleft()
        zero_done.append((x,y))
        for i in range(-1, 2):
            if 0 <= x + i <= size - 1:
                for j in range(-1, 2):
                    if 0 <= y + j <= size - 1:
                        player_field[x+i][y+j] = field[x+i][y+j]
                        cleared_0.add((x+i,y+j))
                        if field[x + i][y + j] == 0 and (x+i, y+j) not in zero_done and (x+i,y+j) not in zero_stack:
                            zero_stack.append((x + i, y + j))
    return cleared_0


def mark_mine(x,y):
    if player_field[x][y] == " ":
        player_field[x][y] = "M"
        return 1
    elif player_field[x][y] == "M":
        player_field[x][y] = " "
        return -1
    else:
        print("Cannot mark mine there!")
    return 0


def show_field(player_field):
    #os.system('cls||clear')
    row = 0
    print("  | " + " | ".join([alph[x] for x in range(size)]) + " | ")
    print("--|"+"---|"*(size))
    while row < size:
        if row + 1 < 10:
            result = " "
        else:
            result = ""
        result += f"{row + 1}| "+" | ".join(map(str,player_field[row]))+" | "
        print(result)
        print("--|"+"---|"*size)
        row += 1
    print(f"Marked mines: {marked_mines} / {mines} | | Cleared Spaces : {cleared_squares} / {size*size-mines}")


if __name__ == "__main__":
    alph = list(ascii_uppercase)
    while True:
        ded = False
        size = int(input("Please input number of rows:"))
        mines = int(input("Please input number of mines:"))
        marked_mines = 0
        cleared_squares = 0
        field = generate_field(size, mines)
        player_field = [[" "]*size for _ in range(size)]
        show_field(player_field)
        while True:
            command = input().split()
            if command[0] == "MM":
                marked_mines += mark_mine(int(command[2])-1,alph.index(command[1]))
            else:
                try:
                    y_input = alph.index(command[0])
                    x_input = int(command[1]) - 1
                except:
                    print("Please input 'A 1' format!")

                result = make_selection(x_input, y_input)
                if not isinstance(result,bool):
                    ded = result[0]
                    cleared_squares += result[1]
                else:
                    ded = True
            show_field(player_field)
            if cleared_squares == size**2 - mines:
                print("Bravo! You have won!\nYou deserve a cookie!")
                break

            if ded:
                print("U ded! :(")
                break

        if input("Would you like to play again? (Y/N):") not in ["Y","y"]:
            break
        #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