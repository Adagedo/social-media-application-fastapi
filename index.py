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



def count_pre(arr, target_pref):
    count = 0
    
    for word in arr:
        for i in range(len(word)):
            for j in range(i, len(word) + 1):
                if j <= len(word)//2 and i <= len(word):
                    if word[i:j] == target_pref:
                        count += 1
    
    return count

m = ["lewsmb","lewrydnve","lewqqm","lewec","lewn","lewb","lewedb"]
print(count_pre(m, "lew"))


def dynamics(arr, target):
    count = 0
    for word in arr:
        if word.index(target) == 0:
            count += 1
    return count 


m = ["lewsmb","lewrydnve","lewqqm","lewec","lewn","lewb","lewedb"]
print(dynamics(m, "lew"))
            

def see(arr1, arr2):
    result = []
    modify_arr2 = ["".join(arr2)]
    print(modify_arr2)
    for word1 in arr1:
        for word2 in ["".join(arr2)]:
            if word2 in word1:
                result.append(word1)
    return result

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
see(words1, words2)

modify_arr2 = ["".join(words2)]


def StringSubs(string, target):
    
    i, j = 0, 0
    s = 0
    n = len(string)
    
    while i < n and j < n + 1:
        if s == len(target):
            if string[i:j] == target:
                return string[i:j]
            return string[i:j]
        if s < len(target):
            if j < n:
                s += j
            j += 1
        if s > len(target):
            s -= i
            i += 1
print(StringSubs("example", "xam"))
"""



"""
travers in the grid using the following ways (row - 1, col + 1) (row, col + 1) and (row + 1, col + 1)
 - initial a counter
 - increament the counter by one for every valid movement in the grid
 - bounce check
 - if no vailid movement return 0
 - if out of bounce return 


up elements:
if i > 0 and i < rows -1:
up = grid[i -1][j]
down = g[i + 1][j]
leeft to right 
if j > 0 and j < cols - 1
left = g[i][j-1]
right = g[i][j + 1]

topleft_daigonal to bottom_right_dai

if i > 0 and j > 0 and i < rows - 1 and j < cols - 1
topleft_dai = g[i -1][j -1]
bottomright = g[i + 1][j + 1]

topright and bottomleft
if i > 0 and j < cols - 1 and i < rows - 1 and j > 0
BLD = g[i + 1][j - 1]
BRD = g[i - 1][j + 1]
"""

def Valid_moves(grid):
    num_of_valid_move = 0
    visited = set()
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore_grid_moves(grid, row, col, visited):
                num_of_valid_move += 1
    return num_of_valid_move


def explore_grid_moves(grid, row, col, visited):
    
    keys = (row, col)
    if keys in visited:
        return False
    visited.add(keys)
    
    RolBounce = 0 <= row < len(grid)
    ColBounce = 0 <= col < len(grid[0])
    
    if not RolBounce or not ColBounce:
        return False
    
    if row > 0 and col < len(grid[0]) - 1 and row < len(grid) - 1 and col > 0:
        if grid[row][col] >= grid[row - 1][col + 1] and grid[0][0] >= grid[row - 1][col + 1]:
            return False
    if col > 0 and row < len(grid[0]) - 1 and col < len(grid[0]) - 1:
        if grid[row][col] >= grid[row][col + 1] and grid[0][0] >= grid[row][col + 1]:
            return False
    if row > 0 and col > 0 and row < len(grid) - 1 and col < len(grid[0]) - 1:
        if grid[row][col] >= grid[row + 1][col + 1] and grid[0][0] > grid[row + 1][col + 1]:
            return False
    
    explore_grid_moves(grid, row - 1, col, visited)
    explore_grid_moves(grid, row, col + 1, visited)
    explore_grid_moves(grid, row + 1, col + 1,visited)
    
    return True

grid = [
    [2, 4, 3, 5],
    [5, 4, 9, 3],
    [3, 4, 2, 11],
    [10, 19, 13, 15]
]

grid2= [
    [3, 2, 4],
    [2, 1, 9],
    [1, 1, 7]
]
response = Valid_moves(grid)
response2 = Valid_moves(grid2)
print(response)
print(response2)
def DungeonGame(game_state):
    player_life = 0
    visited_dungeon = set()
    
    for row in range(len(game_state)):
        for col in range(len(game_state[0])):
            explore_game_state(game_state, row, col, visited_dungeon)
            

def explore_game_state(game_state, row, col, visited_dungeon):
    dungeon_coordinate = (row, col)
    if dungeon_coordinate in visited_dungeon:
        return 0
    visited_dungeon.add(dungeon_coordinate)
    
    RowBounce = 0 <= row < len(game_state)
    ColBounce = 0 <= col < len(game_state[0])
    
    if not RowBounce or ColBounce:
        return 0
    


def sum_of_sub_set(arr):
    
    sums = 0
    
    for i in range(len(arr)):
        for j in range(i, len(arr) + 1):
            if len(arr[i:j]) < len(arr):
                sums += sum(arr[i:j])
    return sums
print(sum_of_sub_set([1,2,3]))
    
    