# Number of rows and columns
n = 8
# Number of obstacles
k = 1
# Queen starting position
r_q = 4
c_q = 4
# Blocked positions
obstacles = [[3,5]]

def find_block(r_q, c_q, n, obstacles, r, c):
    counter = 0
    position = [r_q,c_q]
    while True:
        position[0] = (position[0] + r)
        position[1] = (position[1] + c)
        if position in obstacles:
            return counter
        elif position[0] < 1 or position[0] > n or position[1] < 1 or position[1] > n:
            return counter
        else:
            counter +=1
def queensAttack(n, k, r_q, c_q, obstacles):
    total = 0
    # Going around the directions: N, S, E, W, NE, SE, SW, NW
    directions = [[1, 0],[0, 1],[-1, 0],[0, -1],[1, 1],[-1, 1],[-1, -1],[1, -1]]
    for item in directions:
        total += find_block(r_q, c_q, n, obstacles, item[0], item[1])
    return total
print(queensAttack(n, k, r_q, c_q, obstacles))