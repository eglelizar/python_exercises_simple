from __future__ import annotations

from typing import Generic, Hashable, TypeVar


T = TypeVar("T", bound=Hashable)


class Node(Generic[T]):
    """A graph vertex and its insertion-ordered set of adjacent vertices."""

    __slots__ = ("value", "neighbors")

    def __init__(self, value: T) -> None:
        """Create a vertex with the given hashable value and no neighbors."""
        self.value = value
        self.neighbors: dict[Node[T], None] = {}

    def add_neighbor(self, neighbor: Node[T]) -> bool:
        """Add a neighbor once, returning whether a new edge was recorded."""
        if neighbor in self.neighbors:
            return False
        self.neighbors[neighbor] = None
        return True

    def __repr__(self) -> str:
        """Return a representation useful when inspecting graph structure."""
        return f"Node({self.value!r})"
