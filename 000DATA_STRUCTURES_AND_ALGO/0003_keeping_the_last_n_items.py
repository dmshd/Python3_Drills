from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
            previous_lines.append(line)


# Example use on a file
if __name__ == "__main__":
    with open("somefile.txt") as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)

# The deque(maxlen=N) creates a fixed-sized queue. When new items are added and
# the queue is full, the oldest item is automatically removed.

# deque(maxlen=history) : deque est un type spécial de séquence de données
# fournies par la bibliothèque collections de Python. Il s'agit d'une file
# d'attente à deux bouts (double-ended queue), ce qui signifie que vous pouvez
# ajouter ou retirer des éléments de chaque côté. L'argument maxlen définit la
# longueur maximale de la file d'attente. Si vous essayez d'ajouter un élément
# lorsque la file d'attente est pleine, le plus ancien élément (c'est-à-dire
# l'élément à l'autre extrémité de l'endroit où vous ajoutez le nouvel élément)
# est automatiquement supprimé pour faire de la place.


# yield line, previous_lines : yield est utilisé ici pour faire de search une
# fonction de générateur. Chaque fois que la fonction est appelée, elle renvoie
# la prochaine valeur du générateur (dans ce cas, line et previous_lines), puis
# suspend son exécution jusqu'à ce qu'elle soit appelée à nouveau.


# Using deque(maxlen=N) creates a fixed-sized queue. When new items are added
# and the queue is full, the oldest item is automatically removed.

q = deque(maxlen=3)
q.append(1)  # deque([1], maxlen=3)
print(q)
q.append(2)  # deque([1, 2], maxlen=3)
print(q)
q.append(3)  # deque([1, 2, 3], maxlen=3)
print(q)
q.append(4)  # deque([2, 3, 4], maxlen=3)
print(q)
q.append(5)  # deque([3, 4, 5], maxlen=3)

# Although you could manually perform such operations on a list (e.g.,
# appending, deleting, etc.), the queue solution is far more elegant and runs
# a lot faster.
