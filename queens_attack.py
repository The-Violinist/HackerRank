# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2
# Find the total number of moves that a queen can make given certain obstacles on the board
# I approached this as the points on a compass and move in all 8 possible directions until reaching an obstacle
# This is a work in progress as it returns the correct values, but times out with large data sets

n = 8                                                                                       # Number of rows and columns
k = 1                                                                                       # Number of obstacles
r_q = 4                                                                                     # Queen's starting row
c_q = 4                                                                                     # Queen's starting column
obstacles = [[3,5]]                                                                         # Blocked positions

def find_block(r_q, c_q, n, obstacles, r, c):                                               # Function for summing the possible moves in one direction
    counter = 0                                                                             # Counter for the number of possible moves
    position = [r_q,c_q]                                                                    # Starting square
    while True:
        position[0] = (position[0] + r)
        position[1] = (position[1] + c)
        if position in obstacles:
            return counter
        elif position[0] < 1 or position[0] > n or position[1] < 1 or position[1] > n:
            return counter
        else:
            counter +=1
def queensAttack(n, k, r_q, c_q, obstacles):                                                # Calls the find_block function for each possible compass direction
    total = 0                                                                               # Sums the returned moves for each direction
    
    directions = [[1, 0],[0, 1],[-1, 0],[0, -1],[1, 1],[-1, 1],[-1, -1],[1, -1]]            # Going around the directions: N, S, E, W, NE, SE, SW, NW
    for item in directions:
        total += find_block(r_q, c_q, n, obstacles, item[0], item[1])                       # Add to the total moves
    return total
print(queensAttack(n, k, r_q, c_q, obstacles))