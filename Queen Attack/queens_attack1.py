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

n = 8                                                                   # Number of rows and columns
k = 1                                                                   # Number of obstacles
r_q = 4                                                                 # Queen's starting row
c_q = 4                                                                 # Queen's starting column
obstacles = [[3,5],[2,6]]                                                     # Blocked positions


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