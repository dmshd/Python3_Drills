"""
Implementing a queue that sorts items by a given
priorityand always returns the item with the highest priority on each pop
operation.

The priority queue is a data structure that allows elements to be added with a
priority level, and when elements are removed, the one with the highest
priority is removed first.

Here are a few real-world applications of such a priority queue:

    Task Scheduling in Operating Systems: One of the classic uses of a priority
    queue is in operating systems for process scheduling. Processes can be
    assigned a priority, for instance based on their urgency or the resources
    they require, and the process with the highest priority gets executed
    first.

    Emergency Services: In emergency medical services, patients are often
    prioritized based on the severity of their condition. This is sometimes
    called triage. A patient with a life-threatening condition (high priority)
    would be treated before someone with a minor injury (low priority).

    Airline Check-in: In airports, airline passengers may have different levels
    of priority. For instance, first-class or business-class passengers might
    have priority over economy-class passengers, and would therefore be checked
    in first.

    Traffic Management: In traffic management, certain vehicles like
    ambulances, fire trucks, or police cars often have priority over other
    vehicles.

    Networking and Telecommunications: Packets in a network can be managed
    based on priority queues. Some packets are more important than others and
    should be sent first.

    E-commerce systems: In E-commerce, orders can be processed based on
    priority. For example, orders with expedited shipping could have a higher
    priority than those with standard shipping.

Here's how the PriorityQueue code works:

    The push method inserts an item into the queue with a given priority. It's
    using a negative value for priority because heapq creates a min-heap
    instead of a max-heap (items with smaller values come out first). By
    negating the priority, we can ensure that items with higher priority come
    out first.

    The _index attribute is used to properly order items with the same priority
    level and ensure the queue behaves correctly in such scenarios. This is
    necessary because the Python heapq doesn't handle comparison of two tuples
    where the first elements are equal, and the second elements are not
    comparable (like in our case - the item objects are not comparable).

    The pop method removes and returns the item with highest priority from the
    queue. If multiple items have the same priority, they are returned in the
    order they were inserted.

    Item is a simple class to encapsulate our items. We only have a name for
    each item, and a __repr__ method that defines how the item is represented
    as a string (useful for debugging and logging).

    The last part is a test of the PriorityQueue: We're adding four items with
    different priorities, and then removing them one by one. Given the
    priorities, the order of removal should be: 'bar', 'spam', 'foo' or 'grok',
    and finally 'foo' or 'grok'. Note that 'foo' and 'grok' have the same
    priority, so they could come out in any order.
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


# Example use

if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("spam"), 4)
    q.push(Item("grok"), 1)
    print(q._queue)
    print(q.pop())
    print(q.pop())
    print(q.pop())

"""
The core of this recipe concerns
"""
