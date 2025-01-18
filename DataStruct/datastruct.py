"""
daynamic
"""

def fib(n):
    table = [0 for x in range(n + 1)]
    table[1] = 1
    
    for i in range(len(table)):
        if i + 1 < len(table):
            table[i + 1] += table[i]
        if i + 2 < len(table):
            table[i + 2] += table[i]
    
    return table[n]

print(fib(6))

def Grid(m, n):
    
    table = [[0 for x in range(n + 1)] for x in range(m + 1)]
    table[1][1] = 1
    
    for i in range(len(table)):
        for j in range(len(table)):
            if i + 1 < len(table):
                table[i + 1][j] += table[i][j]
            if j + 1 < len(table):
                table[i][j + 1] += table[i][j]
    return table[m][n]

print(Grid(3,3))
print(Grid(10,10))

def canSum(arr, target):
    
    table = [False for x in range(target + 1)]
    table[0] = True
    
    for i in range(target):
        if table[i] == True:
            for nums in arr:
                if i + nums < len(table):
                    table[i + nums] = True
    return table[target]

print(canSum([1,2,3,4,5], 7))

def Howsum(arr, target):
    
    table = [None for x in range(target + 1)]
    table[0] = []
    
    for i in range(target):
        if table[i] is not None:
            for num in arr:
                if i + num < len(table):
                    table[i +num] = [*table[i], num]
    return table[target]

print(Howsum([1,2,3,4,5], 7))

def BestSum(arr, target):
    table = [None for x in range(target+ 1)]
    table[0] = []
    
    for i in range(target):
        if table[i] is not None:
            for num in arr:
                if i + num < len(table):
                    current_combination = [*table[i], num]
                    if table[i + num] is None or len(table[i + num]) > len(current_combination):
                        table[i + num] = current_combination
    return table[target]


print(BestSum([1,2,3,4,5], 7))
print(BestSum([5, 10, 20, 25, 50, 75], 1000))

def canConst(arr, target):
    table = [False for x in range(len(target) + 1)]
    table[0] = True
    
    for i in range(len(target)):
        if table[i] == True:
            for word in arr:
                if word in target:
                    if i + len(word) < len(table):
                        if target[i:i + len(word)] == word:
                            table[i + len(word)] = True
    return table[len(target)]

print(canConst(["pur", "pu", "r", "p", "ple", "le"], "purple"))
print(canConst(["ja", "ue", "ugf", "tee"],"samuel"))

def countConst(arr, target):
    
    table = [0 for x in range(len(target) + 1)]
    table[0]= 1
    
    for i in range(len(target)):
        if table[i] is not 0:
            for word in arr:
                if word in target:
                    if i + len(word) < len(table):
                        if target[i :i + len(word)] == word:
                            table[i + len(word)] += table[i]
    return table[len(target)]

print(countConst(["pur", "pu", "r", "p", "ple", "le"], "purple"))
print(countConst(["ja", "ue", "ugf", "tee"],"samuel"))

def HowConst(arr, target):
    table = [None for x in range(len(target) + 1)]
    table[0] = []
    
    for i in range(len(target)):
        if table[i] is not None:
            for word in arr:
                if word in target:
                    if i + len(word) < len(table):
                        if target[i: i + len(word)] == word:
                            table[i + len(word)] = [*table[i], word]
    return table[len(target)]

print(HowConst(["pur", "pu", "r", "p", "ple", "le"], "purple"))
print(HowConst(["ja", "ue", "ugf", "tee"],"samuel"))

def BestConst(arr, target):
    table = [None for x in range(len(target) + 1)]
    table[0] = []
    
    for i in range(len(target)):
        if table[i] is not None:
            for word in arr:
                if word in target:
                    if i + len(word) < len(table):
                        if target[i: i + len(word)] == word:
                            combinations = [*table[i], word]
                            if table[i + len(word)] is None or len(table[i + len(word)]) > len(combinations):
                                table[i + len(word)] = combinations
    
    return table[len(target)]
print(BestConst(["pur", "pu", "r", "p", "ple", "le"], "purple"))
print(BestConst(["ja", "ue", "ugf", "tee"],"samuel"))


def substrings(string1, string2, idx1=0, idx2=0):
    if idx1 == len(string1) or idx2 == len(string2):
        return 0
    if string1[idx1] == string2[idx2]:
        return 1 + substrings(string1, string2, idx1 + 1, idx2 + 1)

    else :
        OptionOne = substrings(string1, string2, idx1 + 1, idx2)
        OptionTwo = substrings(string1, string2, idx1, idx2 + 1)
        return max(OptionOne, OptionTwo)
    

def LongestSubs(stringOne, stringTwo):
    
    table = [[0 for x in range(len(stringOne) + 1)] for x in range(len(stringTwo) + 1)]
    table[1][1] = 1
    total = 0
    
    for i in range(len(stringOne)):
        for j in range(len(stringTwo)):
           # print(f" at 'i':{stringOne[j]} and at 'j': {stringTwo[j]}"
            if i + 1 < len(table) - 1:
                if stringOne[i + 1] == stringTwo[j]:
                    table[i + 1][j] = 1
    
            if j + 1 < (len(table[0]) - 1):
                if stringOne[i] == stringTwo[j + 1]:
                    table[i][j + 1] = 1
                    
    
    for arr in table:
        _sum = sum(arr)
        total += _sum
    return total


print(LongestSubs("purple", "samuel"))
print(LongestSubs("name", "same"))
print(LongestSubs("passion", "passion"))
print(LongestSubs("john", "boej"))


"""dynamic array"""

class Nodes:
    
    def __init__(self, node):
        self.node = node 


class Dynamic:
    def __init__(self):
        self.arr = []
        self.len = len(self.arr)
        self.capacity = 0
    
    def insert(self, node):
        new_node = Nodes(node)
        self.capacity += 1
        self.arr.append(new_node.node)
    
    def __str__(self):
        return str(self.arr)
    
    def __len__(self):
        return self.len


d = Dynamic()
d.insert(9)
d.insert(8)
d.insert(33)
d.insert(12)
d.insert(100)

print(d)
spam = "()[]{}"

def check_valid_bkt(bkt):
    stack = []

         


"""
the tower of hanoi game
 - start with a pile of dicks on the first peg 
 - the goal is too move the dicks to right most pile 
 - at each move you can the top of each pile to any other pile with restriction,
   with no dicks be place ontop of a smaller disk 
"""


class Books:
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.contarr = []
        
    class Content:
        def __init__(self):
            self.content = []
    
        def __str__(self):
            return str(self.content)
        
    
    def Add_content(self, _cont):
        #global content
        content = self.Content()
        content.content.append(_cont)
        self.contarr.append(*content.content)
        return self.contarr
        
    
    def __str__(self):
        return str({"title":self.title, "content":[self.content, *self.contarr]})

        
class Lib:
    def __init__(self):
        self.DataBase = []
        
    def Add(self, book:classmethod):
        self.DataBase.append({"title":book.title, "content":[book.content, *book.contarr]})
        
    def Remove_Book_From_Lib(self, title) -> None:
        for books in self.DataBase:
            if books["title"] == title:
                self.DataBase.remove(books)
                print(f"book with the {title} is removed!!!")
        return "Book Not found "
     
    def Search_Book_In_Lib(self, title):
        for book in self.DataBase:
            if book["title"] == title:
                return book
            
            
    def __repr__(self):
        return str(self.DataBase)
    

lib = Lib()

BookOne = Books("new title", "content is new now")
BookOne.Add_content("this is the page of the books that tell the root of the story, And alot has happend in the book")
BookOne.Add_content("Once upon a time in a little town in kano, their lived a farmer who is marride to 3 women. stay tune for more page")

lib.Add(BookOne)

BookTwo = Books("harry potter", "this is the story about harry potter")
lib.Add(BookTwo)

Book3 = Books("sorrows", "this is the introduction")
lib.Add(Book3)
Book3.Add_content("this is about a guy who got rich over a night and he changed based on his personalities")
Book3.Add_content("He the meet a realy good gut who is not that good tho, but he realy helped him in his management of his wealth")

lib.Remove_Book_From_Lib("new title")

print(lib)


