board = {"O": set(), "X": set()}

win_status = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]

human = "O"
computer = "X"


def getCell(index):
    if index in board[human]:
        return human
    if index in board[computer]:
        return computer
    return ""


def showBoard():
    print()

    for i in range(0, 9, 3):
        line = []

        for j in range(i, i + 3):
            cell = getCell(j)

            if cell == "":
                line.append(str(j + 1))
            else:
                line.append(cell)

        print(" " + " | ".join(line))

        if i < 6:
            print("---+---+---")

    print()


def updateGame(who, number):
    board[who].add(number)
    print(who, number + 1)


def isWin(turn):
    turn_set = board[turn]

    for status in win_status:
        if set(status).issubset(turn_set):
            return True

    return False


def isTie():
    return len(board[human] | board[computer]) == 9


def canWin(who):
    who_set = board[who]
    other = computer if who == human else human
    other_set = board[other]

    for status in win_status:
        status_set = set(status)

        if len(status_set & who_set) == 2:
            empty = status_set - who_set - other_set

            if len(empty) == 1:
                return next(iter(empty))

    return -1


def getComputerNumber():

    # 공격
    number = canWin(computer)

    if number != -1:
        return number

    # 방어
    number = canWin(human)

    if number != -1:
        return number

    # 가운데
    if getCell(4) == "":
        return 4

    # 코너
    for i in [0, 2, 6, 8]:
        if getCell(i) == "":
            return i

    # 남는 자리
    for i in range(9):
        if getCell(i) == "":
            return i

    return -1


print("========== Tic-tac-Toe ==========")

showBoard()

while True:

    human_input = int(input("숫자를 입력하세요: ")) - 1

    if human_input < 0 or human_input > 8:
        print("1~9만 입력 가능")
        continue

    if getCell(human_input) != "":
        print("이미 선택된 자리")
        continue

    updateGame(human, human_input)

    showBoard()

    if isWin(human):
        print("You Win")
        break

    if isTie():
        print("Draw")
        break

    computer_input = getComputerNumber()

    updateGame(computer, computer_input)

    showBoard()

    if isWin(computer):
        print("You Lose")
        break

    if isTie():
        print("Draw")
        break