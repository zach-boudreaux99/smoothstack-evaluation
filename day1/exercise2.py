import math

# 1
print(50+50)
print(100-10)

# 3
print("Hello World")
print("Hello World : 10")

# 4
def mortage(p, r, l):
    r_monthly = (r / 100) / 12
    months = l
    numerator = r_monthly * ((1 + r_monthly)**months)
    denominator = ((1 + r_monthly)**months) - 1
    payment = p * (numerator / denominator)
    print(math.ceil(payment))

mortage(800000, 6, 103)