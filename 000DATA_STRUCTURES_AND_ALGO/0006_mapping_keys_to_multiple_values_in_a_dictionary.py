"""
Making a dictionary that maps keys to more than one value (a so-called multidict) is a frequent need.

    The first is a dictionary where each key maps to a list of values. When you insert a new value for a key, it's appended to the list of values for that key. This allows you to maintain the order of insertion and to store multiple identical values for the same key.

    The second is a dictionary where each key maps to a set of values. When you insert a new value for a key, it's added to the set of values for that key. This doesn't maintain the order of insertion, but it ensures that all values for a key are unique.

Here are some real-world examples where a multidict can be useful:

    Grouping or Categorizing Data: If you have a list of items and you want to group them by a certain characteristic (like grouping a list of words by their first letter), a multidict is a great way to do it. The characteristic will be the key, and the values will be the items that have this characteristic. In the above code, 'a' and 'b' could be first letters of words, and the lists or sets could contain the words that start with these letters.

    Graph Representation: In graph theory, a multidict can be used to represent a graph where each key is a node and the corresponding values are the nodes it is connected to.

    Indexing or Inverted Index: In information retrieval or database design, a multidict is often used for creating an index where each key is a term, and the values are the documents or records containing this term.

    Managing Relationships in a Social Network: If you're building a social network, you might have a multidict where each key is a person, and the values are the people they're friends with.
"""

from collections import defaultdict

d = defaultdict(list)

d["a"].append(1)
d["a"].append(2)
d["b"].append(4)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

d = defaultdict(set)

d["a"].add(1)
d["a"].add(2)
d["b"].add(4)
print(d)  # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})
