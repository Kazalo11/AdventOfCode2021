goes = [87, 7, 82, 21, 47, 88, 12, 71, 24, 35, 10, 90, 4, 97, 30, 55, 36, 74, 19, 50, 23, 46, 13, 44, 69, 27, 2, 0, 37,
        33, 99, 49, 77, 15, 89, 98, 31, 51, 22, 96, 73, 94, 95, 18, 52, 78, 32, 83, 85, 54, 75, 84, 59, 25, 76, 45, 20,
        48, 9, 28, 39, 70, 63, 56, 5, 68, 61, 26, 58, 92, 67, 53, 43, 62, 17, 81, 80, 66, 91, 93, 41, 64, 14, 8, 57, 38,
        34, 16, 42, 11, 86, 72, 40, 65, 79, 6, 3, 29, 60, 1]

wins = []
board = []


def find_win(board):
    sol = ['.', '.', '.', '.', '.']
    count = 1
    for go in goes:
        for i, lst in enumerate(board):
            for j, value in enumerate(lst):
                if value == go:
                    board[i][j] = '.'
        for row in board:
            if row == sol:
                return (count, board, go)
        for i in range(len(board)):
            col = [row[i] for row in board]
            if col == sol:
                return (count, board, go)
        count += 1


with open('day4input.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            wins.append(find_win(board))
            board = []
        else:
            line = line.split(' ')
            line = [int(i) for i in line if i.isnumeric()]
            board.append(line)

wins.append(find_win(board))

wins = sorted(wins, key=lambda x: x[0])
answer = wins[-1]
final_board = answer[1]
total = 0
for row in final_board:
    for column in row:
        if column != '.':
            total += column

print(total * answer[2])
