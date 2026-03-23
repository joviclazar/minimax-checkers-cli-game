from copy import deepcopy
import moves
import outputGame
import hashlib

hashed_tables = {}

def loading_hash():
    with open('hashed_tables.txt', 'r') as file:
        for line in file:
            line = line.strip()
            key, value_str = line.split(': ', 1)
            value_str_list = value_str.split(",")
            evaluation = value_str_list[0][1:]
            pieces_num = value_str_list[1][:-1]
            hashed_tables[key] = (int(evaluation), int(pieces_num))
def saving_hash(hashed_tables):
    with open('hashed_tables.txt', 'w') as file:
        for key, value in hashed_tables.items():
            file.write(f'{key}: {value}\n')

#COMPTUER IS MINIMIZER, HUMAN IS MAXIMIZER
#MAXIMIZING PLAYER == TRUE  --> HUMAN
#MAXIMIZING PLAYER == FALSE --> COMPTUER

def get_best_move(table, depth, starting_time):
    best_move = None
    best_value = float('inf')
    possible_moves = get_possible_moves(table)
    if possible_moves == []:
        outputGame.table_print(table)
        print(outputGame.colors.GREEN + "VICTORY!" + outputGame.colors.RESET + "\nCongratulations!")
        exit()
    for move in possible_moves:
        board_value= minimax(move, depth, -float('inf'), +float('inf'), True, starting_time)
        if board_value < best_value:
            best_value = board_value
            best_move = move
    outputGame.print_computer_move(table, best_move)
    return best_move

def get_possible_moves(table, maximizing_player = False): #RETURNS TABLES
    tables = []
    if maximizing_player:
        for i in range(len(table)):
            for j in range(len(table[i])):
                figure = table[i][j]
                if figure == "č":
                    possible_moves, possible_captures = moves.check_possible_moves(table, i, j, "č")
                    if possible_moves == [] and possible_captures == []:
                        continue
                    else:
                        possible_captures_separated = []
                        for capture in possible_captures:
                            for capture_move in capture:
                                possible_captures_separated.append(capture_move)
                        figure_position = str(i) + str(j)
                        tables.extend(get_possible_tables(table, figure, figure_position, possible_moves, possible_captures, possible_captures_separated))
                if figure == "Č":
                    possible_moves, possible_captures = moves.check_possible_moves(table, i, j, "Č")
                    if possible_moves == [] and possible_captures == []:
                        continue
                    else:
                        possible_captures_separated = []
                        for capture in possible_captures:
                            for capture_move in capture:
                                possible_captures_separated.append(capture_move)
                        figure_position = str(i) + str(j)
                        tables.extend(get_possible_tables(table, figure, figure_position, possible_moves, possible_captures, possible_captures_separated))
    else:
        for i in range(len(table)):
            for j in range(len(table[i])):
                figure = table[i][j]
                if figure == "Š":
                    possible_moves, possible_captures = moves.check_possible_moves(table, i, j, "Š")
                    if possible_moves == [] and possible_captures == []:
                        continue
                    else:
                        possible_captures_separated = []
                        for capture in possible_captures:
                            for capture_move in capture:
                                possible_captures_separated.append(capture_move)
                        figure_position = str(i) + str(j)
                        tables.extend(get_possible_tables(table, figure, figure_position, possible_moves, possible_captures, possible_captures_separated))
                if figure == "š":
                    possible_moves, possible_captures = moves.check_possible_moves(table, i, j, "š")
                    if possible_moves == [] and possible_captures == []:
                        continue
                    else:
                        possible_captures_separated = []
                        for capture in possible_captures:
                            for capture_move in capture:
                                possible_captures_separated.append(capture_move)
                        figure_position = str(i) + str(j)
                        tables.extend(get_possible_tables(table, figure, figure_position, possible_moves, possible_captures, possible_captures_separated))
    return tables

def get_possible_tables(table, figure, figure_position, possible_moves, possible_captures, possible_captures_separated):
    tables = []
    for possible_move in possible_moves:
        new_table = deepcopy(table)
        move = str(possible_move[0]) + str(possible_move[1])
        moves.move_figure(new_table, figure_position, move, [], [], possible_moves)
        tables.append(new_table)
    for i in possible_captures_separated:
        new_table = deepcopy(table)
        move = str(i[0]) + str(i[1])
        moves.move_figure(new_table, figure_position, move, possible_captures_separated, possible_captures, [])
        tables.append(new_table)
    return tables

def minimax(table, depth, alpha, beta, maximizing_player, starting_time):
    if depth == 0: # or winning_condition(table):
        if hashlib.md5(str(table).encode()).hexdigest() in hashed_tables:
            return hashed_tables[hashlib.md5(str(table).encode()).hexdigest()][0]
        else:
            return evaluate_heuristic(table)[0]

    if maximizing_player:
        max_value = -float('inf')
        for move in get_possible_moves(table, maximizing_player):   #move is actually a table
            eval = minimax(move, depth - 1, alpha, beta, False, starting_time)
            max_value = max(max_value, eval)
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break  # beta cut-off
        return max_value
    else:
        min_value = float('inf')
        for move in get_possible_moves(table):
            eval = minimax(move, depth - 1, alpha, beta, True, starting_time)
            min_value = min(min_value, eval)
            beta = min(beta, min_value)
            if beta <= alpha:
                break  # alpha cut-off
        return min_value

def determine_dynamic_depth(previous_time_move, previous_depth, number_of_pieces):
    if previous_time_move < 1 and previous_depth < 5:
        return previous_depth + 1
    if number_of_pieces < 8 and previous_depth < 6:
        return previous_depth + 1
    if previous_time_move > 2 and previous_depth > 4:
        return previous_depth - 1
    if number_of_pieces > 15 and previous_time_move > 1 and previous_depth > 4:
        return previous_depth - 1
    return previous_depth


def evaluate_heuristic(table):

    table_hash = hashlib.md5(str(table).encode()).hexdigest()

    if table_hash in hashed_tables.keys():
        return hashed_tables.get(table_hash)[0], hashed_tables.get(table_hash)[1]

    blue_num = 0
    red_num = 0
    evaluation = 0

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "č" or table[i][j] == "Č":
                blue_num += 1
                evaluation += 45
                if table[i][j] == "Č":
                    evaluation += 15
                if (2 <= i <= 5) and (2 <= j <= 5):
                    evaluation += 5
            elif table[i][j] == "š" or table[i][j] == "Š":
                red_num += 1
                evaluation -= 45
                if table[i][j] == "Š":
                    evaluation -=15
                #if (2 <= i <= 5) and (2 <= j <= 5):
                #    evaluation -= 5

    all_possible_moves_human = moves.find_all_possible_moves(table, True)
    all_possible_moves_bot = moves.find_all_possible_moves(table, False)

    if blue_num == 0 or all_possible_moves_human == []:
        evaluation = -10000
    elif red_num == 0 or all_possible_moves_bot == []:
        evaluation = 10000



    number_of_pieces = red_num + blue_num
    hashed_tables[hashlib.md5(str(table).encode()).hexdigest()] = (evaluation, number_of_pieces)
    return evaluation, number_of_pieces