maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

visited = set()
path = []

def dfs(x, y):

    if (x, y) == goal:
        path.append((x, y))
        return True

    if (x < 0 or x >= 5 or y < 0 or y >= 5
            or maze[x][y] == 1 or (x, y) in visited):
        return False

    visited.add((x, y))
    path.append((x, y))

    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    for dx, dy in directions:
        if dfs(x + dx, y + dy):
            return True

    path.pop()
    return False


if dfs(start[0], start[1]):
    print("Path Found:")
    print(path)
else:
    print("No Path Found")