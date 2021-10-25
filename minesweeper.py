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


def make_selection():
    alph = list(ascii_uppercase)
    command = input().split()
    if command[0] == "MM":
        mark_mine(int(command[2])-1,alph.index(command[1]))
        return False
    try:
        y_input = alph.index(command[0])
        x_input = int(command[1])-1
    except:
        print("Please input 'A 1' format!")
        return

    if field[x_input][y_input] == "*":
        print("BOOM")
        return True
    else:
        player_field[x_input][y_input] = field[x_input][y_input]
        show_all_zero(x_input,y_input)
        return False


def show_all_zero(x_input,y_input):
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
                        if field[x + i][y + j] == 0 and (x+i, y+j) not in zero_done and (x+i,y+j) not in zero_stack:
                            zero_stack.append((x + i, y + j))


def mark_mine(x,y):
    if player_field[x][y] == " ":
        player_field[x][y] = "M"
    elif player_field[x][y] == "M":
        player_field[x][y] = " "
    else:
        print("Cannot mark mine there!")
    return





def show_field(player_field):
    #os.system('cls||clear')
    alph = list(ascii_uppercase)
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


if __name__ == "__main__":
    while True:
        ded = False
        size = int(input("Please input number of rows:"))
        mines = int(input("Please input number of mines:"))
        field = generate_field(size, mines)
        player_field = [[" "]*size for _ in range(size)]

        while not ded:
            show_field(player_field)
            ded = make_selection()

        if input("U ded!\nWould you like to play again? (Y/N):") not in ["Y","y"]:
            break
