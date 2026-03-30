"""
Python Generators: Basic to Expert Level Examples
=================================================
"""

# ============================================================================
# BASIC LEVEL GENERATORS
# ============================================================================

def basic_number_generator():
    """Basic generator that yields numbers 1-5"""
    for i in range(1, 6):
        yield i

def countdown_generator(n):
    """Generator that counts down from n to 1"""
    while n > 0:
        yield n
        n -= 1

def fibonacci_basic():
    """Basic Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# ============================================================================
# INTERMEDIATE LEVEL GENERATORS
# ============================================================================

def file_reader(filename):
    """Generator that reads file line by line"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def even_numbers(limit):
    """Generator for even numbers up to limit"""
    num = 0
    while num <= limit:
        if num % 2 == 0:
            yield num
        num += 1

def prime_generator():
    """Generator for prime numbers"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def batch_processor(data, batch_size):
    """Generator that processes data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# ============================================================================
# ADVANCED LEVEL GENERATORS
# ============================================================================

def tree_traversal(node):
    """Generator for depth-first tree traversal"""
    if node is not None:
        yield node.value
        if hasattr(node, 'children'):
            for child in node.children:
                yield from tree_traversal(child)

def sliding_window(iterable, window_size):
    """Generator that creates sliding windows of data"""
    from collections import deque
    window = deque(maxlen=window_size)
    
    for item in iterable:
        window.append(item)
        if len(window) == window_size:
            yield list(window)

def coroutine_generator():
    """Generator that can receive values (coroutine)"""
    result = None
    while True:
        value = yield result
        if value is not None:
            result = value * 2

def pipeline_generator(*generators):
    """Generator that chains multiple generators"""
    for gen in generators:
        yield from gen

# ============================================================================
# EXPERT LEVEL GENERATORS
# ============================================================================

class DataStream:
    """Expert-level generator class for data streaming"""
    def __init__(self, data_source):
        self.data_source = data_source
        self.filters = []
        self.transformers = []
    
    def filter(self, predicate):
        self.filters.append(predicate)
        return self
    
    def transform(self, func):
        self.transformers.append(func)
        return self
    
    def __iter__(self):
        for item in self.data_source:
            # Apply filters
            if all(f(item) for f in self.filters):
                # Apply transformations
                for transformer in self.transformers:
                    item = transformer(item)
                yield item

def async_generator_example():
    """Async generator example"""
    import asyncio
    
    async def async_data_generator():
        for i in range(5):
            await asyncio.sleep(0.1)  # Simulate async operation
            yield f"Data {i}"
    
    return async_data_generator()

def memory_efficient_csv_processor(filename):
    """Memory-efficient CSV processor using generators"""
    import csv
    
    def process_row(row):
        # Process each row (example: convert numeric strings to int)
        processed = {}
        for key, value in row.items():
            try:
                processed[key] = int(value)
            except ValueError:
                try:
                    processed[key] = float(value)
                except ValueError:
                    processed[key] = value
        return processed
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield process_row(row)

def recursive_directory_walker(path):
    """Generator that recursively walks directory structure"""
    import os
    
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

def stateful_generator():
    """Generator that maintains complex state"""
    state = {'count': 0, 'sum': 0, 'history': []}
    
    while True:
        value = yield state.copy()
        if value is not None:
            state['count'] += 1
            state['sum'] += value
            state['history'].append(value)
            if len(state['history']) > 10:
                state['history'].pop(0)

# ============================================================================
# GENERATOR EXPRESSIONS AND COMPREHENSIONS
# ============================================================================

def generator_expressions_examples():
    """Examples of generator expressions"""
    
    # Basic generator expression
    squares = (x**2 for x in range(10))
    
    # Generator with condition
    even_squares = (x**2 for x in range(10) if x % 2 == 0)
    
    # Nested generator expression
    matrix_flatten = (item for row in [[1,2], [3,4], [5,6]] for item in row)
    
    return squares, even_squares, matrix_flatten

# ============================================================================
# PRACTICAL EXAMPLES AND USE CASES
# ============================================================================

def log_parser(log_file):
    """Parse log files efficiently"""
    import re
    
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)')
    
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                yield {
                    'date': match.group(1),
                    'time': match.group(2),
                    'level': match.group(3),
                    'message': match.group(4)
                }

def infinite_sequence_generator(start=0, step=1):
    """Generate infinite sequence with custom start and step"""
    current = start
    while True:
        yield current
        current += step

def weighted_random_generator(weights):
    """Generator for weighted random selection"""
    import random
    
    total = sum(weights.values())
    while True:
        r = random.uniform(0, total)
        cumulative = 0
        for item, weight in weights.items():
            cumulative += weight
            if r <= cumulative:
                yield item
                break

# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_basic():
    """Demonstrate basic generators"""
    print("=== BASIC GENERATORS ===")
    
    print("Basic number generator:")
    for num in basic_number_generator():
        print(num, end=" ")
    print()
    
    print("Countdown from 5:")
    for num in countdown_generator(5):
        print(num, end=" ")
    print()
    
    print("First 10 Fibonacci numbers:")
    fib = fibonacci_basic()
    for _ in range(10):
        print(next(fib), end=" ")
    print()

def demonstrate_intermediate():
    """Demonstrate intermediate generators"""
    print("\n=== INTERMEDIATE GENERATORS ===")
    
    print("Even numbers up to 10:")
    for num in even_numbers(10):
        print(num, end=" ")
    print()
    
    print("First 5 prime numbers:")
    primes = prime_generator()
    for _ in range(5):
        print(next(primes), end=" ")
    print()
    
    print("Batch processing [1,2,3,4,5,6,7,8] with batch size 3:")
    data = [1,2,3,4,5,6,7,8]
    for batch in batch_processor(data, 3):
        print(batch)

def demonstrate_advanced():
    """Demonstrate advanced generators"""
    print("\n=== ADVANCED GENERATORS ===")
    
    print("Sliding window example:")
    data = [1,2,3,4,5,6,7]
    for window in sliding_window(data, 3):
        print(window)
    
    print("Coroutine generator:")
    coro = coroutine_generator()
    next(coro)  # Prime the coroutine
    print(coro.send(5))  # Should print 10
    print(coro.send(3))  # Should print 6

def demonstrate_expert():
    """Demonstrate expert-level generators"""
    print("\n=== EXPERT GENERATORS ===")
    
    print("DataStream example:")
    data = range(1, 11)
    stream = DataStream(data)
    result = (stream
              .filter(lambda x: x % 2 == 0)  # Even numbers only
              .transform(lambda x: x ** 2)    # Square them
              )
    
    print("Even squares from 1-10:")
    for item in result:
        print(item, end=" ")
    print()
    
    print("Stateful generator:")
    stateful = stateful_generator()
    next(stateful)  # Prime the generator
    print("After sending 10:", stateful.send(10))
    print("After sending 20:", stateful.send(20))
    print("After sending 30:", stateful.send(30))

if __name__ == "__main__":
    demonstrate_basic()
    demonstrate_intermediate()
    demonstrate_advanced()
    demonstrate_expert()
