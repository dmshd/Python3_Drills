"""
You want to make a list of the largest or smallest N items in a collection.

The heapq module has two functions—nlargest() and nsmallest()—that do exactly
what you want.

Being able to find the largest or smallest N items from a data set is a very
useful capability in various real-world situations. Here are some examples:

    Finance and Investing: For instance, a portfolio manager may want to
    identify the top 10 performing stocks in a portfolio, or an analyst might
    want to identify the 5 companies with the lowest debt levels in a specific
    industry.

    Data Analysis and Data Science: If you're analyzing a large dataset,
    you might want to find the top or bottom N items. For example, in a survey
    of customer satisfaction, you might want to find the 10 most dissatisfied
    customers to understand their complaints and improve the service.

    E-Commerce: An e-commerce website might want to display the top 5
    best-selling products in each category to customers, or identify the 10
    least sold items to apply discounts and boost their sales.

    Sports Analytics: If you are a sports analyst, you might want to identify
    the top 5 players with the highest scores in a season, or the 3 teams with
    the fewest wins in a league.

    Education: A teacher might want to identify the 5 students with the highest
    marks in a test to give them recognition, or the 5 students with the lowest
    marks to provide them with additional help.

    Healthcare: In healthcare analytics, you might want to identify the top 10
    regions with the highest occurrence of a particular disease to focus
    resources for treatment and prevention.

In all these cases, you would be finding the largest or smallest N items from
a collection, which is the same concept you're reading about in your Python
book. The Python functions heapq.nlargest() and heapq.nsmallest() are perfect
for these kinds of tasks, as they provide an efficient way to find the N
largest or smallest items in a collection.

"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

# Both functions also accept a key parameter that allows them to be used with
# more complicated data structures.

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])
print(cheap)
# Prints [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB',
# 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35,
# 'price': 31.75}]
print(expensive)
# Prints [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME',
# 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100,
# 'price': 91.1}]


# If you are looking for the N smallest or largest items and N is small
# compared to the overall size of the collection, these functions provide
# superior performance. Underneath the covers, they work by first converting
# the data into a list where items are ordered as a heap. For example:

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)  # Prints [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
