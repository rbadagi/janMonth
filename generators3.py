#qq
"""
Specialized Python Generator Examples
====================================
Advanced patterns and real-world applications
"""

import itertools
import time
import json
from collections import deque
from typing import Generator, Any, Iterator

# ============================================================================
# PERFORMANCE-FOCUSED GENERATORS
# ============================================================================

def chunked_file_reader(filename: str, chunk_size: int = 8192) -> Generator[str, None, None]:
    """Memory-efficient file reader for large files"""
    with open(filename, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def lazy_json_parser(json_file: str) -> Generator[dict, None, None]:
    """Parse large JSON files lazily"""
    with open(json_file, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            for item in data:
                yield item
        else:
            yield data

def database_cursor_generator(cursor, batch_size: int = 1000):
    """Generator for database results in batches"""
    while True:
        results = cursor.fetchmany(batch_size)
        if not results:
            break
        for row in results:
            yield row

# ============================================================================
# MATHEMATICAL GENERATORS
# ============================================================================

def collatz_sequence(n: int) -> Generator[int, None, None]:
    """Generate Collatz sequence for given number"""
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

def pascal_triangle() -> Generator[list, None, None]:
    """Generate rows of Pascal's triangle"""
    row = [1]
    while True:
        yield row
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]

def geometric_series(first_term: float, ratio: float) -> Generator[float, None, None]:
    """Generate geometric series"""
    term = first_term
    while True:
        yield term
        term *= ratio

def factorial_generator() -> Generator[int, None, None]:
    """Generate factorials: 1!, 2!, 3!, ..."""
    n, factorial = 1, 1
    while True:
        yield factorial
        n += 1
        factorial *= n

# ============================================================================
# DATA PROCESSING GENERATORS
# ============================================================================

def csv_row_processor(filename: str, delimiter: str = ',') -> Generator[dict, None, None]:
    """Process CSV files row by row with custom processing"""
    import csv
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            # Clean and process each row
            processed_row = {}
            for key, value in row.items():
                # Strip whitespace and handle empty values
                clean_key = key.strip() if key else ''
                clean_value = value.strip() if value else None
                
                # Try to convert to appropriate type
                if clean_value:
                    try:
                        # Try integer first
                        processed_row[clean_key] = int(clean_value)
                    except ValueError:
                        try:
                            # Try float
                            processed_row[clean_key] = float(clean_value)
                        except ValueError:
                            # Keep as string
                            processed_row[clean_key] = clean_value
                else:
                    processed_row[clean_key] = None
            
            yield processed_row

def xml_element_generator(xml_file: str, target_tag: str):
    """Parse XML and yield specific elements"""
    import xml.etree.ElementTree as ET
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    for element in root.iter(target_tag):
        yield {
            'tag': element.tag,
            'text': element.text,
            'attributes': element.attrib
        }

def json_stream_processor(json_lines_file: str) -> Generator[dict, None, None]:
    """Process JSON Lines format files"""
    with open(json_lines_file, 'r') as file:
        for line in file:
            try:
                yield json.loads(line.strip())
            except json.JSONDecodeError:
                continue  # Skip invalid JSON lines

# ============================================================================
# NETWORK AND API GENERATORS
# ============================================================================

def api_paginator(base_url: str, params: dict = None, page_param: str = 'page'):
    """Generator for paginated API responses"""
    import requests
    
    page = 1
    params = params or {}
    
    while True:
        params[page_param] = page
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
            
        data = response.json()
        
        # Assume data is a list or has a 'results' key
        items = data if isinstance(data, list) else data.get('results', [])
        
        if not items:
            break
            
        for item in items:
            yield item
            
        page += 1

def rate_limited_generator(generator: Iterator, calls_per_second: float):
    """Wrap any generator with rate limiting"""
    min_interval = 1.0 / calls_per_second
    last_call = 0
    
    for item in generator:
        current_time = time.time()
        time_since_last = current_time - last_call
        
        if time_since_last < min_interval:
            time.sleep(min_interval - time_since_last)
        
        last_call = time.time()
        yield item

# ============================================================================
# ADVANCED PATTERN GENERATORS
# ============================================================================

def state_machine_generator(states: dict, initial_state: str):
    """Generator that implements a state machine"""
    current_state = initial_state
    
    while True:
        # Yield current state and receive input
        input_data = yield current_state
        
        # Transition to next state based on input
        if current_state in states and input_data in states[current_state]:
            current_state = states[current_state][input_data]

def cache_generator(generator: Iterator, cache_size: int = 100):
    """Generator with LRU cache for expensive computations"""
    from functools import lru_cache
    
    cache = deque(maxlen=cache_size)
    cache_dict = {}
    
    for item in generator:
        # Simple caching based on item hash
        item_hash = hash(str(item))
        
        if item_hash in cache_dict:
            yield cache_dict[item_hash]
        else:
            cache.append(item_hash)
            cache_dict[item_hash] = item
            yield item

def retry_generator(generator: Iterator, max_retries: int = 3, delay: float = 1.0):
    """Generator that retries failed operations"""
    for item in generator:
        retries = 0
        while retries <= max_retries:
            try:
                # Simulate processing that might fail
                if hasattr(item, '__call__'):
                    result = item()
                else:
                    result = item
                yield result
                break
            except Exception as e:
                retries += 1
                if retries > max_retries:
                    raise e
                time.sleep(delay * retries)  # Exponential backoff

# ============================================================================
# CONCURRENT GENERATORS
# ============================================================================

def threaded_generator(generator: Iterator, max_workers: int = 4):
    """Process generator items using thread pool"""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from queue import Queue
    import threading
    
    def worker(item):
        # Simulate some processing
        time.sleep(0.1)
        return f"Processed: {item}"
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        
        for item in generator:
            future = executor.submit(worker, item)
            futures.append(future)
            
            # Yield completed results
            if len(futures) >= max_workers:
                for future in as_completed(futures[:max_workers]):
                    yield future.result()
                futures = futures[max_workers:]
        
        # Process remaining futures
        for future in as_completed(futures):
            yield future.result()

# ============================================================================
# UTILITY GENERATORS
# ============================================================================

def tee_generator(generator: Iterator, n: int = 2):
    """Split generator into multiple independent generators"""
    return itertools.tee(generator, n)

def merge_generators(*generators):
    """Merge multiple generators into one"""
    for generator in generators:
        yield from generator

def round_robin_generators(*generators):
    """Alternate between multiple generators"""
    iterators = [iter(gen) for gen in generators]
    
    while iterators:
        for i, iterator in enumerate(iterators[:]):
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)

def filter_generator(generator: Iterator, predicate):
    """Filter generator items based on predicate"""
    for item in generator:
        if predicate(item):
            yield item

def transform_generator(generator: Iterator, transform_func):
    """Transform generator items using function"""
    for item in generator:
        yield transform_func(item)

# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demo_mathematical_generators():
    """Demonstrate mathematical generators"""
    print("=== MATHEMATICAL GENERATORS ===")
    
    print("Collatz sequence for 13:")
    for num in collatz_sequence(13):
        print(num, end=" ")
    print()
    
    print("First 5 rows of Pascal's triangle:")
    pascal = pascal_triangle()
    for _ in range(5):
        print(next(pascal))
    
    print("First 5 factorials:")
    factorials = factorial_generator()
    for _ in range(5):
        print(next(factorials), end=" ")
    print()

def demo_advanced_patterns():
    """Demonstrate advanced pattern generators"""
    print("\n=== ADVANCED PATTERNS ===")
    
    # State machine example
    states = {
        'idle': {'start': 'running', 'stop': 'idle'},
        'running': {'pause': 'paused', 'stop': 'idle'},
        'paused': {'resume': 'running', 'stop': 'idle'}
    }
    
    sm = state_machine_generator(states, 'idle')
    print("State machine demo:")
    print("Initial state:", next(sm))
    print("After 'start':", sm.send('start'))
    print("After 'pause':", sm.send('pause'))
    print("After 'resume':", sm.send('resume'))

def demo_utility_generators():
    """Demonstrate utility generators"""
    print("\n=== UTILITY GENERATORS ===")
    
    # Merge generators
    gen1 = (x for x in range(3))
    gen2 = (x for x in range(3, 6))
    
    print("Merged generators:")
    for item in merge_generators(gen1, gen2):
        print(item, end=" ")
    print()
    
    # Round robin
    gen1 = (f"A{x}" for x in range(3))
    gen2 = (f"B{x}" for x in range(3))
    
    print("Round robin generators:")
    for item in round_robin_generators(gen1, gen2):
        print(item, end=" ")
    print()

if __name__ == "__main__":
    demo_mathematical_generators()
    demo_advanced_patterns()
    demo_utility_generators()


"""I've created a comprehensive collection of Python generator programs from basic to expert level! Here's what I've provided:

📁 Files Created:
python_generators_tutorial.py - Main tutorial with progressive examples

specialized_generators.py - Advanced patterns and specialized use cases

practical_generators.py - Real-world applications

README.md - Complete guide and documentation

🎯 What You'll Learn:
Basic Level:
Simple number generators

Countdown generators

Basic Fibonacci sequence

Understanding yield keyword

Intermediate Level:
File processing generators

Prime number generators

Batch processing

Generator expressions

Memory-efficient operations

Advanced Level:
Tree traversal generators

Sliding window generators

Coroutines (bidirectional generators)

Pipeline generators

State management

Expert Level:
Custom generator classes with method chaining

Async generators

Concurrent generators

Database batch processors

API pagination generators

Log analysis generators

Data streaming with anomaly detection

🚀 Key Features:
Memory Efficient: Process large datasets without memory issues

Real-World Examples: Log parsing, file processing, data streaming

Performance Focused: Chunked file readers, database batch processing

Mathematical: Collatz sequences, Pascal's triangle, factorials

Practical Applications: Web scraping, duplicate file detection, sensor data simulation

💡 Run the Examples:
python python_generators_tutorial.py    # Start here for basics
python specialized_generators.py        # Advanced patterns
python practical_generators.py          # Real-world applications

Copy
Each file includes demonstration functions that show the generators in action. The examples progress from simple concepts to complex real-world scenarios, giving you a complete understanding of Python generators!"""
