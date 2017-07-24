from random import randint
from copy import deepcopy
from random import random
from random import choice


def get_five_by_five(bot_coordinate, board):
    local = get_neighbors(get_neighbors([bot_coordinate], board), board)
    local.sort()
    first = deepcopy(local[0])
    
    scaled_local = [[0, 0] for i in range(len(local))]
    for coord in range(len(local)):
        scaled_local[coord][0] = local[coord][0] - first[0]
        scaled_local[coord][1] = local[coord][1] - first[1]

    max_row = scaled_local[-1][0]
    max_col = scaled_local[-1][1]
    true_max_row = local[-1][0]
    true_max_col = local[-1][1]
    corner = local[0]
    
    five_by_five = [[0 for i in range(max_col + 1)] for i in range(max_row + 1)]
    col = 0
    row = 0
    for coordinate in local:
        try:
            if board[coordinate[0]][coordinate[1]] == "F":
                five_by_five[row][col] = -2
            else: five_by_five[row][col] = int(board[coordinate[0]][coordinate[1]])
        except:
            five_by_five[row][col] = -1
        col += 1
        if col == max_col + 1:
            col = 0
            row += 1
    
    if len(five_by_five) == 4:
        if true_max_row == 3:
            five_by_five.insert(0, [-3 for i in range(max_col + 1)])
        else: five_by_five.append([-3 for i in range(max_col + 1)])

    elif len(five_by_five) == 3:
        if true_max_row == 2:
            five_by_five.insert(0, [-3 for i in range(max_col + 1)])
            five_by_five.insert(0, [-3 for i in range(max_col + 1)])
        else:
            five_by_five.append([-3 for i in range(max_col + 1)])
            five_by_five.append([-3 for i in range(max_col + 1)])
    if len(five_by_five[0]) == 4:
        if true_max_col == 3:
            for row in range(len(five_by_five)):
                five_by_five[row].insert(0, -3)
        else:
            for row in range(len(five_by_five)):
                five_by_five[row].append(-3)
    elif len(five_by_five[0]) == 3:
        if true_max_col == 2:
            for row in range(len(five_by_five)):
                five_by_five[row].insert(0, -3)
                five_by_five[row].insert(0, -3)
        else:
            for row in range(len(five_by_five)):
                five_by_five[row].append(-3)
                five_by_five[row].append(-3)
    return [five_by_five, corner]


def get_neighbors(coordinates, board):
    neighbors = []
    for coordinate in coordinates:
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0] + 1, coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1] + 1])
        if coordinate[0] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1]])
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0] + 1, coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1] - 1])
        if coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0], coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] + 1])
        if coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0], coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] - 1])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0] - 1, coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1] + 1])
        if coordinate[0] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1]])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0] - 1, coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1] - 1])
    return neighbors

def get_dir_neighbors(coordinates, board):
    neighbors = []
    for coordinate in coordinates:
        if [coordinate[0] - 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] - 1, coordinate[1]])
       
        if [coordinate[0], coordinate[1] - 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] - 1])
        
        if [coordinate[0] + 1, coordinate[1]] not in neighbors: neighbors.append([coordinate[0] + 1, coordinate[1]])
        
        if [coordinate[0], coordinate[1] + 1] not in neighbors: neighbors.append([coordinate[0], coordinate[1] + 1])
    return neighbors

        
def get_unk_neighbors(coordinates, board):
    neighbors = []
    for coordinate in coordinates:
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0] + 1, coordinate[1] + 1] not in neighbors and (board[coordinate[0] + 1][coordinate[1] + 1] == -1 or board[coordinate[0] + 1][coordinate[1] + 1] == "*"): neighbors.append([coordinate[0] + 1, coordinate[1] + 1])
        if coordinate[0] + 1 in range(len(board)):
            if [coordinate[0] + 1, coordinate[1]] not in neighbors and (board[coordinate[0] + 1][coordinate[1]] == -1 or board[coordinate[0] + 1][coordinate[1]] == "*"): neighbors.append([coordinate[0] + 1, coordinate[1]])
        if coordinate[0] + 1 in range(len(board)) and coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0] + 1, coordinate[1] - 1] not in neighbors and (board[coordinate[0] + 1][coordinate[1] - 1] == -1 or board[coordinate[0] + 1][coordinate[1] - 1] == "*"): neighbors.append([coordinate[0] + 1, coordinate[1] - 1])
        if coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0], coordinate[1] + 1] not in neighbors and (board[coordinate[0]][coordinate[1] + 1] == -1 or board[coordinate[0]][coordinate[1] + 1] == "*"): neighbors.append([coordinate[0], coordinate[1] + 1])
        if coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0], coordinate[1] - 1] not in neighbors and (board[coordinate[0]][coordinate[1] - 1] == -1 or board[coordinate[0]][coordinate[1] - 1] == "*"): neighbors.append([coordinate[0], coordinate[1] - 1])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] + 1 in range(len(board[0])):
            if [coordinate[0] - 1, coordinate[1] + 1] not in neighbors and (board[coordinate[0] - 1][coordinate[1] + 1] == -1 or board[coordinate[0] - 1][coordinate[1] + 1] == "*"): neighbors.append([coordinate[0] - 1, coordinate[1] + 1])
        if coordinate[0] - 1 in range(len(board)):
            if [coordinate[0] - 1, coordinate[1]] not in neighbors and (board[coordinate[0] - 1][coordinate[1]] == -1 or board[coordinate[0] - 1][coordinate[1]] == "*"): neighbors.append([coordinate[0] - 1, coordinate[1]])
        if coordinate[0] - 1 in range(len(board)) and coordinate[1] - 1 in range(len(board[0])):
            if [coordinate[0] - 1, coordinate[1] - 1] not in neighbors and (board[coordinate[0] - 1][coordinate[1] - 1] == -1 or board[coordinate[0] - 1][coordinate[1] - 1] == "*"): neighbors.append([coordinate[0] - 1, coordinate[1] - 1])
    return neighbors

def write_to_file(five_by_five, heat_map, player_board):
    file_name = "Five_by_five.txt"

    file = open(file_name, 'w')
    for line in five_by_five:
        for index in line:
            if index == "F": file.write("-2" + " ")
            else: file.write(str(index) + " ")
        file.write('\n')
    file.write('\n')
    for line in heat_map:
        for index in line:
            file.write(str(index) + " ")
        file.write('\n')
    file.write('\n')
    for line in player_board:
        for index in line:
            if index == "F": file.write("-2 ")
            elif index == "*": file.write("-1 ")
            else: file.write(str(index) + " ")
        file.write("\n")
    file.close()
    print ("Successfully written to file " + file_name)

    
def expand(coordinate, board):
    coordinates = get_neighbors([coordinate], board)
    for index in coordinates:
        board[index[0]][index[1]] = str(defined_board[index[0]][index[1]])

def fill_zeroes(board, zeroes):
    coords = []
    change = zeroes
    
    while True:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "0" and [row, col] not in zeroes:
                    coords.append([row, col])
                    zeroes.append([row, col])
        change.append(zeroes)
        for coord in coords:
            expand(coord, board)
        if change[-2] == change[-1]: break    
    return zeroes

def get_heat_map(five_by_five, bot_coordinate, threshold):
    heat_map = [[0 for i in range(len(five_by_five))] for i in range(len(five_by_five[0]))]
    effective = deepcopy(five_by_five)

    for line in range(len(effective)):
            for index in range(len(effective[0])):
                if effective[line][index] == -2:
                    for coordinate in get_neighbors([[line, index]], effective):
                        if effective[coordinate[0]][coordinate[1]] > 0:
                            effective[coordinate[0]][coordinate[1]] -= 1
                    
    
    for row in range(len(effective) - 2):
        for col in range(len(effective[0]) - 2):
            if effective[row + 1][col + 1] > 0:
                 neighbors = get_unk_neighbors([[row + 1, col + 1]], effective)
                 for coord in neighbors:
                    heat_map[coord[0]][coord[1]] += (effective[row + 1][col + 1]/len(neighbors)) 
    sum = 0
    for line in heat_map:
        for index in line:
            sum += index
    if sum != 0:
        for row in range(len(heat_map)):
            for col in range(len(heat_map[0])):
                heat_map[row][col] /= sum
        threshold /= sum
    #print (threshold)
    #print('\n')
    return [heat_map, threshold]

def mark_mine(five_by_five, heat_map, threshold, inv_heat_map, bot_coordinate, guess):
    values = []
    success = 1
    for row in range(len(heat_map)):
        for col in range(len(heat_map[0])):
            values.append([heat_map[row][col], row, col])
    values.sort()
    values.reverse()

    n = 0
    if inv_heat_map[bot_coordinate[0]][bot_coordinate[1]] >= 10:
        while(values[n][0] >= 0.1):
            #print ("Iteration " + str(n + 1) + "\n")
            five_by_five[values[n][1]][values[n][2]] = -2
            if contradiction(five_by_five):
                print("There was a contradiction in the algorithm\n")
                five_by_five[values[n][1]][values[n][2]] = -1
                n += 1
            else:
                success = 0
                break
    else:        
        while(values[n][0] >= threshold):
            print ("Iteration " + str(n + 1) + "\n")
            five_by_five[values[n][1]][values[n][2]] = -2
            if contradiction(five_by_five):
                print("There was a contradiction in the algorithm\n")
                five_by_five[values[n][1]][values[n][2]] = -1
                n += 1
            else:
                success = 0
            break
    effective = deepcopy(five_by_five)
    if not guess:
        if success == 1:
            inv_heat_map[bot_coordinate[0]][bot_coordinate[1]] += 1
        else:
            inv_heat_map[bot_coordinate[0]][bot_coordinate[1]] = 0
            neighbors = get_neighbors([bot_coordinate], inv_heat_map)
            for coord in neighbors:
                if inv_heat_map[coord[0]][coord[1]] > 1: inv_heat_map[coord[0]][coord[1]] += -2
                elif inv_heat_map[coord[0]][coord[1]] == 1: inv_heat_map[coord[0]][coord[1]] = 0

    if five_by_five[values[n][1]][values[n][2]] == -2:
        for coordinate in get_neighbors([[values[n][1], values[n][2]]], effective):
            if effective[coordinate[0]][coordinate[1]] >= 1:
                effective[coordinate[0]][coordinate[1]] += -1
        effective[values[n][1]][values[n][2]] = "M"
    return [five_by_five, effective, inv_heat_map]

def sweeping(five_by_five, effective, true_board):
    for row in range(len(five_by_five)):
        for col in range(len(five_by_five[0])):
            if effective[row][col] == 0:
                local = get_unk_neighbors([[row, col]], effective)
                for coord in local:
                    effective[coord[0]][coord[1]] = true_board[coord[0]][coord[1]]
                    five_by_five[coord[0]][coord[1]] = true_board[coord[0]][coord[1]]
    return five_by_five

def transform_board(game_board):
    location_board = [[" " for i in range(len(game_board))] for i in range(len(game_board[0]))]
    for row in range(len(game_board)):
        for col in range(len(game_board[0])):
            if game_board[row][col] == "*" or game_board[row][col] == "F":
                location_board[row][col] = 1
            else: location_board[row][col] = 0
    return location_board

def get_effective(five_by_five):
    effective = deepcopy(five_by_five)
    for row in range(len(five_by_five)):
        for col in range(len(five_by_five[0])):
            if five_by_five[row][col] == -2:
                for neighbor in get_neighbors([[row, col]], five_by_five):
                    if effective[neighbor[0]][neighbor[1]] >= 1:
                        effective[neighbor[0]][neighbor[1]] += -1
    return effective

def get_heuristic(board, bot_coordinate, solving_heuristic):
    coordinates = get_neighbors(get_neighbors([bot_coordinate]))
    for coordinate in coordinates:
        try:
            solving_heuristic[bot_coordinate[0]][bot_coordinate[1]] += int(board[coordinate[0]][coordinate[1]])
        except:
            solving_heuristic[bot_coordinate[0]][bot_coordinate[1]] += -1
    return solving_heuristic

def contradiction(five_by_five):
    truth = []
    flags = []
    effective = deepcopy(five_by_five)
    for row in range(len(five_by_five)):
        for col in range(len(five_by_five[0])):
            if five_by_five[row][col] == -2:
                flags.append([row, col])
    for flag in flags:
        for coordinate in get_neighbors([flag], effective):
            try:
                if effective[coordinate[0]][coordinate[1]] >= 0:
                    effective[coordinate[0]][coordinate[1]] += -1
                    if effective[coordinate[0]][coordinate[1]] < 0: return True
            except: pass
        effective[flag[0]][flag[1]] = "M"

        

    for flag in flags:
        for coordinate in get_neighbors([flag], effective):
            if effective[coordinate[0]][coordinate[1]] == 0:
                unknowns = get_unk_neighbors([coordinate], effective)
                for unknown in unknowns:
                    effective[unknown[0]][unknown[1]] = "Q"
        for coordinate in get_neighbors([flag], five_by_five):
            if five_by_five[coordinate[0]][coordinate[1]] > 0:
                unknowns = get_unk_neighbors([coordinate], effective)
                if coordinate[0] == 0 or coordinate[0] == 4 or coordinate[1] == 0 or coordinate[1] == 4: continue
                else: truth.append(effective[coordinate[0]][coordinate[1]] > len(unknowns))
    if True in truth: return True
    else: return False


def reasonable_location(board, bot_coordinate):
    return len(get_unk_neighbors([bot_coordinate], board)) >= 1
        

    
def move_randomly(bot_coordinate, safe_board, player_board, num_moves):
    moves = []
    while(True):
        move = randint(0, 3)
        if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
            if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                print (delta_name[move])
                print ('\n')
                moves.append(move)
                num_moves += 1
                break
    while(not reasonable_location(player_board, bot_coordinate)):
        while(True):
            move = randint(0, 3)
            if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
                if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                    bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                    bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                    print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                    print (delta_name[move])
                    print ('\n')
                    num_moves += 1
                    moves.append(move)
                    break
    write_moves(moves)
    return [bot_coordinate, num_moves]

def insert_board(five_by_five, player_board, corner):
    i = 0
    j = 0
    for row in range(len(five_by_five)):
        for col in range(len(five_by_five[0])):
            if five_by_five[row][col] == -3 and col == 4 and five_by_five[row][0] == -3: continue
            elif five_by_five[row][col] == -3: pass
            elif five_by_five[row][col] == -2:
                player_board[i + corner[0]][j + corner[1]] = "F"
                j += 1
            elif five_by_five[row][col] == -1: j += 1
            else:
                player_board[i + corner[0]][j + corner[1]] = str(five_by_five[row][col])
                j += 1
            if col == 4:
                j = 0
                i += 1
    return player_board

def completed(player_board):
    count = 0
    for line in player_board:
        for index in line:
            if index == "*": count += 1
    return count == 0

def lost(player_board):
    lost = False
    for line in player_board:
        for index in line:
            if index == "9":
                lost = True
    return lost


def write_moves(bot_moves):

    for move in bot_moves:
        animation.write(str(move) + " ")
    animation.write('\n')
    animation.write("66")
    animation.write('\n')

def write_five_by_five(five_by_five):
    for row in five_by_five:
        for col in row:
            animation.write(str(col) + " ")
        animation.write('\n')
    animation.write('\n')

def generate_board(bot_coordinate, n, mine_number):
    board = [[0 for i in range(n)] for i in range(n)]
    neighbors = get_neighbors([bot_coordinate], board)
    while mine_number > 0:
        mine_row = randint(0, n - 1)
        mine_col = randint(0, n - 1)
        if [mine_row, mine_col] in neighbors or [mine_row, mine_col] == bot_coordinate or board[mine_row][mine_col] == 9:
            continue
        else:
            board[mine_row][mine_col] = 9
            mine_number += -1
    # Get values
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 9:
                for coord in get_neighbors([[row, col]], board):
                    if board[coord[0]][coord[1]] != 9:
                        board[coord[0]][coord[1]] += 1
    board = faulty_sensors(board, .3, bot_coordinate)
    return board

def faulty_sensors(board, error, bot_coordinate):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if [row, col] == bot_coordinate: continue
            if board[row][col] != 9:
                if random() <= error:
                    board[row][col] += 1
    return board
                    

def check_quadrants(player_board, bot_coordinate):
    max_unk = [0, 0]
    unk = 0
    for row in range(bot_coordinate[0]):
        for col in range(bot_coordinate[1]):
            if player_board[row][col] == "*": unk += 1
    if unk > max_unk[0]:
        max_unk[0] = unk
        max_unk[1] = 1
        unk = 0
    for row in range(bot_coordinate[0]):
        for col in range(bot_coordinate[1] + 1, len(player_board[0])):
            if player_board[row][col] == "*": unk += 1
    if unk > max_unk[0]:
        max_unk[0] = unk
        max_unk[1] = 2
        unk = 0
    for row in range(bot_coordinate[0] + 1, len(player_board)):
        for col in range(bot_coordinate[1]):
            if player_board[row][col] == "*": unk += 1
    if unk > max_unk[0]:
        max_unk[0] = unk
        max_unk[1] = 3
        unk = 0
    for row in range(bot_coordinate[0] + 1, len(player_board)):
        for col in range(bot_coordinate[1] + 1, len(player_board[0])):
            if player_board[row][col] == "*": unk += 1
    if unk > max_unk[0]:
        max_unk[0] = unk
        max_unk[1] = 4
        unk = 0
    return max_unk[1]
        
def move_smartly(bot_coordinate, safe_board, player_board, num_moves, inv_heat_map):
    moves = []
    delta = [[-1, 0 ], # go up
             [ 0, -1], # go left
             [ 1, 0 ], # go down
             [ 0, 1 ]] # go right
    delta_num = [0, 1, 2, 3]
    neighbors = get_dir_neighbors([bot_coordinate], player_board)
    count = 0
    storage = []
    probs = [0, 0, 0, 0]
    for coord in range(len(neighbors)):
        try:
            if inv_heat_map[neighbors[coord][0]][neighbors[coord][1]] != 0:
                count += 1
                storage.append(coord)
        except: pass
    if count == 1:
        probs[storage[0]] = .25/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
        for i in range(len(probs)):
            if probs[i] == 0: probs[i] = (1 - probs[storage[0]]) / 3
        
            
    elif count == 2:
        prob1 = .25/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
        prob2 = .25/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
        probs[storage[0]] = prob1
        probs[storage[1]] = prob2
        for i in range(len(probs)):
            if probs[i] == 0: probs[i] = (1 - prob1 - prob2) / 2

    elif count == 3:
        prob1 = .25/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
        prob2 = .25/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
        prob3 = .25/( 1 + inv_heat_map[neighbors[storage[2]][0]][neighbors[storage[2]][1]])
        probs[storage[0]] = prob1
        probs[storage[1]] = prob2
        probs[storage[2]] = prob3
        for i in range(len(probs)):
            if probs[i] == 0: probs[i] = (1 - prob1 - prob2 - prob3)
    elif count == 4:
        prob1 = .25/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
        prob2 = .25/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
        prob3 = .25/( 1 + inv_heat_map[neighbors[storage[2]][0]][neighbors[storage[2]][1]])
        prob4 = .25/( 1 + inv_heat_map[neighbors[storage[3]][0]][neighbors[storage[3]][1]])
        prob1 = prob1 / (prob1 + prob2 + prob3 + prob4)
        prob2 = prob2 / (prob1 + prob2 + prob3 + prob4)
        prob3 = prob3 / (prob1 + prob2 + prob3 + prob4)
        prob4 = prob4 / (prob1 + prob2 + prob3 + prob4)
        probs[storage[0]] = prob1
        probs[storage[1]] = prob2
        probs[storage[2]] = prob3
        probs[storage[3]] = prob4
    else: probs = [.25, .25, .25, .25]
    #print (probs)
    
    while(True):
            
        move = random()
        if move <= probs[0]: move = 0
        elif move > probs[0] and move <= probs[0] + probs[1]: move = 1
        elif move > probs[0] + probs[1] and move <= probs[0] + probs[1] + probs[2]: move = 2
        else: move = 3
        #print(move)
        #print('\n')
        if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
            if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                #print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                #print ('\n')
                moves.append(move)
                num_moves += 1
                break
    while(not reasonable_location(player_board, bot_coordinate)):
        quad = check_quadrants(player_board, bot_coordinate)
        neighbors = get_dir_neighbors([bot_coordinate], player_board)
        if quad == 2:
            delta[3], delta[1] = delta[1], delta[3]
            delta_num[3], delta_num[1] = delta_num[1], delta_num[3]
            neighbors[3], neighbors[1] = neighbors[1], neighbors[3]
        elif quad == 3:
            delta[0], delta[2] = delta[2], delta[0]
            delta_num[0], delta_num[2] = delta_num[2], delta_num[0]
            neighbors[0], neighbors[2] = neighbors[2], neighbors[0]
        elif quad == 4:
            delta[0], delta[2] = delta[2], delta[0]
            delta[3], delta[1] = delta[1], delta[3]
            delta_num[3], delta_num[1] = delta_num[1], delta_num[3]
            delta_num[0], delta_num[2] = delta_num[2], delta_num[0]
            neighbors[3], neighbors[1] = neighbors[1], neighbors[3]
            neighbors[0], neighbors[2] = neighbors[2], neighbors[0]

        count = 0
        storage = []
        probs = [0, 0, 0, 0]
        for coord in range(len(neighbors)):
            try:
                if inv_heat_map[neighbors[coord][0]][neighbors[coord][1]] != 0:
                    count += 1
                    storage.append(coord)
            except: pass
        if count == 1:
            a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
            b = .1/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])

            if storage[0] == 0 or storage[0] == 1:
                probs[storage[0]] = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                for i in range(len(probs)):
                    if probs[i] == 0 and (i == 0 or i == 1):
                        probs[i] = (2 - 2*a) / 3
                    elif probs[i] == 0:
                        probs[i] = (1 - a) / 6
            else: 
                probs[storage[0]] = .1/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                for i in range(len(probs)):
                    if probs[i] == 0 and (i == 0 or i == 1):
                        probs[i] = (4 - 4*b) / 9
                    elif probs[i] == 0:
                        probs[i] = (1 - b) / 9
        elif count == 2:

            if storage[0] == 0 and storage[1] == 1:
                a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                b = .4/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])

                probs[storage[0]] = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                probs[storage[1]] = .4/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                for i in range(len(probs)):
                    if probs[i] == 0:
                        probs[i] = (1 - a - b) / 2
            elif storage[0] == 2 and storage[1] == 3:
                a = .1/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                b = .1/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                probs[storage[0]] = .1/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                probs[storage[1]] = .1/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                for i in range(len(probs)):
                    if probs[i] == 0:
                        probs[i] = (1 - a - b) / 2
            elif storage[0] == 0:
                a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                b = .1/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                probs[storage[0]] = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                probs[storage[1]] = .1/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                for i in range(len(probs)):
                    if probs[i] == 0 and (i == 0 or i == 1):
                        probs[i] = (4 - 4*a - 4*b) / 5
                    elif probs[i] == 0:
                        probs[i] = (1 - a - b) / 5
        elif count == 3:
            if storage[0] == 0 and storage[1] == 1:
                a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                b = .4/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                c = .1/( 1 + inv_heat_map[neighbors[storage[2]][0]][neighbors[storage[2]][1]])
                probs[storage[0]] = a
                probs[storage[1]] = b
                probs[storage[2]] = c
                for i in range(len(probs)):
                    if probs[i] == 0:
                        probs[i] = 1 - a - b - c
            else:
                a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
                b = .1/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
                c = .1/( 1 + inv_heat_map[neighbors[storage[2]][0]][neighbors[storage[2]][1]])
                probs[storage[0]] = a
                probs[storage[1]] = b
                probs[storage[2]] = c
                for i in range(len(probs)):
                    if probs[i] == 0:
                        probs[i] = 1 - a - b - c
        elif count == 4:
            a = .4/( 1 + inv_heat_map[neighbors[storage[0]][0]][neighbors[storage[0]][1]])
            b = .4/( 1 + inv_heat_map[neighbors[storage[1]][0]][neighbors[storage[1]][1]])
            c = .1/( 1 + inv_heat_map[neighbors[storage[2]][0]][neighbors[storage[2]][1]])
            d = .1/( 1 + inv_heat_map[neighbors[storage[3]][0]][neighbors[storage[3]][1]])
            probs[storage[0]] = a / (a + b + c + d)
            probs[storage[1]] = b / (a + b + c + d)
            probs[storage[2]] = c / (a + b + c + d)
            probs[storage[3]] = d / (a + b + c + d)

        else: probs = [.4, .4, .1, .1]
        #print(probs)
        while(True):
            move = random()
            if move <= probs[0]: move = 0
            elif move > probs[0] and move <= probs[0] + probs[1]: move = 1
            elif move > probs[0] + probs[1] and move <= probs[0] + probs[1] + probs[2]: move = 2
            else: move = 3
            #print(move)
            #print('\n')
            if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
                if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                    bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                    bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                    #print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                    # print (delta_name[move])
                    #print ('\n')
                    num_moves += 1
                    moves.append(delta_num[move])
                    break
        delta = [[-1, 0 ], # go up
                 [ 0, -1], # go left
                 [ 1, 0 ], # go down
                 [ 0, 1 ]] # go right
        delta_num = [0, 1, 2, 3]
    write_moves(moves)
    return [bot_coordinate, num_moves]
'''
def exceeded_checks(guess_board):
    for row in range(len(guess_board)):
        for col in range(len(guess_board[0])):
            if guess_board[row][col][1] >= 5 and guess_board[row][col][0] == 1:
                return True
    return False

def new_target(guess_board):
    targets = []
    for row in range(len(guess_board)):
        for col in range(len(guess_board[0])):
            if guess_board[row][col][0] == 1 and guess_board[row][col][1] == 0:
                targets.append([row, col])
    if len(targets) == 0:
        max_row = 0
        max_col = 0
        max_val = 0
        for row in guess_board:
            for index in row:
                if index[0] == 1 and index[2] > max_val:
                    max_val = index[2]
                    max_row = row
                    max_col = col
                col += 1
                if col == len(guess_board[0]): col = 0
            row += 1
        return [max_row, max_col]
    decision = randint(0, len(targets) - 1)
    return targets[decision]

def move_to_target(bot_coordinate, safe_board, player_board, num_moves, target):
    moves = []
    delta = [[-1, 0 ], # go up
             [ 0, -1], # go left
             [ 1, 0 ], # go down
             [ 0, 1 ]] # go right
    delta_num = [0, 1, 2, 3]
    print ("hi")
    if target[0] > bot_coordinate[0]:
        delta[0], delta[2] = delta[2], delta[0]
        delta_num[0], delta_num[2] = delta_num[2], delta_num[0]
    if target[1] > bot_coordinate[1]:
        delta[1], delta[3] = delta[3], delta[1]
        delta_num[1], delta_num[3] = delta_num[3], delta_num[1]
    while(True):
        move = random()
        if move <= .4: move = 0
        elif move > .4 and move <= .8: move = 1
        elif move > .8 and move <= .9: move = 2
        else: move = 3
        if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
            if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                print (delta_name[move])
                print ('\n')
                num_moves += 1
                moves.append(delta_num[move])
                break
        delta = [[-1, 0 ], # go up
                 [ 0, -1], # go left
                 [ 1, 0 ], # go down
                 [ 0, 1 ]] # go right
        delta_num = [0, 1, 2, 3]
    
    while(not reasonable_location(player_board, bot_coordinate)):
        if target[0] > bot_coordinate[0]:
            delta[0], delta[2] = delta[2], delta[0]
            delta_num[0], delta_num[2] = delta_num[2], delta_num[0]
        if target[1] > bot_coordinate[1]:
            delta[1], delta[3] = delta[3], delta[1]
            delta_num[1], delta_num[3] = delta_num[3], delta_num[1]
        while(True):
            move = random()
            if move <= .4: move = 0
            elif move > .4 and move <= .8: move = 1
            elif move > .8 and move <= .9: move = 2
            else: move = 3
            if bot_coordinate[0] + delta[move][0] in range(len(safe_board)) and bot_coordinate[1] + delta[move][1] in range(len(safe_board[0])):
                if safe_board[bot_coordinate[0] + delta[move][0]][bot_coordinate[1] + delta[move][1]] != 1:
                    bot_coordinate[0] = bot_coordinate[0] + delta[move][0]
                    bot_coordinate[1] = bot_coordinate[1] + delta[move][1]
                    #print ("Bot coordinate row = " + str(bot_coordinate[0]) + " col = " + str(bot_coordinate[1]))
                    # print (delta_name[move])
                    #print ('\n')
                    num_moves += 1
                    moves.append(delta_num[move])
                    break
        delta = [[-1, 0 ], # go up
                 [ 0, -1], # go left
                 [ 1, 0 ], # go down
                 [ 0, 1 ]] # go right
        delta_num = [0, 1, 2, 3]
    write_moves(moves)
    return [bot_coordinate, num_moves]
  '''  

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

num_moves = 0
'''
defined_board = [[1, 1, 1, 9, 2, 1, 0, 1, 9],
                 [9, 1, 1, 2, 9, 1, 0, 2, 2],
                 [2, 2, 0, 1, 1, 1, 0, 1, 9],
                 [9, 1, 0, 0, 0, 0, 1, 2, 2],
                 [1, 1, 0, 0, 0, 0, 1, 9, 2],
                 [0, 0, 0, 1, 1, 1, 1, 3, 9],
                 [0, 0, 0, 1, 9, 1, 0, 2, 9],
                 [0, 0, 0, 1, 1, 1, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''
'''
defined_board = [[0, 1, 2, 3, 9, 1, 0, 0, 0],
[0, 1, 9, 9, 3, 1, 0, 0, 0],
[0, 1, 3, 9, 2, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 2, 9, 2, 0],
[1, 1, 2, 9, 1, 3, 9, 4, 1],
[1, 9, 2, 1, 1, 2, 9, 3, 9]]
'''                
                 
'''
[1, 2, 2, 9, 2, 9, 1, 1, 1]
[9, 2, 9, 2, 2, 1, 1, 1, 9]
[1, 2, 1, 1, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 1]
[1, 1, 1, 0, 0, 0, 0, 1, 9]
[1, 9, 1, 0, 0, 0, 0, 1, 1]
[1, 1, 1, 0, 1, 1, 2, 1, 1]
[0, 0, 1, 1, 2, 9, 2, 9, 1]
[0, 0, 1, 9, 2, 1, 2, 1, 1]
'''
'''
'''                
'''
defined_board = [[1, 1, 0, 1, 9, 1, 0, 0, 0, 0, 1, 9, 1, 0, 0],
[9, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 2, 9, 1, 0, 0, 1, 1, 2, 1, 2, 9],
[0, 0, 0, 1, 9, 2, 1, 0, 0, 2, 9, 3, 9, 3, 2],
[1, 2, 3, 3, 2, 1, 1, 1, 1, 2, 9, 4, 2, 3, 9],
[2, 9, 9, 9, 3, 1, 2, 9, 2, 2, 2, 2, 9, 2, 1],
[3, 9, 9, 9, 3, 9, 2, 1, 2, 9, 1, 1, 2, 2, 1],
[9, 4, 3, 2, 2, 1, 1, 0, 1, 1, 1, 1, 2, 9, 1],
[9, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 9, 2, 1],
[1, 1, 0, 1, 9, 1, 1, 9, 1, 2, 9, 3, 1, 1, 0],
[0, 1, 1, 3, 2, 3, 2, 2, 1, 2, 9, 3, 1, 1, 0],
[0, 1, 9, 2, 9, 2, 9, 2, 1, 1, 1, 2, 9, 2, 1],
[0, 1, 1, 2, 1, 2, 2, 9, 1, 0, 0, 1, 3, 9, 2],
[0, 1, 1, 1, 1, 1, 3, 2, 2, 0, 0, 0, 3, 9, 4],
[0, 1, 9, 1, 1, 9, 2, 9, 1, 0, 0, 0, 2, 9, 9]]
'''

j = input("How large of a grid? nxn ")
j = int(j)
mine_number = input("How many mines? ")
mine_number = int(mine_number)


first_click = int(j/2)
zeroes = []
player_board = [["*" for i in range(j)] for i in range(j)]
'''
guess_board = [[[0, 0, 0] for i in range(j)] for i in range(j)]
progress = False
guess = False
'''

inv_heat_map = [[0 for i in range(j)] for i in range(j)]

# Expand Board #

bot_coordinate = [first_click, first_click]

defined_board = generate_board(bot_coordinate, j, mine_number)
guess = False
for line in defined_board:
    print (line)
print ('\n')

player_board[first_click][first_click] = str(defined_board[first_click][first_click])


zeroes = fill_zeroes(player_board, zeroes)

for line in player_board:
    print(line)
print('\n')

animation_file = "animation.txt"

animation = open(animation_file, 'w')
for line in player_board:
    for index in line:
        if index == "*": animation.write("-1 ")
        else: animation.write(index + " ")
    animation.write("\n")
animation.write("\n")

animation.close()


safe_board = transform_board(player_board)
#for line in safe_board:
#    print (line)
#print ('\n')

check = []

for row in range(len(safe_board)):
    for col in range(len(safe_board[0])):
        if safe_board[row][col] == 0: check.append([row, col])
'''
solving_heuristic = [[0 for i in range(9)] for i in range(9)]

for coordinate in check:
    solving_heuristic = get_heuristic(player_board, coordinate, solving_heuristic)
for line in solving_heuristic: print (line)
'''
# get 5-by-5 at location
count1 = 0
count2 = 0
anim_num = 1

while(not completed(player_board)):
    threshold = 1.2
    animation_file = "animation" + str(anim_num) + ".txt"
    #inv_map_file = "inv_map" + str(anim_num) + ".txt"

    #map_file = open(inv_map_file, 'w')

    animation = open(animation_file, 'w')
  #  quad = check_quadrants(player_board)
    '''
    for line in inv_heat_map:
        for index in line:
            if index > 0: count1 += 1
    for line in player_board:
        for index in line:
            if index == "*": count2 += 1
    if count1 >= count2:
        guess = True
        print ('hi')
        for row in range(len(inv_heat_map)):
            for col in range(len(inv_heat_map[0])):
                inv_heat_map[row][col] = 0
    count1 = 0
    count2 = 0
    '''
    '''
    if exceeded_checks(guess_board)
        print ("Visited more than 5 times")
        target = new_target(guess_board)
        print (target)
        if guess_board[target[0]][target[1]][1] != 0: guess = True
        [bot_coordinate, num_moves] = move_to_target(bot_coordinate, safe_board, player_board, num_moves, target)        
    else
    '''
    #for line in player_board:
     #   print(line)
    #print('\n')
    [bot_coordinate, num_moves] = move_smartly(bot_coordinate, safe_board, player_board, num_moves, inv_heat_map)
    [five_by_five, corner] = get_five_by_five(bot_coordinate, player_board)
    #guess_board[bot_coordinate[0]][bot_coordinate[1]][1] += 1
    #for line in five_by_five: print (line)
    #print ('\n')
    write_five_by_five(five_by_five)
    [true_board, corner] = get_five_by_five(bot_coordinate, defined_board)
    if sweeping(five_by_five, get_effective(five_by_five), true_board) != five_by_five:
        five_by_five = sweeping(five_by_five, get_effective(five_by_five), true_board)
        player_board = insert_board(five_by_five, player_board, corner)
        continue
    [heat_map, threshold] = get_heat_map(five_by_five, bot_coordinate, threshold)
    write_five_by_five(heat_map)
    #if guess and bot_coordinate == target:
        #[five_by_five, effective, progress] = mark_mine(five_by_five, heat_map, 0, progress)
    if guess: [five_by_five, effective, inv_heat_map] = mark_mine(five_by_five, heat_map, 0.01, inv_heat_map, bot_coordinate, guess)
    else: [five_by_five, effective, inv_heat_map] = mark_mine(five_by_five, heat_map, threshold, inv_heat_map, bot_coordinate, guess)
    five_by_five = sweeping(five_by_five, effective, true_board)
    write_five_by_five(five_by_five)

    player_board = insert_board(five_by_five, player_board, corner)
    if lost(player_board):
        print ("Oh no, I hit a mine!")
        animation.close()
        break
    '''if progress:
        for row in range(len(guess_board)):
            for col in range(len(guess_board[0])):
                if guess_board[row][col][1] > 0:
                    guess_board[row][col][1] += -1
    
        for row in range(len(player_board)):
            for col in range(len(player_board[0])):
                if player_board[row][col] != "*" and player_board[row][col] != "0":
                    if len(get_unk_neighbors([[row, col]], player_board)) > 0:
                        guess_board[row][col][0] = 1
                    else: guess_board[row][col] = [0, 0, 0]
    
    progress = False
    guess = False
    for line in guess_board:
        print (line)
    print ('\n')
    '''
    '''
    for row in range(len(inv_heat_map)):
        for col in range(len(inv_heat_map)):
            if
    '''
    for line in player_board:
        for index in line:
            if index == "*": animation.write("-1 ")
            elif index == "F": animation.write("-2 ")
            else: animation.write(index + " ")
        animation.write("\n")
    animation.write("\n")
    safe_board = transform_board(player_board)
    animation.close()


    '''
    for line in inv_heat_map:
        for index in line:
            map_file.write(str(index) + " ")
        map_file.write('\n')
    map_file.close()

    '''
    anim_num += 1

'''
bot_coordinate = defined_movement(bot_coordinate, safe_board, player_board, moves)
[five_by_five, corner] = get_five_by_five(bot_coordinate, player_board)
write_five_by_five(five_by_five)
[true_board, corner] = get_five_by_five(bot_coordinate, defined_board)
heat_map = get_heat_map(five_by_five)
write_five_by_five(heat_map)
[five_by_five, effective] = mark_mine(five_by_five, heat_map, threshold)

five_by_five = sweeping(five_by_five, effective, true_board)
write_five_by_five(five_by_five)

player_board = insert_board(five_by_five, player_board, corner)

for line in player_board:
    for index in line:
        if index == "*": animation.write("-1 ")
        elif index == "F": animation.write("-2 ")
        else: animation.write(index + " ")
    animation.write("\n")
animation.write("\n")
animation.close()

print("Animation file successfully written")
'''
# write_to_file(five_by_five, heat_map, player_board)
animation.close()


print("Number of moves: " + str(num_moves))
print ("Number of files: " + str(anim_num))
'''file = open('inv_map.txt', 'w')
for line in inv_heat_map:
    for index in line:
        file.write(str(index) + " ")
    file.write('\n')
file.close()
'''
