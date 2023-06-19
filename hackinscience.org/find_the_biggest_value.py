"""
Comparisons
Created by Julien Palard

Find the biggest value in a given list.

Try it by using only a temporary variable, a for loop, and an if to compare the
values.

I prefilled the list in the answer box, but in case you need it again, here it
is:
"""

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

tmp_var = None

for value in the_list:
    if tmp_var is None or value > tmp_var:
        tmp_var = value

print(tmp_var)
