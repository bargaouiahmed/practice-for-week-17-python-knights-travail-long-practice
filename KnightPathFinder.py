from collections import deque
from tree import Node

class KnightPathFinder:
    def __init__(self, root):
        self._root = Node(self.chess_to_coord(root))  # Convert chess notation to coordinates
        self._considered_positions = set([self._root.value])  # Store root in a set

    def chess_to_coord(self, pos):
        """Converts chess notation (e.g., 'a1') to board coordinates (e.g., (0, 0))."""
        columns = 'abcdefgh'
        column_index = columns.index(pos[0])  # Get column index from chess notation
        row_index = int(pos[1]) - 1  # Convert row from chess notation to zero-based index
        return (row_index, column_index)

    def coord_to_chess(self, pos):
        """Converts board coordinates (e.g., (0, 0)) to chess notation (e.g., 'a1')."""
        columns = 'abcdefgh'
        return f"{columns[pos[1]]}{pos[0] + 1}"  # e.g., (0, 0) -> 'a1'

    def get_valid_moves(self, pos):
        valid_moves = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for move in knight_moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            # Ensure new positions are on the board and not already considered
            if (0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7 and
                new_pos not in self._considered_positions):
                valid_moves.append(new_pos)
        return valid_moves

    def new_move_positions(self, pos):
        valid_moves = self.get_valid_moves(pos)
        for move in valid_moves:
            self._considered_positions.add(move)  # Mark move as considered
            yield move

    def build_move_tree(self):
        # Create a queue to manage BFS; initially, the queue holds the root
        queue = deque([self._root])

        # While there are nodes to explore:
        while queue:
            current_node = queue.popleft()  # Dequeue the front node
            current_pos = current_node.value  # Get position of this node

            # Generate new valid moves for the current position
            for new_pos in self.new_move_positions(current_pos):
                new_node = Node(new_pos)  # Create a node for each move
                current_node.add_child(new_node)  # Add it as a child
                queue.append(new_node)  # Enqueue the new node for further exploration

    def find_path(self, end_position):
        # Convert chess notation to coordinates for the end position
        end_coord = self.chess_to_coord(end_position)

        # Perform a breadth-first search for the end_position
        queue = deque([self._root])

        while queue:
            current_node = queue.popleft()
            current_pos = current_node.value

            if current_pos == end_coord:
                return self.trace_to_root(current_node)  # Found the end position, trace the path

            # Add children to queue to continue search
            for child in current_node.children:
                queue.append(child)

        return None  # Return None if the end_position is not found

    def trace_to_root(self, end_node):
        path = []
        current_node = end_node

        # Trace back from the end_node to the root using parent links
        while current_node:
            path.append(self.coord_to_chess(current_node.value))  # Convert to chess notation
            current_node = current_node.parent

        return path[::-1]  # Reverse the path to go from root to end

# Instantiate the KnightPathFinder and build the move tree
# finder = KnightPathFinder('a1')  # Start position as chess notation
# finder.build_move_tree()

# Test the find_path method with different positions in chess notation
# print(finder.find_path('c2'))  # => ['a1', 'c2']
# print(finder.find_path('d4'))  # => ['a1', 'c2', 'd4']
# print(finder.find_path('g3'))  # => ['a1', 'b3', 'd5', 'e4', 'g3']
# print(finder.find_path('h8'))  # => ['a1', 'b3', 'c5', 'e6', 'g7', 'h8']
finder2=KnightPathFinder(input('current position: '))
finder2.build_move_tree()
print(finder2.find_path(input('end position: ')))
