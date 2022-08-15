from typing import List, TypeVar


T = TypeVar("T")


class TreeNode:
    def __init__(self, data: T) -> None:
        self.data = data
        self.left = None
        self.right = None


def binary_tree_insert(node: TreeNode, data: T) -> None:
    if node is None:
        node = TreeNode(data)
    else:
        if data < node.data:
            if node.left is not None:
                binary_tree_insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right is not None:
                binary_tree_insert(node.right, data)
            else:
                node.right = TreeNode(data)


def pre_order_traversal(node: TreeNode, output: List[T]) -> List[T]:
    if node is not None:
        output.append(node.data)
        if node.left:
            pre_order_traversal(node.left, output)
        if node.right:
            pre_order_traversal(node.right, output)
        return output


def post_order_traversal(node: TreeNode, output: List[T]) -> List[T]:
    if node is not None:
        if node.left:
            post_order_traversal(node.left, output)
        if node.right:
            post_order_traversal(node.right, output)
        output.append(node.data)
        return output


def in_order_traversal(node: TreeNode, output: List[T]) -> List[T]:
    if node is not None:
        if node.left:
            in_order_traversal(node.left, output)
        output.append(node.data)
        if node.right:
            in_order_traversal(node.right, output)
        return output


def binary_search_tree(node: TreeNode, value: T) -> T:
    if node is not None:
        if value == node.data:
            return node.data
        if value < node.data:
            return binary_search_tree(node.left, value)
        else:
            return binary_search_tree(node.right, value)


if __name__ == "__main__":
    tree_root: TreeNode = TreeNode(45)

    binary_tree_insert(tree_root, 33)
    binary_tree_insert(tree_root, 50)
    binary_tree_insert(tree_root, 47)
    binary_tree_insert(tree_root, 67)
    binary_tree_insert(tree_root, 36)
    binary_tree_insert(tree_root, 22)

    values: List[T] = pre_order_traversal(tree_root, [])
    print("pre_order_traversal: ", values)
    values: List[T] = post_order_traversal(tree_root, [])
    print("post_order_traversal: ", values)
    values: List[T] = in_order_traversal(tree_root, [])
    print("in_order_traversal: ", values)
    print(binary_search_tree(tree_root, 36))
