"""
Unpacking N-element into a collection of N variables.
Any sequence or iterable can be unpacked into variables using a simple
assignment operation.
"""

p = (4, 5)
x, y = p
print(x)  # 4
print(y)  # 5

data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)  # ACME
print(shares)  # 50
print(price)  # 91.1
print(date)  # (2012, 12, 21)

# p = (4, 5)
# x, y, z = p
# ValueError: not enough values to unpack (expected 3, got 2)
# print(x)

s = "Hello"
a, b, c, d, e = s
print(a)  # H
print(b)  # e
print(c)  # l
print(d)  # l
print(e)  # o

# Unpacking works with any object that happens to be iterable, not just tuples
# or lists.

# When unpacking, you may sometimes want to discard certain values. Python has
# no special syntax for this, but you can often just pick a throwaway variable
# name for it.

data = ["ACME", 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)  # 50
print(price)  # 91.1
