# 1
example_list = [1, "hello", 1.5]
print(example_list)

# 2
nested_list = [1, 1, [1, 2]]
print(nested_list[2][1])

# 3
lst1 = ['a', 'b', 'c']
print(lst1[1:])

# 4
week = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7
}
print(week)

# 5
d = {"k1": [1, 2, 3]}
print(d["k1"][1])

# 6
lst2 = [1, [1, 2]]
tple1 = (1, [1, 2])

# 7
def chars(word):
    for char in word:
        print(char)

chars("Mississippi")

# 8

# 9
print(set([1,1,2,3]))

# Question 1
def question1():
    result = ""
    for x in range(2000, 3201):
        if x % 7 == 0 and x % 5 != 0:
            result += f"{x}, "
    
    print(result)

question1()

# Question 2
def factorial():
    x = input("Input your value: ")
    result = 1
    for x in range(1, int(x) + 1):
        result *= x
    
    print(result)
    
factorial()

# Question 3
def dicts():
    x = input("Input your value: ")
    result = {}
    for x in range(1, int(x) + 1):
        result[x] = x * x
    
    print(result)
    
dicts()

# Question 4
def lists_and_tuples(array):
    list_result = list(array)
    tuple_result = tuple(array)
        
    print(list_result)
    print(tuple_result)
    
lists_and_tuples([34, 67, 55, 33, 12, 98])

# Question 5
class Input_Output():
    def __init__(self):
        self.s = ""
        
    def getString(self):
        self.s = input("Input your string: ")
        
    def printString(self):
        print(self.s.upper())
    
strObj = Input_Output()
strObj.getString()
strObj.printString()