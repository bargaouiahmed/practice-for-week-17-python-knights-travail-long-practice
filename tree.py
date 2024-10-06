from collections import deque

class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent_node):
        if self._parent:  # Remove from current parent's children
            self._parent.remove_child(self)
        self._parent = parent_node
        if parent_node:  # Only add to new parent's children if it's not None
            parent_node.add_child(self)

    def add_child(self, child):
        if child is None:
            return
        if child not in self._children:
            self._children.append(child)
            if child._parent is not self:  # Set child's parent to this node
                child.parent = self

    def remove_child(self, child):
        if child in self._children:
            self._children.remove(child)
            child.parent = None  # Use the setter to properly reset the parent

    def depth_search(self, target):
        if self.value == target:
            return self
        for child in self.children:
            result = child.depth_search(target)
            if result:
                return result
        return None

    def breadth_search(self, target):
        queue = deque([self])  # Use a deque for efficient popping from the front
        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return current_node
            queue.extend(current_node.children)  # Add children to the queue
        return None  # Return None if the target is not found
