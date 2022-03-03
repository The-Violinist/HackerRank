# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2
# Find the total number of moves that a queen can make given certain obstacles on the board
# I approached this as the points on a compass and move in all 8 possible directions until reaching an obstacle
# This script does not work, in that it subtracts too many spaces if there are multiple obstacles in the same direction
# This was used as the basis for queens_attack2.py by turning each conditional into its own function

# n = 5                                                                 # Number of rows and columns
# k = 3                                                                 # Number of obstacles
# r_q = 4                                                               # Queen's starting row
# c_q = 3                                                               # Queen's starting column
# obstacles = [[5,5],[4,2],[2,3]]                                       # Blocked positions

# n = 8                                                                   # Number of rows and columns
# k = 1                                                                   # Number of obstacles
# r_q = 4                                                                 # Queen's starting row
# c_q = 4                                                                 # Queen's starting column
# obstacles = [[3,5],[2,6]]                                                     # Blocked positions

n = 100
k = 100
r_q = 48
c_q = 81
obstacles = [[54,87],[64,97],[42,75],[32,65],[42,87],[32,97],[54,75],[64,65],[48,87],[48,75],[54,81],[42,81],[45,17],[14,24],[35,15],[95,64],[63,87],[25,72],[71,38],[96,97],[16,30],[60,34],[31,67],[26,82],[20,93],[81,38],[51,94],[75,41],[79,84],[79,65],[76,80],[52,87],[81,54],[89,52],[20,31],[10,41],[32,73],[83,98],[87,61],[82,52],[80,64],[82,46],[49,21],[73,86],[37,70],[43,12],[94,28],[10,93],[52,25],[50,61],[52,68],[52,23],[60,91],[79,17],[93,82],[12,18],[75,64],[69,69],[94,74],[61,61],[46,57],[67,45],[96,64],[83,89],[58,87],[76,53],[79,21],[94,70],[16,10],[50,82],[92,20],[40,51],[49,28],[51,82],[35,16],[15,86],[78,89],[41,98],[70,46],[79,79],[24,40],[91,13],[59,73],[35,32],[40,31],[14,31],[71,35],[96,18],[27,39],[28,38],[41,36],[31,63],[52,48],[81,25],[49,90],[32,65],[25,45],[63,94],[89,50],[43,41]]

def total_moves(r_q, c_q, n):                                           # Finds the total possible moves without blocking squares
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

def queensAttack(n, k, r_q, c_q, obstacles):                            # Determine if the obstacles block the queen
    motion = [1,-1,0]                                                   # Possible directions for motion
    total = total_moves(r_q, c_q, n)                                    # All possible moves without blocking squares
    for obs_item in obstacles:
        r_diff = obs_item[0] - r_q                                      # Find the difference between the queen starting row and the obstacle
        c_diff = obs_item[1] - c_q                                      # Find the difference between the queen starting column and the obstacle
        if r_diff != 0 and c_diff != 0:                                 # Block is not directly vertical or horizontal from the queen
            for mot_item in motion:                                     # Get locations of all diagonal moves
                column = c_q + (r_diff * mot_item)                      # Add the queen's starting column to the amount of difference to equal the current row in the obstacle
                
                if ([obs_item[0], column]) == obs_item:                 # If the queen would encounter that block, continue
                    
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
        
        elif r_diff == 0:                                               # If the block is on the same row as the queen
            if c_q > obs_item[1]:                                           # If queen is to the right of the block
                total -= obs_item[1]
            else:                                                           # If the queen is to the left of the block
                total -= n - obs_item[1] + 1
        elif c_diff == 0:                                               # If the block in on the same column as the queen
            if r_q > obs_item[0]:                                           # If the queen is higher than the block
                total -= obs_item[0]
            else:
                total -= n - obs_item[0] + 1                                # If the queen is lower than the block
    return total

print(queensAttack(n, k, r_q, c_q, obstacles))