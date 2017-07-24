from copy import deepcopy
from math import *

def get_neighbors(coordinates, board):
    neighbors = []
    for coordinate in coordinates:
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1] + 1])
        if coordinate[0] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1]])
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] - 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1] - 1])
        if coordinate[1] + 1 in range(len(board)):
            if [coordinate[0], coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] + 1])
        if coordinate[1] - 1 in range(len(board)):
            if [coordinate[0], coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] - 1])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] + 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1] + 1])
        if coordinate[0] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1]])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1] - 1])
    return neighbors

def get_unk_neighbors(coordinates, board):
    neighbors = []
    for coordinate in coordinates:
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1] + 1] not in neighbors and board[coordinate[0] + 1][coordinate[1] + 1] == -1: neighbors.append([coordinate[0] + 1, coordinate[1] + 1])
        if coordinate[0] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1]] not in neighbors and board[coordinate[0] + 1][coordinate[1]] == -1: neighbors.append([coordinate[0] + 1, coordinate[1]])
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] - 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1] - 1] not in neighbors and board[coordinate[0] + 1][coordinate[1] - 1] == -1: neighbors.append([coordinate[0] + 1, coordinate[1] - 1])
        if coordinate[1] + 1 in range(len(board)):
            if [coordinate[0], coordinate[1] + 1] not in neighbors and board[coordinate[0]][coordinate[1] + 1] == -1: neighbors.append([coordinate[0], coordinate[1] + 1])
        if coordinate[1] - 1 in range(len(board)):
            if [coordinate[0], coordinate[1] - 1] not in neighbors and board[coordinate[0]][coordinate[1] - 1] == -1: neighbors.append([coordinate[0], coordinate[1] - 1])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] + 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1] + 1] not in neighbors and board[coordinate[0] - 1][coordinate[1] + 1] == -1: neighbors.append([coordinate[0] - 1, coordinate[1] + 1])
        if coordinate[0] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1]] not in neighbors and board[coordinate[0] - 1][coordinate[1]] == -1: neighbors.append([coordinate[0] - 1, coordinate[1]])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1] - 1] not in neighbors and board[coordinate[0] - 1][coordinate[1] - 1] == -1: neighbors.append([coordinate[0] - 1, coordinate[1] - 1])
    return neighbors

def get_expected_mines(board):
    exp_mines = 0
    max_score = [0, 0, [0, 0]]
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board[row][col] > max_score[0] and board[row][col] > 0:
                max_score = [board[row][col], len(get_unk_neighbors([[row, col]], board)), [row, col]]
            elif board[row][col] == max_score[0] and len(get_unk_neighbors([[row, col]], board)) > max_score[1]:
                max_score = [board[row][col], len(get_unk_neighbors([[row, col]], board)), [row, col]]
    exp_mines += max_score[0]
    unks = []
    for unknown in get_unk_neighbors([max_score[2]], board):
        unks.append(unknown)
    num = 0
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board[row][col] > 0:
                neighbors = get_unk_neighbors([[row, col]], board)
                for unknown in neighbors:
                    if unknown in unks: num += 1
                if num == 0:
                    for unknown in neighbors:
                        unks.append(unknown)
                    exp_mines += board[row][col]
                num = 0
    return exp_mines
# Random General Cases
'''
true_board = [[2, 2, 9, 9, 2],
              [1, 1, 3, 9, 2],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 1, 2],
              [0, 0, 1, 3, 9]]

five_by_five = [[-1, -1, -1, -1, -1],
                [1, 1, 3, -1, -1],
                [0, 0, 1, 1, -1],
                [0, 0, 0, 1, -1],
                [0, 0, 1, 3, -1]]
'''
'''
true_board = [[0, 2, 9, 9, 3],
              [0, 2, 9, 3, 3],
              [0, 1, 1, 1, 2],
              [0, 0, 0, 0, 2],
              [0, 0, 0, 0, 1]]

five_by_five = [[0, 2, -1, -1, -1],
                [0, 2, -1, -1, -1],
                [0, 1, 1, 1, 2],
                [0, 0, 0, 0, 2],
                [0, 0, 0, 0, 1]]
'''



# 1-2-1 combination
### Algorithm Currently Failing Here
### It believes that the tile underneath the 2 is a mine (this is impossible)
### however, values are close 1.3333 vs 1.0. Threshold problem?

### Additionally, if I shift the grid one to the left or right, the algorithm
### can figure out where the bomb actually is

true_board = [[1, 0, 0, 0, 1],
              [1, 0, 0, 0, 1],
              [2, 1, 2, 1, 2],
              [2, 9, 2, 9, 3],
              [1, 1, 2, 2, 9]]

five_by_five = [[1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]]


file_name = "Five_by_five.txt"

file = open(file_name, 'w')
for line in five_by_five:
    for index in line:
        if index == "F": file.write("-2" + " ")
        else: file.write(str(index) + " ")
    file.write('\n')
file.write('\n')

for line in five_by_five: print(line)
print ('\n')
print(get_expected_mines(five_by_five))
print ('\n')
exp = get_expected_mines(five_by_five)
treshold = 1.5
pOvershoot = 0
pUndershoot = 0

count = 0
for row in range(len(five_by_five) - 2):
    for col in range(len(five_by_five[0]) - 2):
        if len(get_unk_neighbors([[row + 1, col + 1]], five_by_five)) > 0 and five_by_five[row + 1][col + 1] != -1:
            count += 1
            print ([row + 1, col + 1])
print (count)
heat_maps = [[[0 for i in range(len(five_by_five))] for i in range(len(five_by_five[0]))] for i in range(count)]
for board in heat_maps:
    for line in board: print(line)
    print('\n')
count = 0
for row in range(len(five_by_five) - 2):
    for col in range(len(five_by_five[0]) - 2):
        if len(get_unk_neighbors([[row + 1, col + 1]], five_by_five)) > 0 and five_by_five[row + 1][col + 1] != -1:
            neighbors = get_unk_neighbors([[row + 1, col + 1]], five_by_five)
            for coord in neighbors:
                heat_maps[count][coord[0]][coord[1]] += (five_by_five[row + 1][col + 1]/len(neighbors)) * (1 - pUndershoot - pOvershoot)
                
                for i in range(len(heat_maps[0])):
                    for j in range(len(heat_maps[0][0])):
                        if heat_maps[count][i][j] == 0: heat_maps[count][i][j] = 10**-1
            count += 1    

for board in heat_maps:
    for line in board: print(line)
    print('\n')
'''
count = 0
for row in range(len(five_by_five) - 2):
    for col in range(len(five_by_five[0]) - 2):
        if five_by_five[row + 1][col + 1] > 0:
             neighbors = get_unk_neighbors([[row + 1, col + 1]], five_by_five)
             for coord in neighbors:
                if count == 0:
                    heat_map[coord[0]][coord[1]] = (five_by_five[row + 1][col + 1]/len(neighbors)) * (1 - pUndershoot - pOvershoot)*1000
                    if (five_by_five[row + 1][col + 1]/len(neighbors)) * (1 - pUndershoot - pOvershoot) == 0:
                        heat_map[coord[0]][coord[1]] = 1

                elif (five_by_five[row + 1][col + 1]/len(neighbors)) * (1 - pUndershoot - pOvershoot) == 0:
                    heat_map[coord[0]][coord[1]] *= 1
                else:heat_map[coord[0]][coord[1]] *= (five_by_five[row + 1][col + 1]/len(neighbors)) * (1000 - pUndershoot - pOvershoot)
                count += 1
                #heat_map[coord[0]][coord[1]] += ((five_by_five[row + 1][col + 1] - 1)/len(neighbors)) * pOvershoot
                #heat_map[coord[0]][coord[1]] += ((five_by_five[row + 1][col + 1] + 1)/len(neighbors)) * pUndershoot
'''

heat_map = [[0 for i in range(5)] for i in range(5)]
for board in range(len(heat_maps)):
    for row in range(len(heat_maps[0])):
        for col in range(len(heat_maps[0][0])):
            if board == 0: heat_map[row][col] = heat_maps[board][row][col]
            else: heat_map[row][col] *= heat_maps[board][row][col]
              

for line in heat_map:
    print (line)
print("\n")

sum = 0
for row in heat_map:
    for index in row:
        sum += index
for row in range(len(heat_map)):
    for col in range(len(heat_map[0])):
        heat_map[row][col] = (heat_map[row][col]/sum)
for line in heat_map:
    print (line)
print("\n")
    # mark as mine
max_col = 0
max_row = 0
max_val = 0
for row in range(len(heat_map)):
    for col in range(len(heat_map[0])):
        if heat_map[row][col] > max_val:
            max_col = col
            max_row = row
            max_val = heat_map[row][col]
five_by_five[max_row][max_col] = "F"

    # Create new 5-by-5 with effective values

effective = deepcopy(five_by_five)


for coordinate in get_neighbors([[max_row, max_col]], effective):
    if effective[coordinate[0]][coordinate[1]] >= 1:
        effective[coordinate[0]][coordinate[1]] += -1
effective[max_row][max_col] = "M"

# Sweeping

for row in range(len(five_by_five)):
    for col in range(len(five_by_five[0])):
        if effective[row][col] == 0:
            local = get_unk_neighbors([[row, col]], effective)
            for coord in local:
                effective[coord[0]][coord[1]] = true_board[coord[0]][coord[1]]
                five_by_five[coord[0]][coord[1]] = true_board[coord[0]][coord[1]]




for line in heat_map:
    for index in line:
        file.write(str(index) + " ")
    file.write('\n')
file.close()
print ("Successfully written to file " + file_name)
