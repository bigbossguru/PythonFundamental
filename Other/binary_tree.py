from collections import deque
import random

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, *args) -> None:
        self.root: Node = Node(args[0])
        if args:
            for arg in args[1:]:
                self.iter_insert(arg)
            


    def iter_insert(self, val) -> None:
        if self.root is None:
            self.root = Node(val)
            return

        current: Node = self.root
        parent: Node = None

        while current:
            parent = current

            if val < current.val:
                current = current.left
            else:
                current = current.right
        
        if val < parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)
    
    
    @staticmethod
    def preorder(root: Node, sequence: list):
        if root is None:
            return 
        sequence.append(root.val)
        Tree.preorder(root.left, sequence)
        Tree.preorder(root.right, sequence)

    @staticmethod
    def inorder(root: Node, sequence: list):
        if root is None:
            return
        else:
            Tree.inorder(root.left, sequence)
            sequence.append(root.val)
            Tree.inorder(root.right, sequence)

    @staticmethod
    def postorder(root: Node, sequence: list):
        if root is None: return 
        else:
            Tree.postorder(root.left, sequence)
            Tree.postorder(root.right, sequence)
            sequence.append(root.val)

    @ staticmethod
    def iter_inorder(root: Node):
        if root is None: return
        res = []
        stack  = deque()
        current: Node = root
        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                res.append(current.val)
                current = current.right

        return res
    
    @staticmethod
    def iter_preorder(root: Node) -> list:
        if root is None: return
        res = []
        stack = deque()
        current: Node = root
        stack.append(root)

        while stack:
            current = stack.pop()
            res.append(current.val)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        return res


    @staticmethod
    def iter_postorder(root: Node):
        if root is None: return
        res = []
        stack = deque()
        current = root
        last_node = None
        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                peekNode: Node = stack[-1]
                if peekNode.right is not None and last_node != peekNode.right:
                    current = peekNode.right
                else:
                    res.append(peekNode.val)
                    last_node = stack.pop()

        return res


    def __repr__(self) -> str:
        result = []
        Tree.preorder(self.root, result)
        return ' '.join(map(str, result))
        

res_post = []
res_pre = []
res_in = []
t = Tree(60, 97, 85, 35, 36, 9, 25, 58, 50, 29, 79, 67)

# t.iter_insert(5)
# t.iter_insert(15)
# t.iter_insert(3)
# t.iter_insert(7)
# t.iter_insert(12)
# t.iter_insert(23)


print('-'*30)
print('Recursively Tree Traversal'.upper())
print('-'*30)
t.postorder(t.root, res_post)
t.preorder(t.root, res_pre)
t.inorder(t.root, res_in)
print('Post order traverse: ', res_post)
print('Pre order traverse: ', res_pre)
print('In order traverse: ', res_in)
print('-'*30)
print('Iteratively Tree Traversal'.upper())
print('-'*30)
print('Post order traverse: ', t.iter_postorder(t.root))
print('Pre order traverse: ', t.iter_preorder(t.root))
print('Pre order traverse: ', t.iter_inorder(t.root))

# print(random.sample(range(100), 12))