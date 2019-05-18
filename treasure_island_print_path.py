# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
# The treasure island is marked as ‘X’ in a block of the matrix. ‘X’ will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
# Other areas ‘O’ are safe to sail in. The top-left corner is always safe.
# Output the minimum number of steps to get to the treasure.

from collections import deque

def bfs(treasure_map):
    queue = deque()
    queue.append([(0, 0)])
    nr, nc = len(treasure_map), len(treasure_map[0])
    pathLength = 0
    seen = set([list])
    seen.add((0, 0))

    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if treasure_map[r][c] == 3:
            return path
        for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= x <= nc-1 and 0 <= y <= nr-1 and treasure_map[x][y] != 1 and (x, y) not in seen:
                queue.append(path + [(x, y)])
                seen.add((x,y))



def main():
    treasure_map = [[0, 0, 0, 0],
                    [1, 0, 1, 0],
                    [0, 0, 0, 0],
                    [0, 1, 1, 3],]
    print(bfs(treasure_map))

if __name__ == "__main__":
    main()
