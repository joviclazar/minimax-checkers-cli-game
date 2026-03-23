

def check_possible_moves(table, row_figure, column_figure, figure):
    valid_moves = []
    captures = []
    if figure != "š": #for b, B and C
        if row_figure != 0 and column_figure != 0:
            try: #attempt to jump up left
                if table[row_figure - 1][column_figure - 1] == ".":
                    valid_moves.append((row_figure - 1, column_figure - 1))
            except:
                pass
        if row_figure != 0 and column_figure != 7:
            try: #attempt to jump up right
                if table[row_figure - 1][column_figure + 1] == ".":
                    valid_moves.append((row_figure - 1, column_figure + 1))
            except:
                pass
        if figure == "Č":
            captures.extend(check_attack_possibility_C(table, row_figure, column_figure, figure))
        elif figure == "Š":
            captures.extend(check_attack_possibility_S(table, row_figure, column_figure, figure))
        else:
            captures.extend(check_attack_possibility_c(table, row_figure, column_figure, figure))
    if figure != "č": #for c, C and B
        if row_figure != 7 and column_figure != 0:
            try: #attempt to jump down left
                if table[row_figure + 1][column_figure - 1] == ".":
                    valid_moves.append((row_figure + 1, column_figure - 1))
            except:
                pass
        if row_figure != 7 and column_figure != 7:
            try: #attempt to jump down right
                if table[row_figure + 1][column_figure + 1] == ".":
                    valid_moves.append((row_figure + 1, column_figure + 1))
            except:
                pass
        if figure == "Č":
            captures.extend(check_attack_possibility_C(table, row_figure, column_figure, figure, []))
        elif figure == "Š":
            captures.extend(check_attack_possibility_S(table, row_figure, column_figure, figure, []))
        else:
            captures.extend(check_attack_possibility_s(table, row_figure, column_figure, figure))
    return valid_moves, captures


def check_attack_possibility_c(table, row_figure, column_figure, figure):
    possible_attacks = []
    if (row_figure - 1) == 0:
        return possible_attacks
    #opponent up left of č
    if row_figure > 1 and column_figure > 1:
        try:
            if table[row_figure - 1][column_figure - 1] == "š" or table[row_figure - 1][column_figure - 1] == "Š":
                if table[row_figure - 2][column_figure - 2] == ".":
                    possible_long_attack = check_attack_possibility_c(table, row_figure - 2, column_figure - 2, figure)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent up right of č
    if row_figure > 1 and column_figure < 6:
        try:
            if table[row_figure - 1][column_figure + 1] == "š" or table[row_figure - 1][column_figure + 1] == "Š":
                if table[row_figure - 2][column_figure + 2] == ".":
                    possible_long_attack = check_attack_possibility_c(table, row_figure - 2, column_figure + 2, figure)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)])
        except IndexError:
            pass
    return possible_attacks

def check_attack_possibility_s(table, row_figure, column_figure, figure):
    possible_attacks = []
    if (row_figure + 1) == 7:
        return possible_attacks
    #opponent down left of š
    if row_figure < 6 and column_figure > 1:
        try:
            if table[row_figure + 1][column_figure - 1] == "č" or table[row_figure + 1][column_figure - 1] == "Č":
                if table[row_figure + 2][column_figure - 2] == ".":
                    possible_long_attack = check_attack_possibility_s(table, row_figure + 2, column_figure - 2, figure)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent down right of š
    if row_figure < 6 and column_figure < 6:
        try:
            if table[row_figure + 1][column_figure + 1] == "č" or table[row_figure + 1][column_figure + 1] == "Č":
                if table[row_figure + 2][column_figure + 2] == ".":
                    possible_long_attack = check_attack_possibility_s(table, row_figure + 2, column_figure + 2, figure)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)])
        except IndexError:
            pass
    return possible_attacks

def check_attack_possibility_C(table, row_figure, column_figure, figure, done_moves = []):
    possible_attacks = []
    done_moves.append((row_figure, column_figure))
    #opponent up left of Č
    if row_figure > 1 and column_figure > 1:
        try:
            if table[row_figure - 1][column_figure - 1] == "š" or table[row_figure - 1][column_figure - 1] == "Š":
                if table[row_figure - 2][column_figure - 2] == "." and ((row_figure - 2,column_figure - 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_C(table, row_figure - 2, column_figure - 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent up right of Č
    if row_figure > 1 and column_figure < 6:
        try:
            if table[row_figure - 1][column_figure + 1] == "š" or table[row_figure - 1][column_figure + 1] == "Š":
                if table[row_figure - 2][column_figure + 2] == "." and ((row_figure - 2,column_figure + 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_C(table, row_figure - 2, column_figure + 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)])
        except IndexError:
            pass
    #opponent down left of Č
    if row_figure < 6 and column_figure > 1:
        try:
            if table[row_figure + 1][column_figure - 1] == "š" or table[row_figure + 1][column_figure - 1] == "Š":
                if table[row_figure + 2][column_figure - 2] == "." and ((row_figure + 2,column_figure - 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_C(table, row_figure + 2, column_figure - 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent down right of Č
    if row_figure < 6 and column_figure < 6:
        try:
            if table[row_figure + 1][column_figure + 1] == "š" or table[row_figure + 1][column_figure + 1] == "Š":
                if table[row_figure + 2][column_figure + 2] == "." and ((row_figure + 2,column_figure + 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_C(table, row_figure + 2, column_figure + 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)])
        except IndexError:
            pass
    return possible_attacks

def check_attack_possibility_S(table, row_figure, column_figure, figure, done_moves = []):
    possible_attacks = []
    done_moves.append((row_figure, column_figure))
    #opponent up left of Š
    if row_figure > 1 and column_figure > 1:
        try:
            if table[row_figure - 1][column_figure - 1] == "č" or table[row_figure - 1][column_figure - 1] == "Č":
                if table[row_figure - 2][column_figure - 2] == "." and ((row_figure - 2, column_figure - 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_S(table, row_figure - 2, column_figure - 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent up right of Š
    if row_figure > 1 and column_figure < 6:
        try:
            if table[row_figure - 1][column_figure + 1] == "č" or table[row_figure - 1][column_figure + 1] == "Č":
                if table[row_figure - 2][column_figure + 2] == "." and ((row_figure - 2, column_figure + 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_S(table, row_figure - 2, column_figure + 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure - 2, column_figure + 2)])
        except IndexError:
            pass
    #opponent down left of Š
    if row_figure < 6 and column_figure > 1:
        try:
            if table[row_figure + 1][column_figure - 1] == "č" or table[row_figure + 1][column_figure - 1] == "Č":
                if table[row_figure + 2][column_figure - 2] == "." and ((row_figure + 2, column_figure - 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_S(table, row_figure + 2, column_figure - 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure - 2)])
        except IndexError:
            pass

    #opponent down right of Š
    if row_figure < 6 and column_figure < 6:
        try:
            if table[row_figure + 1][column_figure + 1] == "č" or table[row_figure + 1][column_figure + 1] == "Č":
                if table[row_figure + 2][column_figure + 2] == "." and ((row_figure + 2, column_figure + 2) not in done_moves):
                    possible_long_attack = check_attack_possibility_S(table, row_figure + 2, column_figure + 2, figure, done_moves)
                    for attack in possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)] + attack)
                    if not possible_long_attack:
                        possible_attacks.append([(row_figure + 2, column_figure + 2)])
        except IndexError:
            pass

    return possible_attacks

def move_figure(table, figure, move, possible_captures_separated, possible_captures, possible_moves):
    row_figure = int(figure[:1])
    column_figure = int(figure[1:])
    figure_label = table[row_figure][column_figure]
    try:
        row_move = int(move[:1])
        column_move = int(move[1:])
    except:
        return False
    if ((row_move, column_move) not in possible_captures_separated) and ((row_move, column_move) not in possible_moves):
        return False
    table[row_figure][column_figure] = "."
    if figure_label == "š" and row_move == 7:
        figure_label = "Š"
    if figure_label == "č" and row_move == 0:
        figure_label = "Č"
    table[row_move][column_move] = figure_label
    if ((row_move, column_move) in possible_moves):
        return True
    clear_eaten_figures(table, row_figure, column_figure, row_move, column_move, possible_captures)
    return True

def clear_eaten_figures(table, row_figure, column_figure, row_move, column_move, possible_captures):
    for capture_sequence in possible_captures:
        if (row_move, column_move) in capture_sequence:
            for move in capture_sequence:
                table[int((row_figure + move[0]) / 2)][int((column_figure + move[1]) / 2)] = "."
                row_figure = move[0]
                column_figure = move[1]
                if move == (row_move, column_move):
                    return

def find_all_possible_moves(table, maximizing_player):
    all_possible_moves = []
    if maximizing_player:
        for i in range(len(table)):
            for j in range(len(table[i])):
                valid_moves = []
                captures = []
                if table[i][j] == "č":
                    valid_moves, captures = check_possible_moves(table, i, j, "č")
                    all_possible_moves.extend(valid_moves)
                    all_possible_moves.extend(captures)
                    continue
                if table[i][j] == "Č":
                    valid_moves, captures = check_possible_moves(table, i, j, "Č")
                    all_possible_moves.extend(valid_moves)
                    all_possible_moves.extend(captures)
                    continue
                else:
                    pass
        return all_possible_moves
    else:
        for i in range(len(table)):
            for j in range(len(table[i])):
                valid_moves = []
                captures = []
                if table[i][j] == "š":
                    valid_moves, captures = check_possible_moves(table, i, j, "š")
                    all_possible_moves.extend(valid_moves)
                    all_possible_moves.extend(captures)
                    continue
                if table[i][j] == "Š":
                    valid_moves, captures = check_possible_moves(table, i, j, "Š")
                    all_possible_moves.extend(valid_moves)
                    all_possible_moves.extend(captures)
                    continue
                else:
                    pass
        return all_possible_moves