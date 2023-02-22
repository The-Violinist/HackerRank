# https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true
# Find areas of map (as array) which are lower than all adjacent indices -- indicated by a greater number for depth

grid = ["1112", "1912", "1892", "1234"]
grid = ["989", "191", "111"]


def cavityMap(grid):
    end = len(grid) - 1
    if end == 1 or end == 0:
        return grid
    new_list = [grid[0], grid[end]]
    row = 1
    while row < end:
        column = 1
        current_list = [grid[row][0], grid[row][end]]
        while column < end:
            cavity = int(grid[row][column])
            above = int(grid[row - 1][column])
            below = int(grid[row + 1][column])
            left = int(grid[row][column - 1])
            right = int(grid[row][column + 1])
            if cavity > above and cavity > below and cavity > left and cavity > right:
                current_list.insert(column, "X")
            else:
                current_list.insert(column, (grid[row][column]))
            column += 1
        new_list.insert(row, "".join(current_list))
        row += 1
    return new_list


print(cavityMap(grid))
