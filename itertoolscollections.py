#qqq
#Basic Level
#1. Counter - Frequency counting
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)              # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]


#2. defaultdict - Grouping items
from collections import defaultdict

students = [("Math", "Alice"), ("Science", "Bob"), ("Math", "Charlie"), ("Science", "Alice")]
groups = defaultdict(list)
for subject, name in students:
    groups[subject].append(name)
print(dict(groups))  # {'Math': ['Alice', 'Charlie'], 'Science': ['Bob', 'Alice']}


#3. namedtuple - Readable data structures
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)        # 3 4
print(p._asdict())      # {'x': 3, 'y': 4}


#4. itertools.count / cycle / repeat
import itertools

# Infinite counter
for i in itertools.count(10, 2):  # 10, 12, 14...
    if i > 16: break
    print(i, end=" ")

# Cycle through items
colors = itertools.cycle(["red", "green", "blue"])
print([next(colors) for _ in range(5)])  # ['red', 'green', 'blue', 'red', 'green']

# Repeat
print(list(itertools.repeat("hello", 3)))  # ['hello', 'hello', 'hello']



#Intermediate Level
#5. deque - Efficient double-ended queue
from collections import deque

dq = deque(maxlen=3)
for i in range(5):
    dq.append(i)
print(dq)  # deque([2, 3, 4], maxlen=3) — auto-evicts oldest

# Rotate
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)
print(dq)  # deque([4, 5, 1, 2, 3])


#6. OrderedDict - Move to end / LRU-style
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
od.move_to_end("a")       # Move 'a' to end
print(list(od.keys()))     # ['b', 'c', 'a']
od.move_to_end("c", last=False)  # Move 'c' to front
print(list(od.keys()))     # ['c', 'b', 'a']



#7. itertools.chain / chain.from_iterable
import itertools

a = [1, 2, 3]
b = [4, 5]
c = [6, 7, 8, 9]
print(list(itertools.chain(a, b, c)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

nested = [[1, 2], [3, 4], [5]]
print(list(itertools.chain.from_iterable(nested)))  # [1, 2, 3, 4, 5]


#8. itertools.groupby

import itertools

data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot"), ("veg", "pea")]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, [item[1] for item in group])
# fruit ['apple', 'banana']
# veg ['carrot', 'pea']


#9. Combinations and Permutations

import itertools

print(list(itertools.permutations([1, 2, 3], 2)))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

print(list(itertools.combinations([1, 2, 3, 4], 2)))
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

print(list(itertools.combinations_with_replacement("AB", 2)))
# [('A','A'), ('A','B'), ('B','B')]


#10.ChainMap - Layered dictionaries

from collections import ChainMap

defaults = {"color": "red", "size": "medium"}
user_prefs = {"color": "blue"}
config = ChainMap(user_prefs, defaults)
print(config["color"])  # blue (user_prefs wins)
print(config["size"])   # medium (falls back to defaults)





#Advanced Level
#11. Sliding window with deque
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()  # stores indices
    result = []
    for i, n in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]


#12. itertools.accumulate - Running computations
import itertools
import operator

nums = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(nums)))                        # Running sum: [1, 3, 6, 10, 15]
print(list(itertools.accumulate(nums, operator.mul)))          # Running product: [1, 2, 6, 24, 120]
print(list(itertools.accumulate(nums, max)))                   # Running max: [1, 2, 3, 4, 5]


#13. itertools.product - Cartesian product / Grid generation
import itertools

# Replace nested loops
for x, y, z in itertools.product(range(2), range(3), range(2)):
    print(f"({x},{y},{z})", end=" ")
# (0,0,0) (0,0,1) (0,1,0) ... (1,2,1)

# Password brute-force pattern
chars = "ab"
for combo in itertools.product(chars, repeat=3):
    print("".join(combo), end=" ")
# aaa aab aba abb baa bab bba bbb


#14. itertools.starmap
import itertools

pairs = [(2, 3), (4, 5), (6, 7)]
print(list(itertools.starmap(pow, pairs)))  # [8, 1024, 279936]


#Expert Level
#15. LRU Cache using OrderedDict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))   # 1
cache.put("c", 3)       # evicts 'b'
print(cache.get("b"))   # -1


#16. Trie using defaultdict (recursive)

from collections import defaultdict

def make_trie():
    return defaultdict(make_trie)

trie = make_trie()
# Insert words
for word in ["apple", "app", "apply", "bat"]:
    node = trie
    for ch in word:
        node = node[ch]
    node["#"] = True  # end marker

# Search
def search(trie, word):
    node = trie
    for ch in word:
        if ch not in node:
            return False
        node = node[ch]
    return "#" in node

print(search(trie, "app"))    # True
print(search(trie, "ap"))     # False



#17. Powerset using itertools.combinations
import itertools

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )

print(list(powerset([1, 2, 3])))
# [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]


#18. Flatten deeply nested structures with itertools
import itertools
from collections.abc import Iterable

def deep_flatten(iterable):
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item

nested = [1, [2, [3, [4, 5]], 6], [7, 8]]
print(list(deep_flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8]


#19. Weighted round-robin scheduler
import itertools
from collections import Counter

def weighted_round_robin(weights):
    """weights: dict of {task: weight}"""
    elements = Counter(weights).elements()
    pool = list(elements)
    return itertools.cycle(pool)

scheduler = weighted_round_robin({"A": 3, "B": 1, "C": 2})
print([next(scheduler) for _ in range(12)])
# ['A', 'A', 'A', 'B', 'C', 'C', 'A', 'A', 'A', 'B', 'C', 'C']


#20. N-gram generator with itertools.islice and deque

import itertools
from collections import deque

def ngrams(iterable, n):
    it = iter(iterable)
    window = deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)

text = "the quick brown fox jumps".split()
print(list(ngrams(text, 3)))
# [('the','quick','brown'), ('quick','brown','fox'), ('brown','fox','jumps')]





"""Quick reference summary:

Module	                Key Tools	        Use Case
collections.Counter 	Counting, top-N	    Frequency analysis
collections.defaultdict	Auto-init dicts	    Grouping, graphs
collections.deque	    O(1) ends ops	    Queues, sliding windows
collections.OrderedDict	Ordered + move ops	LRU caches
collections.ChainMap	Layered lookups	    Config merging
collections.namedtuple	Lightweight classes	Readable records
itertools.chain     	Flatten one level	Merging iterables
itertools.groupby	    Group sorted data	Categorization
itertools.product	    Cartesian product	Replace nested loops
itertools.combinations	Choose r from n	    Subset generation
itertools.accumulate	Running reductions	Prefix sums, running max
itertools.cycle/count	Infinite iterators	Schedulers, generators"""
