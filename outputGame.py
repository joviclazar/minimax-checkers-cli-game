import moves

#table = [
#        [".", "0", "", "č", "", "c", ".", "c"],
#        ["c", ".", "c", ".", "c", ".", "c", "."],
#        [".", "c", ".", "c", ".", "c", ".", "c"],
#        [".", ".", ".", ".", ".", ".", ".", "."],
#        [".", ".", ".", ".", ".", ".", ".", "."],
#        ["b", ".", "b", ".", "b", ".", "b", "."],
#        [".", "b", ".", "b", ".", "b", ".", "b"],
#        ["b", ".", "b", ".", "b", ".", "b", "."]
#    ]

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    NEGATIVE = "\033[7m"

def table_print(table):
    print("---------------------------------------")
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    for i in range(len(table)):
        print(" " + str(i) + " |", end="")
        for j in range(len(table[0])):
            if table[i][j] == "š" or table[i][j] == "Š":
                print(" " + colors.RED + table[i][j] + colors.RESET + " |", end="")
            elif table[i][j] == "č" or table[i][j] == "Č":
                print(" " + colors.BLUE + table[i][j] + colors.RESET + " |", end="")
            else:
                print(" " + table[i][j] + " |", end="")
        print(" " + str(i))
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

def table_print_highlighed_figure(table, figure):
    row_figure = int(figure[:1])
    column_figure = int(figure[1:])
    figure = table[row_figure][column_figure]
    possible_moves, possible_captures = moves.check_possible_moves(table, row_figure, column_figure, figure)
    possible_captures_separated = []
    for i in possible_captures:
        for j in i:
            possible_captures_separated.append(j)
    if possible_moves == [] and possible_captures == []:
        return possible_captures_separated, possible_captures, possible_moves
    print("------------------------------------")
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    for i in range(len(table)):
        print(" " + str(i) + " |", end="")
        for j in range(len(table[0])):
            if (i, j) in possible_moves or (i, j) in possible_captures_separated:
                print(colors.YELLOW + str(i) + " " + str(j) + colors.RESET + "|", end="")
            elif i == row_figure and j == column_figure:
                print(" " + colors.GREEN + table[i][j] + colors.RESET + " |", end="")
            elif table[i][j] == "š" or table[i][j] == "Š":
                print(" " + colors.RED + table[i][j] + colors.RESET + " |", end="")
            elif table[i][j] == "č" or table[i][j] == "Č":
                print(" " + colors.BLUE + table[i][j] + colors.RESET + " |", end="")
            else:
                print(" " + table[i][j] + " |", end="")
        print(" " + str(i))
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    return possible_captures_separated, possible_captures, possible_moves

def print_computer_move(table, best_move):
    print("---------------------------------------")
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    for i in range(len(best_move)):
        print(" " + str(i) + " |", end="")
        for j in range(len(best_move[0])):
            if table[i][j] != best_move[i][j]:
                if best_move[i][j] == ".":
                    print(colors.NEGATIVE + " " + "x" + " " + colors.RESET + "|", end="")
                else:
                    print(colors.NEGATIVE + " " + best_move[i][j] + " " + colors.RESET + "|", end="")
            else:
                if best_move[i][j] == "š" or best_move[i][j] == "Š":
                    print(" " + colors.RED + best_move[i][j] + colors.RESET + " |", end="")
                elif best_move[i][j] == "č" or best_move[i][j] == "Č":
                    print(" " + colors.BLUE + best_move[i][j] + colors.RESET + " |", end="")
                else:
                    print(" " + best_move[i][j] + " |", end="")
        print(" " + str(i))
    print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")