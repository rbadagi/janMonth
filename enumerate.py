#rrr
Here are some **clear and practical examples of `enumerate()` in Python**, starting from basics and moving to real‑world use cases.

***

## 1. Basic usage with a list

`enumerate()` lets you loop over items **while also getting their index**.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output**

    0 apple
    1 banana
    2 cherry

***

## 2. Starting the index from a custom value

You can change the starting index using the `start` parameter.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

**Output**

    1 apple
    2 banana
    3 cherry

✅ Useful when displaying numbered lists to users.

***

## 3. Replacing `range(len(...))` (best practice)

❌ Less readable:

```python
names = ["Ravi", "Anita", "Suresh"]

for i in range(len(names)):
    print(i, names[i])
```

✅ Better with `enumerate()`:

```python
for i, name in enumerate(names):
    print(i, name)
```

***

## 4. Enumerate with strings

Strings are iterable too.

```python
word = "Python"

for index, ch in enumerate(word):
    print(index, ch)
```

**Output**

    0 P
    1 y
    2 t
    3 h
    4 o
    5 n

***

## 5. Enumerate with lists of tuples

Very common in real projects.

```python
students = [("Ravi", 85), ("Anita", 92), ("Suresh", 78)]

for i, (name, marks) in enumerate(students, start=1):
    print(f"{i}. {name} scored {marks}")
```

***

## 6. Finding an item’s index safely

Instead of using `.index()` (which can fail if not found):

```python
numbers = [10, 20, 30, 40]

for i, num in enumerate(numbers):
    if num == 30:
        print("Found at index:", i)
```

***

## 7. Enumerate inside list comprehension

You can use it in one‑liners too.

```python
words = ["hi", "hello", "bye"]

indexed_words = [(i, word.upper()) for i, word in enumerate(words)]
print(indexed_words)
```

**Output**

    [(0, 'HI'), (1, 'HELLO'), (2, 'BYE')]

***

## 8. Parallel iteration (enumerate + condition)

Example: print only even‑index elements.

```python
data = [5, 10, 15, 20, 25]

for i, value in enumerate(data):
    if i % 2 == 0:
        print(value)
```

***

## Summary

`enumerate()` is used when you need:

*   ✅ Index + value together
*   ✅ Cleaner and readable loops
*   ✅ Less error‑prone code than `range(len())`

If you want, I can also show:

*   `enumerate()` vs `zip()`
*   Common interview questions
*   Real examples from data processing or automation

Just tell me 👍


Here are some **clear and practical examples of `enumerate()` in Python**, starting from basics and moving to real‑world use cases.

***

## 1. Basic usage with a list

`enumerate()` lets you loop over items **while also getting their index**.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output**

    0 apple
    1 banana
    2 cherry

***

## 2. Starting the index from a custom value

You can change the starting index using the `start` parameter.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

**Output**

    1 apple
    2 banana
    3 cherry

✅ Useful when displaying numbered lists to users.

***

## 3. Replacing `range(len(...))` (best practice)

❌ Less readable:

```python
names = ["Ravi", "Anita", "Suresh"]

for i in range(len(names)):
    print(i, names[i])
```

✅ Better with `enumerate()`:

```python
for i, name in enumerate(names):
    print(i, name)
```

***

## 4. Enumerate with strings

Strings are iterable too.

```python
word = "Python"

for index, ch in enumerate(word):
    print(index, ch)
```

**Output**

    0 P
    1 y
    2 t
    3 h
    4 o
    5 n

***

## 5. Enumerate with lists of tuples

Very common in real projects.

```python
students = [("Ravi", 85), ("Anita", 92), ("Suresh", 78)]

for i, (name, marks) in enumerate(students, start=1):
    print(f"{i}. {name} scored {marks}")
```

***

## 6. Finding an item’s index safely

Instead of using `.index()` (which can fail if not found):

```python
numbers = [10, 20, 30, 40]

for i, num in enumerate(numbers):
    if num == 30:
        print("Found at index:", i)
```

***

## 7. Enumerate inside list comprehension

You can use it in one‑liners too.

```python
words = ["hi", "hello", "bye"]

indexed_words = [(i, word.upper()) for i, word in enumerate(words)]
print(indexed_words)
```

**Output**

    [(0, 'HI'), (1, 'HELLO'), (2, 'BYE')]

***

## 8. Parallel iteration (enumerate + condition)

Example: print only even‑index elements.

```python
data = [5, 10, 15, 20, 25]

for i, value in enumerate(data):
    if i % 2 == 0:
        print(value)
```

***

## Summary

`enumerate()` is used when you need:

*   ✅ Index + value together
*   ✅ Cleaner and readable loops
*   ✅ Less error‑prone code than `range(len())`

If you want, I can also show:

*   `enumerate()` vs `zip()`
*   Common interview questions
*   Real examples from data processing or automation

Just tell me 👍
