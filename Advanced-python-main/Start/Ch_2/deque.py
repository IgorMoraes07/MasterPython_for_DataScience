# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Item Count: {len(d)}")

# TODO: deques can be iterated over
for elem in d:
    print(elem.upper())

# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

# TODO: use an index to get a particular item
print(d)
d.rotate(1)
print(d)
