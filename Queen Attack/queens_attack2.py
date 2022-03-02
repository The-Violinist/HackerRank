# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2
# Find the total number of moves that a queen can make given certain obstacles on the board
# I approached this as the points on a compass and move in all 8 possible directions until reaching an obstacle
# This is a work in progress as it returns the correct values, but times out with large data sets

# n = 5                                                                 # Number of rows and columns
# k = 3                                                                 # Number of obstacles
# r_q = 4                                                               # Queen's starting row
# c_q = 3                                                               # Queen's starting column
# obstacles = [[5,5],[4,2],[2,3]]                                       # Blocked positions


n = 8                                                                   # Number of rows and columns
k = 1                                                                   # Number of obstacles
r_q = 4                                                                 # Queen's starting row
c_q = 4                                                                 # Queen's starting column
obstacles = [[3,5],[2,6]]                                                     # Blocked positions

# Finds the total possible moves without blocking squares
def total_moves(r_q, c_q, n):
    N = n - r_q
    E = n - c_q
    S = r_q - 1
    W = c_q - 1
    if N > E:
        NE = E
    else:
        NE = N
    if S > E:
        SE = E
    else:
        SE = S
    if W > S:
        SW = S
    else:
        SW = W
    if N > W:
        NW = W
    else:
        NW = N
    total = N+E+S+W+NE+SE+SW+NW
    return total

# Finds blocked spaces to the north
def North(r_q, c_q, n):
    for obs_item in obstacles:
        if obs_item[1] == c_q and obs_item[0] > r_q:                    # If the item is in the same column as the queen and to the north
            return (n - obs_item[0] + 1)                                # Return the number of blocked spaces

# Finds blocked spaces to the south
def South(r_q, c_q, n):
    for obs_item in obstacles:
        if obs_item[1] == c_q and obs_item[0] < r_q:                    # If the item is in the same column as the queen and lower
            return (obs_item[0])                # Return the number of blocked spaces

# Finds blocked spaces to the east
def East(r_q, c_q, n):
    for obs_item in obstacles:
        if obs_item[0] == r_q and obs_item[1] > c_q:                    # If the item is in the same row as the queen to the right
            return (n - obs_item[1] + 1)        # Return the number of blocked spaces

# Finds blocked spaces to the west
def West(r_q, c_q, n):
    for obs_item in obstacles:
        if obs_item[0] == r_q and obs_item[1] < c_q:                      # If the item is in the same row as the queen and to the left
            return (obs_item[1])                # Return the number of blocked spaces

# Finds blocked spaces to the northeast
def NorEast(r_q, c_q, n):
    motion = 1                                                          # Direction of change for the column number
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] > r_q and obs_item[1] > c_q:                     # If the block is NE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block:
                if (n - column + 1) > (n - obs_item[0] + 1):            # Return whichever side is reached first
                    return (n - obs_item[0] + 1)                        # Top first 
                else:
                    return (n - column + 1)                             # Right side first

# Finds blocked spaces to the southeast
def SouEast(r_q, c_q, n):
    motion = 1                                                          # Direction of change for the column number
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] < r_q and obs_item[1] > c_q:                     # If the block is SE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue
                if obs_item[0] < r_q:                                   # If the block is in a lower row, continue

# Finds blocked spaces to the southwest
def SouWest(r_q, c_q, n):
    motion = -1                                                         # Direction of change for the column number
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] < r_q and obs_item[1] < c_q:                     # If the block is SW from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue



# Finds blocked spaces to the northwest
def NorWest(r_q, c_q, n):
    motion = -1                                                        # Direction of change for the column number
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] > r_q and obs_item[1] < c_q:                     # If the block is SE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue






                    
                    if obs_item[0] < r_q:                               # If the block is in a lower row, continue
                        if obs_item[1] > c_q:                               # If column is to the right of queen
                            if (n - column + 1) > obs_item[0]:                  # Determine if the bottom or right side is reached first
                                total -= obs_item[0]                            # Bottom first
                            else:
                                total -= (n - column + 1)                       # Right side first
                    
                        else:                                               # If the column is to the left of the queen
                            if obs_item[1] < obs_item[0]:                       # Determine if the bottom or left side is reached first
                                total -= obs_item[1]                            # Left side first
                            else: 
                                total -= obs_item[0]                            # Bottom first
                        
                    else:                                               # If the block is in a higher row
                        if obs_item[1] > c_q:                               # If column is to the right of queen
                            if (n - column + 1) > (n - obs_item[0] + 1):        # If the right side is reached before the top
                                total -= (n - obs_item[0] + 1)                  # Top first 
                            else:
                                total -= (n - column + 1)                       # Right side first
                        else:                                               # If the column is to the left
                            if obs_item[1] > (n - obs_item[0] + 1):         # If the top is reached before the left side
                                total -= (n - obs_item[0] + 1)                  # Top first
                            else:
                                total -= obs_item[1]                            # Left side first
        
        elif c_diff == 0:                                               # If the block in on the same column as the queen
            if r_q > obs_item[0]:                                           # If the queen is higher than the block
                total -= obs_item[0]
            else:
                total -= n - obs_item[0] + 1                                # If the queen is lower than the block
    return total

print(queensAttack(n, k, r_q, c_q, obstacles))