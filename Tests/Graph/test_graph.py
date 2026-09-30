import pytest

from Graphs.Graph import Graph
from Graphs.Node import Node


def test_node_stores_its_value_and_adds_each_neighbor_once():
    first = Node("first")
    second = Node("second")

    assert first.value == "first"
    assert first.add_neighbor(second) is True
    assert first.add_neighbor(second) is False
    assert list(first.neighbors) == [second]


def test_add_node_is_idempotent_and_get_node_returns_the_same_node():
    graph = Graph[str]()

    first = graph.add_node("A")

    assert graph.add_node("A") is first
    assert graph.get_node("A") is first
    assert graph.has_node("A")
    assert len(graph) == 1


def test_get_node_raises_key_error_for_a_missing_value():
    graph = Graph[str]()

    with pytest.raises(KeyError):
        graph.get_node("missing")


def test_undirected_edges_are_added_in_both_directions_and_deduplicated():
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "B")

    assert [node.value for node in graph.get_node("A").neighbors] == ["B"]
    assert [node.value for node in graph.get_node("B").neighbors] == ["A"]
    assert len(graph) == 2


def test_directed_edges_only_connect_source_to_destination():
    graph = Graph[str](directed=True)
    graph.add_edge("A", "B")

    assert [node.value for node in graph.get_node("A").neighbors] == ["B"]
    assert list(graph.get_node("B").neighbors) == []


def test_dfs_visits_in_recursive_depth_first_order():
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    assert graph.dfs("A") == ["A", "B", "C", "D"]


def test_dfs_handles_cycles_self_loops_and_duplicate_edges():
    graph = Graph[str]()
    graph.add_edge("A", "A")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.add_edge("A", "B")

    assert graph.dfs("A") == ["A", "B", "C"]


def test_dfs_only_visits_nodes_reachable_from_start():
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_node("isolated")

    assert graph.dfs("A") == ["A", "B"]


def test_dfs_all_covers_disconnected_components_in_insertion_order():
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_node("isolated")
    graph.add_edge("C", "D")

    assert graph.dfs_all() == ["A", "B", "isolated", "C", "D"]


def test_empty_graph_traversals_are_empty():
    graph = Graph[str]()

    assert graph.dfs_all() == []
    assert graph.nodes == ()


def test_dfs_handles_a_path_longer_than_python_recursion_limit():
    graph = Graph[int]()
    path_length = 2_000
    for value in range(path_length - 1):
        graph.add_edge(value, value + 1)

    assert len(graph.dfs(0)) == path_length


def test_print_graph_formats_vertices_and_neighbors(capsys):
    graph = Graph[str]()
    graph.add_edge("A", "B")
    graph.add_node("isolated")

    graph.print_graph()

    assert capsys.readouterr().out == "'A': 'B'\n'B': 'A'\n'isolated': \n"


def test_bfs_level_order_traversal():
    """Verify that BFS explores nodes level by level in correct order."""
    g = Graph[str](directed=False)
    # Constructing a simple tree-like graph structure
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")

    bfs_result = g.bfs("A")

    # Root must be first
    assert bfs_result[0] == "A"
    # Level 1 nodes must follow (B and C in some valid order depending on insertion)
    assert set(bfs_result[1:3]) == {"B", "C"}
    # Level 2 nodes must follow (D and E)
    assert set(bfs_result[3:]) == {"D", "E"}


def test_bfs_nonexistent_start_node_raises_key_error():
    """Verify that starting BFS from an invalid node raises KeyError."""
    g = Graph[int](directed=False)
    g.add_node(1)

    with pytest.raises(KeyError):
        g.bfs(99)
