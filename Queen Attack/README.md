
# Queen's Attack

## These are 3 iterations of the Queen's Attack solution.

1. queens_attack.py returns the correct values, but times out with large data sets
    - The approach is to move the queen in all 8 directions of motion until encountering an obstacle
    - A counter is used to sum the total spaces
2. queens_attack1.py is a second approach which completes all data sets in time but gives an incorrect answer for certain sets
    - This approach starts with the total moves possible if there are no obstacles
    - It is then determined if the queen will encounter any of the obstacles then subtract all spaces beyond that point
3. queens_attack2.py **really works!** It is a variant of the previous script but uses a function for each direction of motion
    - As with the previous approach, this starts with the total possible moves with no obstacles
    - Each direction function then finds obstacles which the queen will encounter and returns the highest number of blocked spaces
    - The highest number of blocked spaces for each direction is then subtracted from the total moves
