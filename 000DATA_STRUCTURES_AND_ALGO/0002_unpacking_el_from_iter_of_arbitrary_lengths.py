"""
You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many values to unpack" exception.

Python "star expressions" can be used to address this problem.

"""

record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
name, email, *phone_numbers = record
print(name)  # Dave
print(email)  # dave@example
print(phone_numbers)  # ['773-555-1212', '847-555-1212']

# The starred variable can also be the first one in the list.
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)  # [10, 8, 7, 1, 9, 5, 10]
print(current)  # 3

# The star syntax can be especially useful when iterating over a sequence of tuples of varying length.


# star syntax is especially useful when iterating over a sequence of tuples of varying length. For example, perhaps a sequence of tagged tuples:

records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4),
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)

# Star unpacking can also be useful when combined with certain kinds of string processing operations, such as splitting.

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
splitted_line = line.split(
    ":"
)  # ['nobody', '*', '-2', '-2', 'Unprivileged User', '/var/empty', '/usr/bin/false']
uname, *fields, homedir, sh = splitted_line
print(uname)  # nobody
print(homedir)  # /var/empty
print(sh)  # /usr/bin/false


# Sometimes you might want to unpack values and throw them away. You can't just specify a bare * when unpacking, but you could use a common throwaway variable name, such as _ or ign (ignored).

record = ("ACME", 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)  # ACME
print(year)  # 2012

# There is a certain similarity between star unpacking and list-processing features of various functional languages. For example, if you have a list, you can easily split it into head and tail components like this:

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)  # 1
print(tail)  # [10, 7, 4, 5, 9]

# One could imagine writing functions that perform such splitting in order to carry out some kind of clever recursive algorithm. For example:

items = [1, 10, 7, 4, 5, 9]


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))  # 36
