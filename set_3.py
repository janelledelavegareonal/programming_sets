'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Returns relationship type between two members in a social graph.
    '''
    from_follows = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_follows and to_follows:
        return "friends"
    elif from_follows:
        return "follower"
    elif to_follows:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Evaluates the board and returns the winner or "NO WINNER".
    '''
    n = len(board)

    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]

    # Check columns
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        if len(set(column)) == 1 and column[0] != "":
            return column[0]

    # Check main diagonal
    diag1 = [board[i][i] for i in range(n)]
    if len(set(diag1)) == 1 and diag1[0] != "":
        return diag1[0]

    # Check anti-diagonal
    diag2 = [board[i][n - 1 - i] for i in range(n)]
    if len(set(diag2)) == 1 and diag2[0] != "":
        return diag2[0]

    return "NO WINNER"



def eta(first_stop, second_stop, route_map):
    '''ETA.

    Returns travel time in minutes between two stops in a circular one-way route.
    '''
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), data in route_map.items():
            if start == current_stop:
                total_time += data["travel_time_mins"]
                current_stop = end
                break

    return total_time

