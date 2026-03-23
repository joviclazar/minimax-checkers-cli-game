import outputGame
import inputGame
import moves
import minimax
import time

"""
table = [
        [".", "š", ".", "š", ".", "š", ".", "š"],
        ["š", ".", "š", ".", "š", ".", "š", "."],
        [".", "š", ".", "š", ".", "š", ".", "š"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["č", ".", "č", ".", "č", ".", "č", "."],
        [".", "č", ".", "č", ".", "č", ".", "č"],
        ["č", ".", "č", ".", "č", ".", "č", "."]
    ]

table = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
"""

def main():
    table = [
        [".", "š", ".", "š", ".", "š", ".", "š"],
        ["š", ".", "š", ".", "š", ".", "š", "."],
        [".", "š", ".", "š", ".", "š", ".", "š"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["č", ".", "č", ".", "č", ".", "č", "."],
        [".", "č", ".", "č", ".", "č", ".", "č"],
        ["č", ".", "č", ".", "č", ".", "č", "."]
    ]

    #č and š are regular pieces, Č and Š are queens
    number_of_pieces = 24
    previous_time_move = 3
    previous_depth = 6
    print(outputGame.colors.GREEN + "WELCOME TO CHECKERS" + outputGame.colors.RESET)
    print("Loading data...")
    minimax.loading_hash()
    print("Data loaded!")
    while True:
        all_possible_moves = moves.find_all_possible_moves(table, True)
        if all_possible_moves == []:
            print("You have no moves available!\nYou lost!")
            minimax.saving_hash(minimax.hashed_tables)
            exit()
        outputGame.table_print(table)
        figure = input("Choose your figure: ")
        if figure.lower() == "x":
            print("Surrender? I am disappointed...")
            minimax.saving_hash(minimax.hashed_tables)
            exit()
        if inputGame.check_selected_figure(table, figure) == False:
            print("You have to chose your own figure!")
            continue
        possible_captures_separated, possible_captures, possible_moves = outputGame.table_print_highlighed_figure(table, figure)
        if possible_captures == [] and possible_moves == []:
            print("You choose a figure that has no movement available!\nTry again")
            continue
        move = input("Choose one of highlighted moves: ")
        while True:
            if move.lower() == "x":
                print("Surrender? I am disappointed...")
                minimax.saving_hash(minimax.hashed_tables)
                exit()
            if not moves.move_figure(table, figure, move, possible_captures_separated, possible_captures, possible_moves):
                move = input("You have to choose one of highlighted positions!\nTry again:")
            else:
                break
        print("I am thinking...")
        depth = minimax.determine_dynamic_depth(previous_time_move, previous_depth, number_of_pieces)
        t1 = time.time()
        table = minimax.get_best_move(table, depth, t1)
        t2 = time.time()
        print("I needed " + str(t2 - t1) + " seconds to think.")
        previous_time_move = t2 - t1
        winning_condition, number_of_pieces = minimax.evaluate_heuristic(table)
        if winning_condition == -float('inf'):
            print("You lost... Sad...")
            minimax.saving_hash(minimax.hashed_tables)
            exit()

if __name__ == '__main__':
    main()