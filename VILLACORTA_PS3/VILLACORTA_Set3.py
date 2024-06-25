'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    following = to_member in social_graph[from_member]["following"]
    follower = from_member in social_graph[to_member]["following"]
        
    if following and follower:
        return "friends"
    elif following: 
        return "follower"
    elif follower:
        return "followed by"
    else:
        return "no relationship"

relationship_status("@joaquin", "@chums", social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
})

    
def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size_of_board = len(board)
    symbols_in_row = ""
    symbols_in_column = ""
    symbols_in_diagonal1 = "" 
    symbols_in_diagonal2 = ""

    for i in range(size_of_board):
        symbols_in_row = ""
        for j in range(size_of_board):
            symbols_in_row += board[i][j]
        if "X" * size_of_board in symbols_in_row:
            return "X"
        elif "O" * size_of_board in symbols_in_row:
            return "O"

    for i in range(size_of_board):
        symbols_in_column = ""
        for j in range(size_of_board):
            symbols_in_column += board[j][i]
        if "X" * size_of_board in symbols_in_column:
            return "X"
        elif "O" * size_of_board in symbols_in_column:
            return "O"

    for i in range (size_of_board): 
        symbols_in_diagonal1 += board[i][i]
        symbols_in_diagonal2 += board[i][size_of_board - 1 - i]

    if symbols_in_diagonal1 == "X" * size_of_board:
        return "X"
    elif symbols_in_diagonal1 == "O" * size_of_board:
        return "O"
            
    if symbols_in_diagonal2 == "X" * size_of_board:
        return "X"
    elif symbols_in_diagonal2 == "O" * size_of_board:
        return "O"
        
    return "NO WINNER"
            
board1 = [
    ['X','X','O'],
    ['O','X','O'],
    ['O','','X'],
]

board2 = [
    ['X','X','O'],
    ['O','X','O'],
    ['','O','X'],
]

board3 = [
    ['O','X','O'],
    ['','O','X'],
    ['X','X','O'],
]

board4 = [
    ['X','X','X'],
    ['O','X','O'],
    ['O','','O'],
]

board5 = [
    ['X','X','O'],
    ['O','X','O'],
    ['X','','O'],
]

board6 = [
    ['X','X','O'],
    ['O','X','O'],
    ['X','',''],
]

board7 = [
    ['X','X','O',''],
    ['O','X','O','O'],
    ['X','','','O'],
    ['O','X','','']
]
tic_tac_toe (board3)


def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # direct route
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]

    min_time = float('inf')

    # extra stops 
    for current_stop in route_map:
        if current_stop[0] == first_stop:
            travel_time = route_map[current_stop]["travel_time_mins"]
            next_stop = current_stop[1]

            while next_stop != first_stop and next_stop != second_stop:
                found_next_leg = False
                for leg in route_map:
                    if leg[0] == next_stop:
                        travel_time += route_map[leg]["travel_time_mins"]
                        next_stop = leg[1]
                        found_next_leg = True
                        break

                if not found_next_leg:
                    break

            if next_stop == second_stop:
                min_time = min(min_time, travel_time)

    return min_time

eta("upd", "dlsu", route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
})
