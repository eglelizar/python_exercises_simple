from __future__ import annotations

from typing import Generic, Hashable, Iterator, TypeVar

from Graphs.Node import Node


T = TypeVar("T", bound=Hashable)


class Graph(Generic[T]):
    """An insertion-ordered adjacency-list graph with iterative DFS traversal."""

    def __init__(self, directed: bool = False) -> None:
        """Create an empty graph; edges are undirected unless directed is true."""
        self.directed = directed
        self._nodes: dict[T, Node[T]] = {}

    def add_node(self, value: T) -> Node[T]:
        """Add a vertex, or return its existing node when the value is present."""
        node = self._nodes.get(value)
        if node is None:
            node = Node(value)
            self._nodes[value] = node
        return node

    def get_node(self, value: T) -> Node[T]:
        """Return the node for value, raising KeyError when it is not in the graph."""
        return self._nodes[value]

    def has_node(self, value: T) -> bool:
        """Return whether the graph contains a vertex with the given value."""
        return value in self._nodes

    def add_edge(self, source: T, destination: T) -> None:
        """Connect two vertices, creating missing vertices and ignoring duplicate edges."""
        source_node = self.add_node(source)
        destination_node = self.add_node(destination)
        source_node.add_neighbor(destination_node)
        if not self.directed:
            destination_node.add_neighbor(source_node)

    @property
    def nodes(self) -> tuple[Node[T], ...]:
        """Return graph vertices in the order they were first added."""
        return tuple(self._nodes.values())

    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return len(self._nodes)

    def dfs(self, start: T) -> list[T]:
        """Return depth-first preorder reachable from start.

        An explicit stack of neighbor iterators mirrors recursive DFS order while
        avoiding Python's recursion-depth limit. For the reachable component, the
        traversal takes O(V + E) time and O(V) auxiliary space.
        """
        start_node = self.get_node(start)
        visited = {start_node}
        traversal: list[T] = []
        self._traverse_from(start_node, visited, traversal)
        return traversal

    def _traverse_from(
        self, root: Node[T], visited: set[Node[T]], traversal: list[T]
    ) -> None:
        """Append one root's unvisited DFS component to traversal."""
        traversal.append(root.value)
        stack: list[tuple[Node[T], Iterator[Node[T]]]] = [
            (root, iter(root.neighbors))
        ]

        while stack:
            _, neighbors = stack[-1]
            neighbor = next(neighbors, None)
            if neighbor is None:
                stack.pop()
                continue
            if neighbor not in visited:
                visited.add(neighbor)
                traversal.append(neighbor.value)
                stack.append((neighbor, iter(neighbor.neighbors)))

    def dfs_all(self) -> list[T]:
        """Return depth-first preorder covering every component exactly once.

        Vertices that are unreachable from earlier roots become the next roots in
        insertion order. The full traversal takes O(V + E) time and O(V) space.
        """
        visited: set[Node[T]] = set()
        traversal: list[T] = []

        for root in self._nodes.values():
            if root in visited:
                continue
            visited.add(root)
            self._traverse_from(root, visited, traversal)

        return traversal

    def print_graph(self) -> None:
        """Print each vertex and its neighbors in insertion order."""
        for node in self._nodes.values():
            neighbors = ", ".join(repr(neighbor.value) for neighbor in node.neighbors)
            print(f"{node.value!r}: {neighbors}")
