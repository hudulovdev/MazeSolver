class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.path = []

    def solve(self, start, goal):
        self._dfs(start, goal)
        return self.path

    def _dfs(self, curr, goal):
        if curr == goal:
            self.path.append(curr)
            return True

        row, col = curr
        if (
            row < 0 or row >= self.rows
            or col < 0 or col >= self.cols
            or self.maze[row][col] == '#'  # Wall
            or self.visited[row][col]
        ):
            return False

        self.visited[row][col] = True
        self.path.append(curr)

        # Explore neighboring cells
        if (
            self._dfs((row - 1, col), goal)  # Up
            or self._dfs((row + 1, col), goal)  # Down
            or self._dfs((row, col - 1), goal)  # Left
            or self._dfs((row, col + 1), goal)  # Right
        ):
            return True

        # If none of the neighboring cells lead to the goal, backtrack
        self.path.pop()
        return False


# Example usage:
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '#', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
]

solver = MazeSolver(maze)
start = (1, 1)  # Start position
goal = (5, 5)  # Goal position
path = solver.solve(start, goal)

if path:
    print("Path found:")
    for position in path:
        print(position)
else:
    print("No path found.")
