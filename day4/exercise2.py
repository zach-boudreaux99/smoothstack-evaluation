from functools import reduce

# 1
data = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Berry", 3, 32.95],
    [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]
]

result = map(lambda x : x if x[1] >= 100 else (x[0], x[1] + 10), map(lambda x : (x[0], x[2] * x[3]), data))
print(list(result)) 

# 2
data2 = [
    [1, (34587, 4, 40.95), (98762, 5, 56.80), (77226, 3, 32.95)],
    [2, (98762, 5, 56.80), (77226, 3, 32.95), (88112, 3, 24.99)],
    [3, (34587, 4, 40.95), (77226, 3, 32.95), (88112, 3, 24.99)]
]

step1 = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), data2)) #Will reduce down to array order cost [1, 163.8, 284.0, 98.85]
step2 = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], step1)) #Will add order cost [1, 546.65]
step3 = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), step2)) #Will add 10 if total < 100
print(step2)