# 1
def func():
    print("Hello World")

func()

# 2
def func2(name):
    print(f"Hello my name is {name}")
    
func2("Zach")

# 3
def func3(x, y, z):
    if z:
        print(x)
    else:
        print(y)

func3("hello", "goodbye", True)
func3("hello", "goodbye", False)

# 4
def func4(x, y):
    print(x * y)

func4(2, 5)

# 5
def is_even(num):
    if num % 2 == 0:
        print(True)
    elif num % 2 == 1:
        print(False)

is_even(1)
is_even(2)

# 6
def greater_than(x, y):
    if x > y:
        print(True)
    else:
        print(False)
        
greater_than(5, 1)
greater_than(5, 5)
greater_than(5, 10)

# 7
def sum_of_args(*args):
    print(sum(args))

sum_of_args(1,2,3,4,5,6,7,8,9)

# 8
def list_of_evens(*args):
    lst = []
    for x in args:
        if x % 2 == 0:
            lst.append(x)
    
    print(lst)

list_of_evens(1,2,3,4,5,6,7,8,9)

# 9
def alternate_case(s):
    result = ""
    i = False
    for char in s:
        if i:
            result += char.upper()
        else:
            result += char.lower()
        i = not i
    
    print(result)

alternate_case("Hello World")

# 10
def greater_or_less(x, y):
    if x % 2 == 0 and y % 2 == 0:
        print(min(x, y))
    else:
        print(max(x, y))

greater_or_less(4, 8)
greater_or_less(5, 8)

# 11
def same_start(s1, s2):
    if s1[0].lower() == s2[0].lower():
        print(True)
    else: 
        print(False)    
        
same_start("Hello", "halloween")

# 12
def square(x):
    print(x ** 2)

square(5)

# 13
def first_and_fourth(s):
    lst = list(s)
    lst[0] = lst[0].upper()
    lst[3] = lst[3].upper()
    print("".join(lst))

first_and_fourth("hello")