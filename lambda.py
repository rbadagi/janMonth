"""
Python Lambda Functions: Basic to Expert Level Examples
======================================================
"""

import functools
import operator
from typing import Callable, List, Dict, Any

# ============================================================================
# BASIC LEVEL LAMBDA FUNCTIONS
# ============================================================================

def basic_lambda_examples():
    """Basic lambda function examples"""
    print("=== BASIC LAMBDA FUNCTIONS ===")
    
    # Simple arithmetic operations
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    square = lambda x: x ** 2
    
    print(f"Add 5 + 3: {add(5, 3)}")
    print(f"Multiply 4 * 6: {multiply(4, 6)}")
    print(f"Square of 7: {square(7)}")
    
    # String operations
    uppercase = lambda s: s.upper()
    reverse = lambda s: s[::-1]
    
    print(f"Uppercase 'hello': {uppercase('hello')}")
    print(f"Reverse 'python': {reverse('python')}")
    
    # Conditional lambda
    max_of_two = lambda a, b: a if a > b else b
    is_even = lambda n: n % 2 == 0
    
    print(f"Max of 10, 15: {max_of_two(10, 15)}")
    print(f"Is 8 even? {is_even(8)}")

def lambda_with_builtin_functions():
    """Lambda functions with built-in functions"""
    print("\n=== LAMBDA WITH BUILT-IN FUNCTIONS ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Using map()
    squares = list(map(lambda x: x**2, numbers))
    print(f"Squares: {squares}")
    
    # Using filter()
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Using reduce()
    from functools import reduce
    sum_all = reduce(lambda x, y: x + y, numbers)
    print(f"Sum of all numbers: {sum_all}")
    
    # String operations
    words = ['python', 'lambda', 'function', 'programming']
    lengths = list(map(lambda word: len(word), words))
    print(f"Word lengths: {lengths}")
    
    long_words = list(filter(lambda word: len(word) > 6, words))
    print(f"Long words: {long_words}")

# ============================================================================
# INTERMEDIATE LEVEL LAMBDA FUNCTIONS
# ============================================================================

def intermediate_lambda_examples():
    """Intermediate lambda function examples"""
    print("\n=== INTERMEDIATE LAMBDA FUNCTIONS ===")
    
    # Lambda with multiple conditions
    grade_classifier = lambda score: (
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'D' if score >= 60 else 'F'
    )
    
    scores = [95, 87, 72, 65, 45]
    grades = list(map(grade_classifier, scores))
    print(f"Grades: {grades}")
    
    # Lambda with nested operations
    students = [
        {'name': 'Alice', 'age': 20, 'grade': 85},
        {'name': 'Bob', 'age': 22, 'grade': 92},
        {'name': 'Charlie', 'age': 19, 'grade': 78}
    ]
    
    # Sort by grade (descending)
    sorted_by_grade = sorted(students, key=lambda student: student['grade'], reverse=True)
    print("Students sorted by grade:")
    for student in sorted_by_grade:
        print(f"  {student['name']}: {student['grade']}")
    
    # Complex filtering
    high_performers = list(filter(lambda s: s['grade'] > 80 and s['age'] < 21, students))
    print(f"High performers under 21: {[s['name'] for s in high_performers]}")

def lambda_with_data_structures():
    """Lambda functions with various data structures"""
    print("\n=== LAMBDA WITH DATA STRUCTURES ===")
    
    # Working with dictionaries
    inventory = {
        'apples': 50,
        'bananas': 30,
        'oranges': 25,
        'grapes': 40
    }
    
    # Filter items with quantity > 30
    high_stock = dict(filter(lambda item: item[1] > 30, inventory.items()))
    print(f"High stock items: {high_stock}")
    
    # Transform values (apply 10% discount)
    discounted = dict(map(lambda item: (item[0], item[1] * 0.9), inventory.items()))
    print(f"After 10% discount: {discounted}")
    
    # Working with nested lists
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Flatten matrix
    flattened = list(map(lambda row: list(map(lambda x: x, row)), matrix))
    flat_list = [item for row in flattened for item in row]
    print(f"Flattened matrix: {flat_list}")
    
    # Sum each row
    row_sums = list(map(lambda row: sum(row), matrix))
    print(f"Row sums: {row_sums}")

# ============================================================================
# ADVANCED LEVEL LAMBDA FUNCTIONS
# ============================================================================

def advanced_lambda_patterns():
    """Advanced lambda function patterns"""
    print("\n=== ADVANCED LAMBDA PATTERNS ===")
    
    # Lambda returning lambda (closure)
    multiplier = lambda n: lambda x: x * n
    double = multiplier(2)
    triple = multiplier(3)
    
    print(f"Double 5: {double(5)}")
    print(f"Triple 4: {triple(4)}")
    
    # Lambda with default arguments
    power = lambda x, n=2: x ** n
    print(f"2^3: {power(2, 3)}")
    print(f"5^2 (default): {power(5)}")
    
    # Lambda with *args and **kwargs
    flexible_lambda = lambda *args, **kwargs: {
        'args': args,
        'kwargs': kwargs,
        'total_args': len(args) + len(kwargs)
    }
    
    result = flexible_lambda(1, 2, 3, name='Alice', age=25)
    print(f"Flexible lambda result: {result}")

def lambda_decorators():
    """Lambda functions as decorators"""
    print("\n=== LAMBDA AS DECORATORS ===")
    
    # Simple timing decorator using lambda
    import time
    
    def timer_decorator(func):
        return lambda *args, **kwargs: (
            lambda start_time: (
                lambda result: (
                    print(f"Function {func.__name__} took {time.time() - start_time:.4f} seconds"),
                    result
                )[1]
            )(func(*args, **kwargs))
        )(time.time())
    
    @timer_decorator
    def slow_function():
        time.sleep(0.1)
        return "Done!"
    
    result = slow_function()
    print(f"Result: {result}")

def functional_programming_with_lambda():
    """Functional programming concepts with lambda"""
    print("\n=== FUNCTIONAL PROGRAMMING WITH LAMBDA ===")
    
    # Compose functions
    compose = lambda f, g: lambda x: f(g(x))
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    
    # Compose: first multiply by 2, then add 1
    composed = compose(add_one, multiply_by_two)
    print(f"Composed function (5): {composed(5)}")  # (5 * 2) + 1 = 11
    
    # Partial application
    partial = lambda func, *partial_args: lambda *args: func(*(partial_args + args))
    
    def greet(greeting, name, punctuation):
        return f"{greeting}, {name}{punctuation}"
    
    say_hello = partial(greet, "Hello")
    enthusiastic_hello = partial(say_hello, punctuation="!")
    
    print(f"Partial application: {enthusiastic_hello('Alice')}")
    
    # Currying
    curry_add = lambda x: lambda y: lambda z: x + y + z
    add_5 = curry_add(5)
    add_5_and_3 = add_5(3)
    result = add_5_and_3(2)
    print(f"Curried addition (5+3+2): {result}")

# ============================================================================
# EXPERT LEVEL LAMBDA FUNCTIONS
# ============================================================================

def lambda_with_classes():
    """Lambda functions with classes and objects"""
    print("\n=== LAMBDA WITH CLASSES ===")
    
    class DataProcessor:
        def __init__(self):
            self.operations = []
        
        def add_operation(self, operation):
            self.operations.append(operation)
            return self
        
        def process(self, data):
            result = data
            for operation in self.operations:
                result = operation(result)
            return result
    
    # Chain operations using lambda
    processor = DataProcessor()
    processor.add_operation(lambda x: x * 2) \
             .add_operation(lambda x: x + 10) \
             .add_operation(lambda x: x ** 2)
    
    result = processor.process(5)
    print(f"Chained operations on 5: {result}")  # ((5*2)+10)^2 = 400
    
    # Lambda as class methods
    class Calculator:
        operations = {
            'add': lambda self, x, y: x + y,
            'multiply': lambda self, x, y: x * y,
            'power': lambda self, x, y: x ** y
        }
        
        def calculate(self, operation, x, y):
            return self.operations[operation](self, x, y)
    
    calc = Calculator()
    print(f"Calculator add: {calc.calculate('add', 10, 5)}")
    print(f"Calculator power: {calc.calculate('power', 2, 8)}")

def advanced_data_processing():
    """Advanced data processing with lambda"""
    print("\n=== ADVANCED DATA PROCESSING ===")
    
    # Complex data transformation pipeline
    sales_data = [
        {'product': 'laptop', 'price': 1000, 'quantity': 2, 'category': 'electronics'},
        {'product': 'mouse', 'price': 25, 'quantity': 10, 'category': 'electronics'},
        {'product': 'book', 'price': 15, 'quantity': 5, 'category': 'education'},
        {'product': 'pen', 'price': 2, 'quantity': 50, 'category': 'office'},
    ]
    
    # Pipeline: calculate total, filter high-value, sort by total
    pipeline = [
        lambda data: map(lambda item: {**item, 'total': item['price'] * item['quantity']}, data),
        lambda data: filter(lambda item: item['total'] > 50, data),
        lambda data: sorted(data, key=lambda item: item['total'], reverse=True)
    ]
    
    # Apply pipeline
    result = sales_data
    for operation in pipeline:
        result = operation(result)
    
    result = list(result)  # Convert to list for printing
    print("Processed sales data:")
    for item in result:
        print(f"  {item['product']}: ${item['total']}")
    
    # Group by category using lambda
    from itertools import groupby
    
    # Sort by category first
    sorted_by_category = sorted(sales_data, key=lambda x: x['category'])
    
    # Group by category
    grouped = {
        category: list(items) 
        for category, items in groupby(sorted_by_category, key=lambda x: x['category'])
    }
    
    print("\nGrouped by category:")
    for category, items in grouped.items():
        total_value = sum(map(lambda item: item['price'] * item['quantity'], items))
        print(f"  {category}: ${total_value}")

def lambda_with_async():
    """Lambda functions with async operations"""
    print("\n=== LAMBDA WITH ASYNC ===")
    
    import asyncio
    
    # Async lambda (Note: This is more of a demonstration)
    async def async_lambda_demo():
        # Create async operations using lambda-like syntax
        async_operations = [
            lambda: asyncio.sleep(0.1),
            lambda: asyncio.sleep(0.2),
            lambda: asyncio.sleep(0.05)
        ]
        
        # Execute all operations concurrently
        await asyncio.gather(*[op() for op in async_operations])
        return "All async operations completed"
    
    # Run the async demo
    try:
        result = asyncio.run(async_lambda_demo())
        print(f"Async result: {result}")
    except Exception as e:
        print(f"Async demo skipped: {e}")

def meta_programming_with_lambda():
    """Meta-programming concepts with lambda"""
    print("\n=== META-PROGRAMMING WITH LAMBDA ===")
    
    # Dynamic function creation
    def create_validator(field_name, validation_func):
        return lambda obj: {
            'field': field_name,
            'valid': validation_func(getattr(obj, field_name, None)),
            'value': getattr(obj, field_name, None)
        }
    
    # Create validators using lambda
    validators = [
        create_validator('age', lambda x: x is not None and 0 <= x <= 120),
        create_validator('email', lambda x: x is not None and '@' in str(x)),
        create_validator('name', lambda x: x is not None and len(str(x)) > 0)
    ]
    
    class Person:
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
    
    person = Person("Alice", 25, "alice@example.com")
    
    # Validate using dynamically created validators
    validation_results = [validator(person) for validator in validators]
    print("Validation results:")
    for result in validation_results:
        status = "✓" if result['valid'] else "✗"
        print(f"  {status} {result['field']}: {result['value']}")

def lambda_performance_patterns():
    """Performance-oriented lambda patterns"""
    print("\n=== LAMBDA PERFORMANCE PATTERNS ===")
    
    # Memoization with lambda
    def memoize(func):
        cache = {}
        return lambda *args: cache.setdefault(args, func(*args))
    
    # Expensive function
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # Memoized version
    fast_fibonacci = memoize(fibonacci)
    
    import time
    
    # Test performance
    start = time.time()
    result1 = fibonacci(30)
    time1 = time.time() - start
    
    start = time.time()
    result2 = fast_fibonacci(30)
    time2 = time.time() - start
    
    print(f"Regular fibonacci(30): {result1} in {time1:.4f}s")
    print(f"Memoized fibonacci(30): {result2} in {time2:.4f}s")
    
    # Lazy evaluation with lambda
    lazy_operations = [
        lambda: sum(range(1000000)),
        lambda: max(range(1000000)),
        lambda: len(list(filter(lambda x: x % 2 == 0, range(1000000))))
    ]
    
    print("Lazy operations created (not executed yet)")
    
    # Execute only when needed
    result = lazy_operations[0]()  # Only execute the first operation
    print(f"First lazy operation result: {result}")

# ============================================================================
# REAL-WORLD LAMBDA APPLICATIONS
# ============================================================================

def real_world_lambda_examples():
    """Real-world lambda function applications"""
    print("\n=== REAL-WORLD LAMBDA APPLICATIONS ===")
    
    # API response processing
    api_responses = [
        {'status': 200, 'data': {'users': 150}, 'timestamp': '2024-01-01'},
        {'status': 404, 'data': None, 'timestamp': '2024-01-02'},
        {'status': 200, 'data': {'users': 175}, 'timestamp': '2024-01-03'},
    ]
    
    # Process API responses
    successful_responses = list(filter(lambda r: r['status'] == 200, api_responses))
    user_counts = list(map(lambda r: r['data']['users'], successful_responses))
    
    print(f"User counts from successful API calls: {user_counts}")
    
    # Log processing
    log_entries = [
        "2024-01-01 10:00:00 INFO User login successful",
        "2024-01-01 10:05:00 ERROR Database connection failed",
        "2024-01-01 10:10:00 INFO User logout",
        "2024-01-01 10:15:00 WARNING High memory usage"
    ]
    
    # Extract error logs
    error_logs = list(filter(lambda log: 'ERROR' in log, log_entries))
    print(f"Error logs: {error_logs}")
    
    # Configuration processing
    config = {
        'database_url': 'localhost:5432',
        'debug_mode': 'true',
        'max_connections': '100',
        'timeout': '30'
    }
    
    # Convert string values to appropriate types
    type_converters = {
        'debug_mode': lambda x: x.lower() == 'true',
        'max_connections': lambda x: int(x),
        'timeout': lambda x: int(x)
    }
    
    processed_config = {
        key: type_converters.get(key, lambda x: x)(value)
        for key, value in config.items()
    }
    
    print(f"Processed config: {processed_config}")

# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def run_all_examples():
    """Run all lambda function examples"""
    basic_lambda_examples()
    lambda_with_builtin_functions()
    intermediate_lambda_examples()
    lambda_with_data_structures()
    advanced_lambda_patterns()
    lambda_decorators()
    functional_programming_with_lambda()
    lambda_with_classes()
    advanced_data_processing()
    lambda_with_async()
    meta_programming_with_lambda()
    lambda_performance_patterns()
    real_world_lambda_examples()

if __name__ == "__main__":
    run_all_examples()
