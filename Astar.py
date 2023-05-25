from queue import PriorityQueue

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self, other):
        return self.f < other.f
    

def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    openL = PriorityQueue()
    closedL = []

    openL.put((0, start_node))  # Add start node to the priority queue

    while not openL.empty():
        current_node = openL.get()[1]  # Get the node with the lowest priority (smallest f value)
        closedL.append(current_node)

        if current_node == end_node:
            print("End found!")
            path = []
            curr = current_node
            while curr:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if (
                node_position[0] > (len(maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(maze[len(maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closedL:
                continue

            child.g = (
                current_node.g
                + abs(child.position[0] - current_node.position[0])
                + abs(child.position[1] - current_node.position[1])
            )
            child.h = (
                abs(end_node.position[0] - current_node.position[0])
                + abs(end_node.position[1] - current_node.position[1])
            )
            child.f = child.g + child.h

            # Check if the child is already in the priority queue with a lower g value
            found = False
            for item in openL.queue:
                if child == item[1] and child.g > item[1].g:
                    found = True
                    break
            if found:
                continue

            openL.put((child.f, child))  # Add the child to the priority queue

    return "No possible path"


def main():
    maze = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == "__main__":
    main()
    