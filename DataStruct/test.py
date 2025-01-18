

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


def crack(arr, code):
    string_code = str(code)
    if len(string_code) <= 1:
        return [string_code]
    result = []
    
    def dfs(index, path):
        if index == len(string_code):
            result.append("".join(path))
            print(result)
            return
        
        for num in arr:
            path.append(str(num))
            dfs(index + 1, path)
            path.pop()
        
    dfs(0, [])
    for password in result:
        if password == string_code:
            return True
    return False

arr = [0,1,2,3,4,5,6,7,8,9]
code = 2
results = crack(arr=arr, code=code)
print(results)

def combination(Number, keypad):
    string_nums = str(Number)
    if string_nums is None:
        return []
    
    result = []
    
    def dfs(index, path):
        if index == len(string_nums):
            result.append("".join(path))
            return 
        
        for char in keypad[string_nums[index]]:
            path.append(char)
            dfs(index + 1, path)
            path.pop()
    dfs(0, [])
    return result 

num = 23
digit_to_char = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jik",
    "6": "mno", "7": "pqrs", "8": "tvs", "9": "wxyz"
}
response = combination(23, digit_to_char)
print(response)

def crack(constrains, code):
    if code is not str:
        raise TypeError("code must be s string")

    result = []
    
    def dfs(index, path):
        if index == code:
            result.append("".join(path))
            return 
        
        for char in constrains:
            path.append(char)
            dfs(index + 1, path)
            path.pop()
    dfs(0, [])
    
    return result

strings_consts = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%^&*()_+"

response = crack(strings_consts, )
print(response)

class Book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def info(self):
        print(f"title: {self.title}")
        print(f"author:{ self.author}")
        print(f"year: {self.year}")
        
class FictionalBook(Book):
    
    def __init__(self, title, author, year, gener):
        super().__init__(title, author, year)
        self.gener = gener
        
    def info(self):
        super().info()
        print("gener:", self.gener)
    
class NoneFictionalBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic
    
    def info(self):
        super().info()
        print(f"topic:{self.topic}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    def displayBooks(self):
        print(self.books)

mainBook = Book("harrypoter","Perterson", "2003" )
finctional = FictionalBook("star wars", "john james", "2009", "adventure")
Nonfictions = NoneFictionalBook("Geograpy wild", "bois gone", "2006", "wild life in action")

mainBook.info()
finctional.info()
Nonfictions.info()

l = Library()
l.add_book(mainBook)
l.add_book(FictionalBook)

l.displayBooks()
  


# fib 
def fib(n,memo=None):
    if memo == None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] =  fib(n -1, memo) + fib(n- 2, memo)
    return memo[n]
print(fib(100))

def grid(n,m, memo=None):
    if memo is None:
        memo={}
    keys = f"{n},{m}"
    if keys in memo:
        return memo[keys]
    
    if n == 1 or m ==1:
        return 1
    if n == 0 and m == 0:
        return 0
    memo[keys] = grid(n-1, m, memo) + grid(n, m-1, memo)
    return memo[keys]

print(grid(50, 50))

def sanSum(arr, target):
    if target < 0 :
        return False
    if target == 0:
        return True
    for num in arr:
        remainder = target - num
        remainder_depth = sanSum(arr, remainder)
        if remainder_depth:
            return True
    
    return False

print(sanSum([1,2,3,4,5], 7))

def HowSum(arr, target, memo= None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    if target < 0:
        return 
    if target == 0:
        return []
    
    for nums in arr:
        remainder = target-nums
        remainder_values = HowSum(arr, remainder, memo)
        if remainder_values is not None:
            combinations = [nums, *remainder_values]
            if combinations:
                memo[target] = combinations
                return memo[target]
      
print(HowSum([5, 10, 25, 50, 75], 100))

def BestSum(arr, target):
    if target <0:
        return 
    if target == 0:
        return []
    
    shortestCombination = None
    
    for nums in arr:
        remainder = target -nums
        remainder_values = BestSum(arr, remainder)
        if remainder_values is not None:
            combination = [nums, *remainder_values]
            if combination:
                if shortestCombination is None or len(combination) < len(shortestCombination):
                    shortestCombination = combination
    return shortestCombination
print(BestSum([1,2,3,4,5], 7))
print(BestSum([5, 10, 25, 50, 75], 100))
name = "samuel"
pre = name.index("sam")
print(name[len("sam"):])
def Canconstruct(arr, target):
    if target == "":
        return True
    
    for word in arr:
        if word in target:
            preffix = target.index(word)
            if preffix is 0:
                suffixs = target[len(word):]
                remainderCombination = Canconstruct(arr, suffixs)
                if remainderCombination:
                    return True

    
    return False

print(Canconstruct(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel"))
    

def HowConst(arr, target):
    if target == "":
        return []
    
    for word in arr:
        if word in target:
            preffix = target.index(word)
            if preffix is 0:
                suffixs = target[len(word):]
                reminder_combination = HowConst(arr, suffixs)
                if reminder_combination is not None:
                    result_combination = [word, *reminder_combination]
                    return result_combination
    return 

print(HowConst(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel"))

def _HowConsts_(arr, target):
    
    if target == "":
        return 1
    total = 0
    for word in arr:
        if word in target:
            preffix = target.index(word)
            if preffix == 0:
                suffix = target[len(word):]
                remainder_combinations = _HowConsts_(arr, suffix)
                if remainder_combinations is not None:
                    total += remainder_combinations
    return total
response = _HowConsts_(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel")    
print(response)

def allconstruct(arr, target):
    if target == "":
        return [[]]

    result = []
    
    for word in arr:
        if word in target:
            preffix = target.index(word)
            if preffix == 0:
                suffixs = target[len(word):]
                combination = allconstruct(arr, suffixs)
                if combination:
                    combination_values = lambda y, x: [y, *x]
                    result .append(combination_values(word, combination))
    return result
                    

result_response = allconstruct(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel")   
print(result_response) 
    
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


def Grid(m,n):
    table = [[0 for x in range(m + 1)] for x in range(n + 1)]
    table[1][1] = 1
    
    for i in range(len(table)):
        for j in range(len(table)):
            if i + 1 < len(table):
                table[i + 1][j] += table[i][j]
            if j + 1 < len(table):
                table[i][j + 1] += table[i][j]
    return table[m][n]
print(Grid(3,3))
print(Grid(18, 18))

def canSum(arr, target):
    table = [False for x in range(target + 1)]
    table[0] = True
    
    for i in range(len(table)):
        if table[i] == True:
            for num in arr:
                if i + num < len(table):
                    table[i + num] = True
                    
    
    return table[target]

print(canSum([1,2,3,4,5], 7))
print(canSum([8, 9, 10, 16], 7))
print(canSum([7, 6, 8, 5, 10], 20))

def howSum(arr, target):
    
    table = [None for x in range(target + 1)]
    table[0] = []
    
    for i in range(target):
        if table[i] is not None:
            for num in arr:
                if i + num < len(table):
                    table[i + num] = [*table[i], num]
    return table[target]
print(howSum([1,2,3,4,5], 7))
print(howSum([8, 9, 10, 16], 7))
print(howSum([7, 6, 8, 5, 10], 20))
print(howSum([20, 50, 75, 25], 100))

def BestSum(arr, target):
    table = [None for x in range(target + 1)]
    table[0] = []
    
    for i in range(target):
        if table[i] is not None:
            for num in arr:
                if i + num < len(table):
                    combination = [*table[i], num]
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination
    return table[target] if True else []

print(BestSum([1,2,3,4,5], 7))
print(BestSum([8, 9, 10, 16], 7))
print(BestSum([7, 6, 8, 5, 10], 20))
print(BestSum([20, 50, 75, 25], 100))

def canConst(arr, target):
    table = [False for x in range(len(target) + 1)]
    table[0] = True
    
    for i in range(len(target)):
        if table[i] == True:
            for word in arr:
                if word in target:
                    preffixs = target.index(word)
                    if preffixs == 0:
                        suffixs = target[len(word):]
                        suffs = len(suffixs)
                        if i + suffs < len(table):
                            table[i + suffs] = True
    return table[len(target)]

print(canConst(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel"))
print(canConst(["sam", "jame", "joe"], "purple"))
print(canConst(["pru", "pur", "le", "p", "ple", "ur", "urp"],"purple"))


def canconst_alternative(arr, target):
    table = [None for x in range(len(target)+ 1)]
    table[0] = []
    
    for i in range(len(target)):
        if table[i] is not None:
            for word in arr:
                if word in target:
                    if target[i : i + len(word)] == word:
                        table[i + len(word)] = [*table[i], word]
    
    return table[len(target)]


print(canconst_alternative(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel"))
print(canconst_alternative(["sam", "jame", "joe"], "purple"))
print(canconst_alternative(["pru", "pur", "le", "p", "ple", "ur", "urp"],"purple"))

def countConst(arr, target):
    
    table = [0 for x in range(len(target) + 1)]
    table[0] = 1
    
    for i in range(len(target)):
        if table[i] == 1 :
            for word in arr:
                if word in target:
                    if target[i: i+len(word)] == word:
                        if i + len(word) < len(table):
                            table[i + len(word)] += table[i]
    return table(len(target))


print(countConst(["sa", "sam", "u", "ue", "le", "uel", "l"], "samuel"))
print(countConst(["sam", "jame", "joe"], "purple"))
print(countConst(["pru", "pur", "le", "p", "ple", "ur", "urp"],"purple"))

                    