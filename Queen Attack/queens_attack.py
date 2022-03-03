# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2
# Find the total number of moves that a queen can make given certain obstacles on the board
# I approached this as the points on a compass and move in all 8 possible directions until reaching an obstacle
# This is a work in progress as it returns the correct values, but times out with large data sets
# See queens_attack2.py for the working script

# n = 5                                                                                       # Number of rows and columns
# k = 3                                                                                       # Number of obstacles
# r_q = 4                                                                                     # Queen's starting row
# c_q = 3                                                                                     # Queen's starting column
# obstacles = [[5,5],[4,2],[2,3]]                                                             # Blocked positions

n = 100
k = 100
r_q = 48
c_q = 81
obstacles = [[54,87],[64,97],[42,75],[32,65],[42,87],[32,97],[54,75],[64,65],[48,87],[48,75],[54,81],[42,81],[45,17],[14,24],[35,15],[95,64],[63,87],[25,72],[71,38],[96,97],[16,30],[60,34],[31,67],[26,82],[20,93],[81,38],[51,94],[75,41],[79,84],[79,65],[76,80],[52,87],[81,54],[89,52],[20,31],[10,41],[32,73],[83,98],[87,61],[82,52],[80,64],[82,46],[49,21],[73,86],[37,70],[43,12],[94,28],[10,93],[52,25],[50,61],[52,68],[52,23],[60,91],[79,17],[93,82],[12,18],[75,64],[69,69],[94,74],[61,61],[46,57],[67,45],[96,64],[83,89],[58,87],[76,53],[79,21],[94,70],[16,10],[50,82],[92,20],[40,51],[49,28],[51,82],[35,16],[15,86],[78,89],[41,98],[70,46],[79,79],[24,40],[91,13],[59,73],[35,32],[40,31],[14,31],[71,35],[96,18],[27,39],[28,38],[41,36],[31,63],[52,48],[81,25],[49,90],[32,65],[25,45],[63,94],[89,50],[43,41]]

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
        fb_counter = (find_block(r_q, c_q, n, obstacles, item[0], item[1]))             # Get number of moves for this turn
        total += fb_counter                                                                 # Add those moves to the total
    return total                                                                            # Return the total moves if all blocks are not encountered
print(queensAttack(n, k, r_q, c_q, obstacles))