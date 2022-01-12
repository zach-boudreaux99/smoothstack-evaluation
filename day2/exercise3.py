# Three is a crowd
print("THREE IS A CROWD")
def is_overcrowded(lst):
    if len(lst) > 3:
        print("Overcrowded")

people = ["Zach", "Mariah", "Emilie", "Byron"]
is_overcrowded(people)
people = people[:2]
is_overcrowded(people)

# Three is a crowd pt 2
print("THREE IS A CROWD PT 2")
def is_overcrowded2(lst):
    if len(lst) > 3:
        print("Overcrowded")
    else:
        print("Not overcrowded")

people = ["Zach", "Mariah", "Emilie", "Byron"]
is_overcrowded2(people)
people = people[:2]
is_overcrowded2(people)

# Six is mob
print("SIX IS A MOB")
def is_overcrowded3(lst):
    if len(lst) > 5:
        print("There is a mob")
    elif len(lst) >= 3 and len(lst) <= 5:
        print("This room is crowded")
    elif len(lst) < 3 and len(lst) > 0:
        print("This room is not crowded")
    elif len(lst) == 0:
        print("This room is empty")
        
people = ["Zach", "Mariah", "Emilie", "Byron", "Laura", "Molly"]
is_overcrowded3(people)
people = people[0:5]
is_overcrowded3(people)
people = people[0:2]
is_overcrowded3(people)
people = people[0:0]
is_overcrowded3(people)