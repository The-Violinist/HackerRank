# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2
# Find the total number of moves that a queen can make given certain obstacles on the board
# I approached this as the points on a compass and move in all 8 possible directions until reaching an obstacle
# 3/3/22: Fully working script. Special thanks to Jackson Hazdovac for troubleshooting the pseudo code with me!

### TEST DATA ###
# n = 5                                                                 # Number of rows and columns
# k = 3                                                                 # Number of obstacles
# r_q = 4                                                               # Queen's starting row
# c_q = 3                                                               # Queen's starting column
# obstacles = [[5,5],[4,2],[2,3]]                                       # Blocked positions


# n = 8                                                                   # Number of rows and columns
# k = 1                                                                   # Number of obstacles
# r_q = 4                                                                 # Queen's starting row
# c_q = 4                                                                 # Queen's starting column
# obstacles = [[3,5],[2,6]]                                               # Blocked positions

n = 100
k = 100
r_q = 48
c_q = 81
obstacles = [[54,87],[64,97],[42,75],[32,65],[42,87],[32,97],[54,75],[64,65],[48,87],[48,75],[54,81],[42,81],[45,17],[14,24],[35,15],[95,64],[63,87],[25,72],[71,38],[96,97],[16,30],[60,34],[31,67],[26,82],[20,93],[81,38],[51,94],[75,41],[79,84],[79,65],[76,80],[52,87],[81,54],[89,52],[20,31],[10,41],[32,73],[83,98],[87,61],[82,52],[80,64],[82,46],[49,21],[73,86],[37,70],[43,12],[94,28],[10,93],[52,25],[50,61],[52,68],[52,23],[60,91],[79,17],[93,82],[12,18],[75,64],[69,69],[94,74],[61,61],[46,57],[67,45],[96,64],[83,89],[58,87],[76,53],[79,21],[94,70],[16,10],[50,82],[92,20],[40,51],[49,28],[51,82],[35,16],[15,86],[78,89],[41,98],[70,46],[79,79],[24,40],[91,13],[59,73],[35,32],[40,31],[14,31],[71,35],[96,18],[27,39],[28,38],[41,36],[31,63],[52,48],[81,25],[49,90],[32,65],[25,45],[63,94],[89,50],[43,41]]

### FUNCTIONS ###
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
def North(r_q, c_q, n, obstacles):
    blocked = 0
    for obs_item in obstacles:
        if obs_item[1] == c_q and obs_item[0] > r_q:                    # If the item is in the same column as the queen and to the north
            if (n - obs_item[0] + 1) > blocked:                         # Return the greatest number of blocked spaces
                blocked = (n - obs_item[0] + 1)
    return blocked

# Finds blocked spaces to the south
def South(r_q, c_q, n, obstacles):
    blocked = 0
    for obs_item in obstacles:
        if obs_item[1] == c_q and obs_item[0] < r_q:                    # If the item is in the same column as the queen and lower
            if obs_item[0] > blocked:                                   # Return the greatest number of blocked spaces
                blocked = obs_item[0]
    return blocked

# Finds blocked spaces to the east
def East(r_q, c_q, n, obstacles):
    blocked = 0
    for obs_item in obstacles:
        if obs_item[0] == r_q and obs_item[1] > c_q:                    # If the item is in the same row as the queen to the right
            if (n - obs_item[1] + 1) > blocked:                         # Return the greatest number of blocked spaces
                blocked = (n - obs_item[1] + 1)
    return blocked

# Finds blocked spaces to the west
def West(r_q, c_q, n, obstacles):
    blocked = 0
    for obs_item in obstacles:
        if obs_item[0] == r_q and obs_item[1] < c_q:                      # If the item is in the same row as the queen and to the left
            if obs_item[1] > blocked:                                     # Return the greatest number of blocked spaces
                blocked = obs_item[1]
    return blocked

# Finds blocked spaces to the northeast
def NorEast(r_q, c_q, n, obstacles):
    motion = 1                                                          # Direction of change for the column number
    blocked = 0
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] > r_q and obs_item[1] > c_q:                     # If the block is NE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block:
                if (n - column + 1) > (n - obs_item[0] + 1):            # Determine which side is reached first
                    if (n - obs_item[0] + 1) > blocked:                 # Top first 
                        blocked = (n - obs_item[0] + 1)
                else:
                    if (n - column + 1) > blocked:                      # Right side first
                        blocked = (n - column + 1)
    return blocked                                                      # Return the greatest number of blocked spaces

# Finds blocked spaces to the southeast
def SouEast(r_q, c_q, n, obstacles):
    motion = -1                                                         # Direction of change for the column number
    blocked = 0
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] < r_q and obs_item[1] > c_q:                     # If the block is SE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue
                if (n - column + 1) > obs_item[0]:                      # Determine if right side is greater distance than bottom
                    if obs_item[0] > blocked:                           # Bottom first 
                        blocked = obs_item[0]
                else:
                    if (n - column + 1) > blocked:                      # Right side first
                        blocked = (n - column + 1)
    return blocked                                                      # Return the greatest number of blocked spaces

# Finds blocked spaces to the southwest
def SouWest(r_q, c_q, n, obstacles):
    motion = 1                                                          # Direction of change for the column number
    blocked = 0
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] < r_q and obs_item[1] < c_q:                     # If the block is SW from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue
                if obs_item[1] > obs_item[0]:                           # Determine if left side is a greater distance than the bottom
                    if obs_item[0] > blocked:                           # Bottom first 
                        blocked = obs_item[0]
                else:
                    if obs_item[1] > blocked:                           # Right side first
                        blocked = obs_item[1]
    return blocked                                                      # Return the greatest number of blocked spaces

# Finds blocked spaces to the northwest
def NorWest(r_q, c_q, n, obstacles):
    motion = -1                                                         # Direction of change for the column number
    blocked = 0
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        if obs_item[0] > r_q and obs_item[1] < c_q:                     # If the block is SE from the queen
            column = c_q + (r_diff * motion)                            # The column of the queen position based on the row positions in the obstacles
            if ([obs_item[0], column]) == obs_item:                     # If the queen would encounter that block, continue
                if obs_item[1] > (n - obs_item[0] + 1):                 # Determine if the distance to the left side is greater
                    if (n - obs_item[0] + 1) > blocked:                 # Top first 
                        blocked = (n - obs_item[0] + 1)
                else:
                    if obs_item[1] > blocked:                           # Right side first
                        blocked = obs_item[1]
    return blocked                                                      # Return the greatest number of blocked spaces

# Main function to get the final return value (total possible moves for the queen)
def queensAttack(n, k, r_q, c_q, obstacles):
    total = total_moves(r_q, c_q, n)                                    # The total moves before any blocking spaces
    total -= North(r_q, c_q, n, obstacles)                              # Subtract all unavailable moves based on the closest obstacle to the queen in each direction
    total -= South(r_q, c_q, n, obstacles)
    total -= East(r_q, c_q, n, obstacles)
    total -= West(r_q, c_q, n, obstacles)
    total -= NorEast(r_q, c_q, n, obstacles)
    total -= SouEast(r_q, c_q, n, obstacles)
    total -= SouWest(r_q, c_q, n, obstacles)
    total -= NorWest(r_q, c_q, n, obstacles)
    return total


print(queensAttack(n, k, r_q, c_q, obstacles))
