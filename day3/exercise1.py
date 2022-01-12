import random

# 1
def find_numbers():
    result = ""
    for x in range(1500, 2701):
        if x % 7 == 0 and x % 5 == 0:
            result += f"{x}, "
    
    print(result)

find_numbers()

# 2
def temp_convert():
    type = input("Input f or c: ")
    temp = input("Input current temp: ")
    if type == "f" or type == "F":
        new_temp = (int(temp) - 32) * (5/9)
        print(f"{new_temp}C")
    elif type == "c" or type == "C":
        new_temp = (int(temp) * 1.8) + 32
        print(f"{new_temp}F")
    else:
        print("Incorrect input")

temp_convert()

# 3
def number_guess():
    num = random.randrange(1, 10, 1)
    print(num)
    guess = input("Guess a number between 0-9: ")
    
    while int(guess) != num:
        guess = input("Incorrect, guess another number: ")
    
    print("Correct")
    
number_guess()

# 4
def print_pyramid():
    i = 1
    while i < 6:
        print(i * "*")
        i += 1
    while i > 0:
        print(i * "*")
        i -= 1

print_pyramid()

# 5
def reverse_input():
    word = input("Input a word to reverse: ")
    print(word[::-1])

reverse_input()

# 6
def count_evens_odds(array):
    evens = 0
    odds = 0
    
    for x in array:
        if x % 2 == 0:
            evens += 1
        elif x % 2 == 1:
            odds += 1
            
    print(f"Count of evens: {evens}")
    print(f"Count of odds: {odds}")

count_evens_odds([1,2,3,4,5,6,7,8,9])

# 7
def display_type(array):
    for x in array:
        print(type(x))

display_type([[1,2,3], True, "hello", (1,2), {"class": "V", "section": "A"}])

# 8
def print_nums():
    num = 0
    while num <= 6:
        if num == 3 or num == 6:
            num += 1
            continue
        else:
            print(num)
            num += 1
            
print_nums()