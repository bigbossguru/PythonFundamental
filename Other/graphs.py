from string import ascii_letters
from random import sample, randint
from collections import deque

small_letters = ascii_letters[:len(ascii_letters)//2]

# graph = {x: sample(small_letters, randint(5, 10)) for x in small_letters}
GRAPH = {   'a': ['b', 'y', 'd', 't', 'o'],
            'b': ['k', 'x', 'j', 'h', 'n', 'l', 'q'],
            'c': ['o', 'c', 'f', 'p', 'e', 'z'],
            'd': ['r', 'j', 'z', 'w', 'o', 'y', 'm', 'u'],
            'e': ['f', 'o', 'd', 'e', 'q', 'u', 'm'],
            'f': ['o', 'f', 'c', 'a', 'h', 'z', 'l'],
            'g': ['x', 'r', 'p', 'q', 'b', 'w', 's', 'g', 'z'],     
            'h': ['l', 'h', 'c', 'y', 'r', 'x'],
            'i': ['f', 'j', 'c', 'g', 'h', 'u'],
            'j': ['g', 'b', 'q', 'v', 'x', 'j', 'c', 'l'],
            'k': ['c', 'u', 'k', 'r', 'j', 'f'],
            'l': ['h', 'o', 'e', 'p', 'c', 'j', 't', 'x'],
            'm': ['y', 'a', 'b', 'i', 'l', 'c', 'f', 'v', 's', 'n'],
            'n': ['r', 'l', 'e', 'o', 'p', 'n', 'v', 'f'],
            'o': ['v', 't', 'l', 'r', 'x'],
            'p': ['z', 'w', 'y', 'f', 'n', 'b', 'j'],
            'q': ['f', 'q', 'o', 'x', 'w', 'p'],
            'r': ['o', 'n', 'a', 'e', 'v'],
            's': ['x', 't', 'z', 'd', 'r', 'l', 'y', 'i', 'j'],     
            't': ['h', 'k', 'w', 's', 'n'],
            'u': ['r', 'k', 'f', 'a', 'b'],
            'v': ['d', 'g', 'u', 'o', 'n', 'e', 'i', 'h', 'z'],     
            'w': ['f', 'y', 'i', 'd', 'w', 'm', 's'],
            'x': ['m', 'j', 'u', 'n', 'y', 'e', 'l'],
            'y': ['a', 's', 'm', 'd', 't', 'h', 'f', 'k', 'l', 'e'],
            'z': ['f', 'm', 't', 'h', 'g', 'y']
        }

def BFS(graph, root='a', goal='h'):
    queue = deque([root])
    visited = list([root])
    while queue:
        item = queue.popleft()
        print(item, end=' ')

        if item == goal:
            return visited

        for neighbour in graph[item]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def DFS(graph, root='a', goal='h'):
    stack = deque([root])
    visited = list([root])
    while stack:
        item = stack.pop()
        print(item, end=' ')

        if item == goal:
            return visited

        for neighbour in graph[item]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

BFS(GRAPH)
print()
DFS(GRAPH)