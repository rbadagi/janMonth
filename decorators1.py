#aa
#1. Basic Decorator (Print before/after)
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@simple_logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#Kwargs usage
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Called with args={args}, kwargs={kwargs}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def create_user(name, age, city="Unknown", active=True):
    time.sleep(0.3)
    return f"{name}, {age}, {city}, active={active}"

# All these work thanks to **kwargs
print(create_user("Alice", 30))
print(create_user("Bob", 25, city="NYC", active=False))
print(create_user("Charlie", 40, city="London"))

#use @wraps
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@timer
def greet():
    """Says hello"""
    print("Hello!")

print(greet.__name__)    # greet      ✅
print(greet.__doc__)     # Says hello ✅


#Time Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

print(slow_add(2, 3))


#Decorator with Arguments
import time

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i+1}/{n}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()


#Preserving Metadata with functools.wraps
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def compute(x):
    """Squares a number."""
    return x ** 2

print(compute.__name__)  # compute (not wrapper)
print(compute.__doc__)   # Squares a number.


#Stacking Multiple Decorators
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__}: {time.time() - start:.4f}s")
        return result
    return wrapper

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] return={result}")
        return result
    return wrapper

@timer
@debug
def multiply(a, b):
    time.sleep(0.5)
    return a * b

multiply(3, 4)


#Class-Based Decorator
import time

class Timer:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"{self.__name__}: {time.time() - start:.4f}s")
        return result

@Timer
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(10))


#7. Expert — Decorator with Optional Arguments + Timing Threshold
import time
from functools import wraps

def monitor(func=None, *, threshold=1.0):
    """Warns if function exceeds time threshold."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed = time.perf_counter() - start
            if elapsed > threshold:
                print(f"⚠ SLOW: {fn.__name__} took {elapsed:.4f}s (threshold={threshold}s)")
            else:
                print(f"✓ OK: {fn.__name__} took {elapsed:.4f}s")
            return result
        return wrapper

    # Allows @monitor or @monitor(threshold=2.0)
    if func is not None:
        return decorator(func)
    return decorator

@monitor
def fast():
    time.sleep(0.2)

@monitor(threshold=0.5)
def slow():
    time.sleep(1)

fast()  # ✓ OK
slow()  # ⚠ SLOW

#Expert — Decorator That Caches + Logs Timing
import time
from functools import wraps

def cached_timer(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"[CACHE HIT] {func.__name__}{args} = {cache[args]}")
            return cache[args]
        start = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - start
        cache[args] = result
        print(f"[COMPUTED] {func.__name__}{args} = {result} ({elapsed:.4f}s)")
        return result
    return wrapper

@cached_timer
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(10)
fib(10)  # cache hit


"""Key takeaways:

A decorator wraps a function, taking it as input and returning a new function

Use *args, **kwargs to make decorators work with any function signature

Always use @wraps(func) to preserve the original function's metadata

Decorators with arguments need an extra nesting level

time.perf_counter() is more precise than time.time() for benchmarking

Decorators can be stacked — they apply bottom-up"""




#Retry Decorator — retries on failure
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise Exception(f"{func.__name__} failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server down")
    return "Data fetched!"

print(fetch_data())


#Access Control - restricts by role
from functools import wraps

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                print(f"Access denied: {user['name']} is not {role}")
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user, target):
    return f"{user['name']} deleted {target}"

print(delete_user({"name": "Alice", "role": "admin"}, "Bob"))    # works
print(delete_user({"name": "Charlie", "role": "viewer"}, "Bob")) # denied



#Rate Limiter - limits calls per second
import time
from functools import wraps

def rate_limit(max_calls, period=1.0):
    calls = []
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [t for t in calls if now - t < period]
            if len(calls) >= max_calls:
                print(f"Rate limited! Max {max_calls} calls per {period}s")
                return None
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=2, period=1.0)
def send_message(msg):
    print(f"Sent: {msg}")

send_message("Hi")      # Sent
send_message("Hello")   # Sent
send_message("Hey")     # Rate limited!


#Validate Types - checks argument types
from functools import wraps

def validate_types(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for arg, expected in zip(args, types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected.__name__}, got {type(arg).__name__}")
            return func(*args)
        return wrapper
    return decorator

@validate_types(str, int)
def register(name, age):
    return f"{name} is {age}"

print(register("Alice", 25))   # works
print(register("Alice", "25")) # TypeError


#Decorator Factory - creates decorators dynamically
import time
from functools import wraps

def log_to(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            line = f"{func.__name__} | args={args} | result={result} | time={elapsed:.4f}s\n"
            with open(filename, "a") as f:
                f.write(line)
            print(f"Logged to {filename}")
            return result
        return wrapper
    return decorator

@log_to("app.log")
def add(a, b):
    return a + b

@log_to("errors.log")
def divide(a, b):
    return a / b

add(2, 3)
divide(10, 2)



"""The common pattern in all of these — a function that takes parameters, returns a decorator, 
which returns a wrapper. Three levels of nesting:
def outer(params):          # accepts decorator arguments
    def decorator(func):    # accepts the function
        def wrapper(*args): # accepts function arguments
            ...
        return wrapper
    return decorator
    
Python has no hard limit on nesting levels. But practically:

3 levels — standard for decorators with arguments (what you saw above)

4 levels — decorator that creates decorator factories

Beyond 4 — technically possible but becomes unreadable and unnecessary

4 Levels — Decorator Generator"""

from functools import wraps

def config(env):                          # Level 1: config
    def decorator_factory(prefix):        # Level 2: factory
        def decorator(func):             # Level 3: decorator
            @wraps(func)
            def wrapper(*args, **kwargs): # Level 4: wrapper
                print(f"[{env}][{prefix}] Calling {func.__name__}")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    return decorator_factory

# Usage
log = config("PROD")

@log("API")
def get_users():
    return ["Alice", "Bob"]

@log("DB")
def query():
    return "SELECT * FROM users"

get_users()  # [PROD][API] Calling get_users
query()      # [PROD][DB] Calling query


"""Why stop at 3-4?
Levels	Use Case	Readability
2	Simple decorator	✅ Easy
3	Decorator with arguments	✅ Standard
4	Decorator factory generator	⚠️ Complex
5+	Almost never needed	❌ Unreadable
If you need 5+ levels, it's a sign to refactor — use classes instead:"""

class Decorator:
    def __init__(self, env, prefix):
        self.env = env
        self.prefix = prefix

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{self.env}][{self.prefix}] Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

@Decorator("PROD", "API")
def get_users():
    return ["Alice", "Bob"]

get_users()  # [PROD][API] Calling get_users

Rule of thumb: If nesting goes beyond 4, switch to a class-based approach — same power, much cleaner.

