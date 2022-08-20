def breadth_first_search(graph: dict, src: str, dst: str) -> bool:
    """Breadth First Search Algorithm

    :param dict graph: _description_
    :param str src: _description_
    :param str dst: _description_
    :return bool: _description_
    """

    visited = []
    queue = [src]

    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.append(current_node)

        if current_node == dst:
            return visited

        for node in graph.get(current_node):
            queue.append(node)


def depth_first_search(graph: dict, src: str, dst: str) -> bool:
    """Depth First Search Algorithm

    :param dict graph: _description_
    :param str src: _description_
    :param str dst: _description_
    :return bool: _description_
    """

    visited = []
    stack = [src]

    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node == dst:
            return visited

        for node in graph.get(current_node):
            stack.append(node)


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e", "j"],
        "e": ["b"],
        "d": [],
        "f": ["d"],
        "j": [],
    }

    print(breadth_first_search(graph, "a", "d"))
    print(depth_first_search(graph, "a", "d"))


def raise_errors(key: str, *arg, **kwargs) -> bool:
    """_summary_

    :param str key: _description_
    :raises ValueError: _description_
    :return bool: _description_
    """
    if arg[0] == key:
        return True
    else:
        if key == "key":
            return False
        else:
            raise ValueError
