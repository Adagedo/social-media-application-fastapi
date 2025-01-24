from collections import deque
import asyncio
import socket
from keyword import kwlist
import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path
import httpx

"""b
def Undirected_path(edges, NodeA, NodeB):
    graph = BuildGraph(edges)
    return haspath(graph, NodeA, NodeB, visited=set())

def haspath(graph, node, src, visited):
    if node == src:
        return True
    
    if node in visited:
        return False
    visited.add(node)
    
    for neighbor in graph[node]:
        if haspath(graph, neighbor, src):
            return True
        
    return False



def BuildGraph(edges):
    
    graph = {}
    
    for edge in edges:
        [a, b] = edges
        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

graph = {
    3:[],
    4: [6],
    6:[4, 5, 7, 8],
    8:[6],
    7:[6],
    5:[6],
    1:[2],
    2:[1]
}

def Connected_Component(graph):
    
    count = 0
    visited = set()
    for node in graph.keys():
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, node, visited):
    
    if node in visited:
        return False
    visited.add(node)
    
    for neighbors in graph[node]:
        explore(graph, neighbors, visited)
    
    return True


print(Connected_Component(graph=graph))

def Larget_component_count(graph):
    largest = 0
    visited = set()
    
    for node in graph.keys():
        size = Explore(graph, node, visited)
        if size > largest:
            largest = size
    return largest
    

def Explore(graph, node, visited):
    count = 1
    
    if node in visited:
        return 0
    visited.add(node)
    
    for neighbors in graph[node]:
        count  += Explore(graph, neighbors, visited)
    
    return count

print(Larget_component_count(graph=graph))


def shortestPath(graph, nodeA, nodeB):
    queue = deque([[nodeA, 0]])
    while len(queue) > 0:
        current = queue.popleft()
        [node, distance] = current
        
        if node == nodeB:
            return distance
        
        for neighbors in graph[node]:
            queue.append([neighbors, distance + 1])
            

result = shortestPath(graph, 6, 4)
print(result)

def Number_of_island(grid):
    count = 0
    visited = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore_grid(grid, row, col, visited)
            if size > count:
                count = size
    return count

    


def explore_grid(grid, row, col, visited):
    
    size = 1

    coordinate = f"{row},{col}"
    
    if coordinate in visited:
        return 0
    visited.add(coordinate)
    
        
    RowBounce = 0 <= row < len(grid)
    colbounce = 0 <= col < len(grid[0])
    
    if not RowBounce or not colbounce:
        return 0
    

    
    if grid[row][col] == 0:
        return 0
    
    size += explore_grid(grid, row + 1, col, visited)
    size += explore_grid(grid, row - 1, col, visited)
    size += explore_grid(grid, row, col + 1, visited)
    size += explore_grid(grid, row, col - 1, visited)
    
    return size

grid = [
    [1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0]
]


result = Number_of_island(grid)
print(result)

str_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        ]
def combination(arr, code):
    if code <=1:
        return []
    result = []
    
    def depthFirst(startIndex, path):
        if startIndex == code:
            result.append("".join(path))
            return 
        
        for char in arr:
            path.append(str(char))
            depthFirst(startIndex + 1, path)
            path.pop()
    
    depthFirst(0, [])
    return result

print(combination(str_,2))



def convert(stringOne, stringtwo, i=0, j=0) -> int:
    if stringOne == "":
        return stringtwo  - i
    if stringtwo == "":
        return stringOne - j
    
    if stringOne == stringtwo:
        return 0

    if stringOne[i] == stringtwo[j]:
        return convert(stringOne, stringtwo, i + 1, j + 1)
    
    else:
        OperationOne = convert(stringOne, stringtwo, i + 1, j + 1)
        OperationTwo= convert(stringOne, stringtwo, i + 1, j)
        OperationThree = convert(stringOne, stringtwo, i, j + 1)
        
        return 1 + min(OperationOne, OperationTwo, OperationThree)
    

stringOne = "execution"
stringTwo = "executio"

def SubArrSum(arr, target):
    
    i, j, s, n = 0, 0, 0, len(arr)
    
    while i < n and j < n + 1:
        if s == target:
            return arr[i:j]
        if s < target:
            if j < n:
                s += arr[j]
            j += 1
        if s > target:
            s -= arr[i]
            i += 1
    return []

arr = [4, 5, 6,2 ,1, 9, 8, 7]
target = 20

response = SubArrSum(arr, target)
print(response)

backtracking template

"""


 
def Min_steps_tabulation(stringOne, stringtwo):
    table = [[0 for _ in range(len(stringtwo) + 1)] for _ in range(len(stringOne) + 1)]

    
    for i in range(len(stringOne)):
        for j in range(len(stringtwo)):
            if i < len(stringOne) and j < len(stringtwo):
                if stringOne[i] == stringtwo[j]:
                    table[i + 1][j + 1] = table[i][j]
            else:
                if i <= len(stringOne) and j <= len(stringtwo):
                    Deletion = 1 + table[i + 1][j]
                    swap = 1 + table[i + 1][j + 1]
                    insertion = 1 + table[i][j + 1]
                    table[i + 1][j + 1] =  1 + min(Deletion, insertion, swap)
    print(table)
    return table[-1][-1]


class Node:
    
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


class Bst:
    
    def __init__(self):
        self.root = None
    
    def search(self, node):
        
        if not node:
            raise Exception("node cannot be None")
        
        temp_node = self.root
        while temp_node:
            if temp_node.node is None:
                break
            if node < temp_node.node:
                temp_node = temp_node.left
            if node > temp_node.node:
                temp_node = temp_node.right
            if node == temp_node.node:
                return True
        return False
    
    def insert(self, node):
        new_node = Node(node)
        if self.root is None:
            self.root = new_node
            return self
        
        temp_node = self.root
        
        while True:
            if new_node == temp_node:
                raise Exception("can't v duplicate of nodes")
            
            if new_node.node < temp_node.node:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return self
                temp_node = temp_node.left
                return self
            if new_node.node > temp_node.node:
                if temp_node.right is None:
                    temp_node.right = new_node
                    return self
                temp_node = temp_node.right
                return self
    def __repr__(self):
        
        def BreathFirst(root):
            queue = deque([root])
            result = []
            while len(queue) > 0:
                current_node = queue.popleft()
                result.append(current_node.node)
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            return result 
        
        nodes = BreathFirst(self.root)
        return str(nodes)          
            
                    

tree = Bst()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(9)
tree.insert(7)
print(tree.search(3))
print(tree)

a = "personification"
b = "backtracking"
x="name"
y="same"

def min_stesp(stringone, stringtwo, i=0, j=0):
    if i == len(stringone):
        return len(stringtwo) - j
    if j == len(stringtwo):
        return len(stringone) - i
    
    if stringone[i] == stringtwo[j]:
        return min_stesp(stringone, stringtwo, i + 1, j + 1)
    else:
        OperationOne = min_stesp(stringone, stringtwo, i + 1, j + 1)
        OperationTwo = min_stesp(stringone, stringtwo, i + 1, j)
        OperationThree = min_stesp(stringone, stringtwo, i, j + 1)
        return  1 + min(OperationOne, OperationThree, OperationTwo)
    

print("Nums operation",min_stesp("name", "jane"))



