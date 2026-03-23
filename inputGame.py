def check_selected_figure(table, figure):
    try:
        row = int(figure[:1])
        column = int(figure[1:])
        if (row > 7 or row < 0) or (column > 7 or column < 0):
            return False
    except Exception:
        return False
    if table[row][column] == "č" or table[row][column] == "Č":
        return True
    return False
