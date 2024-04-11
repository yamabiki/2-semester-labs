def shortest_path(matrix, start, destination):
    rows = len(matrix)
    cols = len(matrix[0])

    if not (0 <= start[0] < cols and 0 <= start[1] < rows) or not (
            0 <= destination[0] < cols and 0 <= destination[1] < rows):
        return -1

    if matrix[start[0]][start[1]] == 0 or matrix[destination[0]][destination[1]] == 0:
        return -1

    queue = [(start[0], start[1], 0)]
    queue_index = 0

    visited = set()

    while queue_index < len(queue):
        x, y, dist = queue[queue_index]
        queue_index += 1

        if (x, y) == destination:
            return dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and matrix[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
                visited.add((nx, ny))

    return -1


def read_input_file(inputfile):
    with open(inputfile, 'r') as file:
        lines = file.readlines()
        start = tuple(map(int, lines[0].strip().split(', ')))
        end = tuple(map(int, lines[1].strip().split(', ')))
        matrix = [list(map(int, line.strip()[1:-1].split())) for line in lines[3:]]
    return start, end, matrix

def write_output_file(outputfile, shortest_distance):
    with open(outputfile, 'w') as file:
        file.write(str(shortest_distance))