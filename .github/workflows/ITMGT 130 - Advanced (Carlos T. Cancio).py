'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    if from_member in social_graph and to_member in social_graph:
        if to_member in social_graph[from_member]["following"]:
            if from_member in social_graph[to_member]["following"]:
                return "friends"
            else:
                return "follower"
        elif from_member in social_graph[to_member]["following"]:
            return "followed by"
    return "no relationship"

def tic_tac_toe(board):
    n = len(board)
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != '':
            return row[0]
    for col in range(n):
        if all(row[col] == board[0][col] for row in board) and board[0][col] != '':
            return board[0][col]
    if all(board[i][i] == board[0][0] for i in range(1, n)) and board[0][0] != '':
        return board[0][0]
    if all(board[i][n - i - 1] == board[0][n - 1] for i in range(1, n)) and board[0][n - 1] != '':
        return board[0][n - 1]
    if all(board[i][0] == board[0][0] and board[i][0] != '' for i in range(1, n)):
        return board[0][0]
    if all(board[0][i] == board[0][0] and board[0][i] != '' for i in range(1, n)):
        return board[0][0]
    if all(cell != '' for row in board for cell in row):
        return "NO WINNER"
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0

    while current_stop != second_stop:
        next_stop = None
        for route, data in route_map.items():
            if route[0] == current_stop:
                next_stop = route[1]
                total_time += data['travel_time_mins']
                break
        current_stop = next_stop
    return total_time
