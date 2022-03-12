# Another possible iteration, but not complete

n = 8
r_q = 4
c_q = 4
obstacles = [[5,5],[3,5],[3,3],[5,3],[6,6]]

# n = 100
# k = 100
# r_q = 48
# c_q = 81
# obstacles = [[54,87],[64,97],[42,75],[32,65],[42,87],[32,97],[54,75],[64,65],[48,87],[48,75],[54,81],[42,81],[45,17],[14,24],[35,15],[95,64],[63,87],[25,72],[71,38],[96,97],[16,30],[60,34],[31,67],[26,82],[20,93],[81,38],[51,94],[75,41],[79,84],[79,65],[76,80],[52,87],[81,54],[89,52],[20,31],[10,41],[32,73],[83,98],[87,61],[82,52],[80,64],[82,46],[49,21],[73,86],[37,70],[43,12],[94,28],[10,93],[52,25],[50,61],[52,68],[52,23],[60,91],[79,17],[93,82],[12,18],[75,64],[69,69],[94,74],[61,61],[46,57],[67,45],[96,64],[83,89],[58,87],[76,53],[79,21],[94,70],[16,10],[50,82],[92,20],[40,51],[49,28],[51,82],[35,16],[15,86],[78,89],[41,98],[70,46],[79,79],[24,40],[91,13],[59,73],[35,32],[40,31],[14,31],[71,35],[96,18],[27,39],[28,38],[41,36],[31,63],[52,48],[81,25],[49,90],[32,65],[25,45],[63,94],[89,50],[43,41]]

def total_moves(r_q, c_q, n):
    if r_q > n // 2:                                                        # Determine if the queen starting row is greater than the halfway point on the board
        row_q = n - r_q                                                         # Assign the relative placement from the edge on a 0 point scale
    else:
        row_q = r_q - 1                                                         # Assign the relative placement from the edge on a 0 point scale 
    if c_q > n // 2:                                                        # Determine if the queen starting column is greater than the halfway point on the board
        column_q = n - c_q                                                      # Assign the relative placement from the edge on a 0 point scale 
    else:
        column_q = c_q -1                                                       # Assign the relative placement from the edge on a 0 point scale 
    if row_q > column_q:                                                    # Determine which is further away from the edge of the board (each point towards the center adds 2 additional moves)
        return ((n * 2) -2) + ((n - 1) + (column_q * 2))                    # The vertical and horizontal axes will always be constant, which is n*2-2 (2 is subtracted for the space taken by the queen on each axis)
    else:                                                                       # Add to that the the horizontals, which add up to (n - 1) + (the relative distance from the edge * 2)
        return ((n * 2) -2) + ((n - 1) + (row_q * 2))

obs_dirs = {}
for c in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
    obs_dirs[c] = None

def blocks():
    #NE SE SW NW
    directions = [[1,1],[-1,1],[-1,-1],[1,-1]]
    for obstacle in obstacles:
        row_diff = r_q - obstacle[0]
        column_diff = c_q - obstacle[1]
        if obstacle[0] == r_q:
            if obstacle[1] > c_q:
                if obs_dirs['e'] == None:
                    obs_dirs['e'] = obstacle
                elif obstacle[1] < obs_dirs['e'][1]:
                    obs_dirs['e'] = obstacle
            else:
                if obs_dirs['w'] == None:
                    obs_dirs['w'] = obstacle
                elif obstacle[1] > obs_dirs['w'][1]:
                    obs_dirs['w'] = obstacle
        elif obstacle[1] == c_q:
            if obstacle[0] > r_q:
                if obs_dirs['n'] == None:
                    obs_dirs['n'] = obstacle
                elif obstacle[0] < obs_dirs['n'][[0]]:
                    obs_dirs['n'] = obstacle
            else:
                if obs_dirs['s'] == None:
                    obs_dirs['s'] = obstacle
                elif  obs_dirs['s'][0] > obstacle[0]:
                     obs_dirs['s'] = obstacle
        elif abs(row_diff) % abs(column_diff) == 0:
            direction = []
            row_motion = row_diff / abs(row_diff)
            column_motion = column_diff / abs(column_diff)
            direction.extend([row_motion, column_motion])
            if direction == directions[0]:
                obs_dirs['ne'] = obstacle
            if direction == directions[1]:
                obs_dirs['se'] = obstacle
            if direction == directions[2]:
                print("sw")
                obs_dirs['sw'] = obstacle
            if direction == directions[3]:
                obs_dirs['nw'] = obstacle

    print(obs_dirs)


blocks()
'''
def relative_dist(n, r_q, c_q, obs_row, obs_col):
  middle = n // 2
  if r_q > middle:
    r_q = n - r_q + 1
  if c_q > middle:
    c_q = n - c_q + 1
  if 
'''