from collections import deque

def solution(map):
    def is_valid(x, y):
        """ Check if the coordinates are within the map boundaries """
        return 0 <= x < width and 0 <= y < height

    def bfs():
        """ Perform a Breadth-First Search to find the shortest path """
        visited = set()
        queue = deque([(0, 0, 1, False)])  # (x, y, steps, has_removed_wall)
        
        while queue:
            x, y, steps, has_removed_wall = queue.popleft()

            # Skip if this state has been visited
            if (x, y, has_removed_wall) in visited:
                continue

            visited.add((x, y, has_removed_wall))

            # Check if the escape pod is reached
            if (x, y) == (width - 1, height - 1):
                return steps

            # Explore adjacent cells
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if is_valid(nx, ny):
                    next_has_removed_wall = has_removed_wall or map[ny][nx] == 1

                    # If the next cell is a wall and we haven't removed a wall yet
                    if map[ny][nx] == 1 and not has_removed_wall:
                        queue.append((nx, ny, steps + 1, True))
                    # If the next cell is not a wall
                    elif map[ny][nx] == 0:
                        queue.append((nx, ny, steps + 1, next_has_removed_wall))

        # Return -1 if no path is found (shouldn't occur as per problem statement)
        return -1

    height = len(map)
    width = len(map[0])

    return bfs()
