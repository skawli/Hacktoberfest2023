import random

# Create a maze grid
def create_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]
    return maze

# Check if a cell is valid (within bounds)
def is_valid(cell, width, height):
    x, y = cell
    return 0 <= x < width and 0 <= y < height

# Get neighboring cells
def get_neighbors(cell, width, height):
    x, y = cell
    neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
    neighbors = [neighbor for neighbor in neighbors if is_valid(neighbor, width, height)]
    return neighbors

# Carve passages using depth-first search
def depth_first_search(maze, cell, width, height):
    maze[cell[1]][cell[0]] = 1
    neighbors = get_neighbors(cell, width, height)
    random.shuffle(neighbors)

    for neighbor in neighbors:
        nx, ny = neighbor
        if maze[ny][nx] == 0:
            dx, dy = nx - x, ny - y
            maze[y + dy // 2][x + dx // 2] = 1
            depth_first_search(maze, neighbor, width, height)

# Display the maze
def display_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 0:
                print("█", end="")  # Wall
            else:
                print(" ", end="")  # Path
        print()

# Solve the maze using recursion
def solve_maze(maze, start, end):
    x, y = start
    if start == end:
        return True
    if not is_valid(start, len(maze[0]), len(maze)):
        return False
    if maze[y][x] == 0:
        return False

    maze[y][x] = 2  # Mark the current cell as part of the solution path

    # Check neighboring cells
    if solve_maze(maze, (x + 1, y), end) or \
       solve_maze(maze, (x - 1, y), end) or \
       solve_maze(maze, (x, y + 1), end) or \
       solve_maze(maze, (x, y - 1), end):
        return True

    maze[y][x] = 3  # Mark the current cell as visited but not on the solution path
    return False

if __name__ == "__main__":
    width, height = 21, 21
    maze = create_maze(width, height)
    start, end = (1, 1), (width - 2, height - 2)

    # Generate and display the maze
    depth_first_search(maze, start, width, height)
    display_maze(maze)

    # Solve and display the solution
    solve_maze(maze, start, end)
    display_maze(maze)
