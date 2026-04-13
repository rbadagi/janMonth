Here are **clear, beginner‑friendly examples of `zip()` in Python**, from **basic to slightly advanced**, with explanations.

***

## ✅ What is `zip()`?

`zip()` **combines multiple iterables element‑by‑element** into tuples.

```python
zip(iterable1, iterable2, ...)
```

***

## 1️⃣ Basic Example – Zipping Two Lists

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

result = zip(a, b)
print(list(result))
```

✅ Output:

```python
[(1, 'a'), (2, 'b'), (3, 'c')]
```

📌 Each element is paired by **index**

***

## 2️⃣ Looping with `zip()`

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)
```

✅ Output:

    Alice 85
    Bob 90
    Charlie 95

***

## 3️⃣ Zipping More Than Two Iterables

```python
ids = [101, 102, 103]
names = ["Ram", "Shyam", "Mohan"]
marks = [80, 85, 90]

print(list(zip(ids, names, marks)))
```

✅ Output:

```python
[(101, 'Ram', 80), (102, 'Shyam', 85), (103, 'Mohan', 90)]
```

***

## 4️⃣ Unequal Length Iterables

`zip()` **stops at the shortest iterable**

```python
a = [1, 2, 3, 4]
b = ['x', 'y']

print(list(zip(a, b)))
```

✅ Output:

```python
[(1, 'x'), (2, 'y')]
```

***

## 5️⃣ Convert Two Lists Into a Dictionary

```python
keys = ["name", "age", "city"]
values = ["Raghav", 22, "Bangalore"]

data = dict(zip(keys, values))
print(data)
```

✅ Output:

```python
{'name': 'Raghav', 'age': 22, 'city': 'Bangalore'}
```

📌 Very common interview use ✅

***

## 6️⃣ Unzipping Using `zip(*)`

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

nums, letters = zip(*pairs)

print(nums)
print(letters)
```

✅ Output:

```python
(1, 2, 3)
('a', 'b', 'c')
```

***

## 7️⃣ Using `zip()` with List Comprehension

```python
a = [1, 2, 3]
b = [4, 5, 6]

sum_list = [x + y for x, y in zip(a, b)]
print(sum_list)
```

✅ Output:

```python
[5, 7, 9]
```

***

## 8️⃣ Matrix Transpose Using `zip()` (Important 💡)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(zip(*matrix))
print(transpose)
```

✅ Output:

```python
[(1, 4), (2, 5), (3, 6)]
```

📌 Very useful in DSA & ML

***

## 9️⃣ zip() with `enumerate()`

```python
names = ["Ram", "Shyam", "Mohan"]

for index, name in enumerate(names):
    print(index, name)
```

✅ Equivalent clarity `[zip is not required here but useful when pairing]`

***

## 🔑 Key Points to Remember

*   `zip()` returns an **iterator** (convert to list/tuple if needed)
*   Stops at **shortest iterable**
*   Very efficient (memory‑friendly)
*   Widely used in:
    *   ✅ DSA
    *   ✅ Data processing
    *   ✅ Dictionaries
    *   ✅ Matrix problems

***

## 🎯 Common Interview Question

**Q: What happens if iterables are of different lengths?**  
✅ Answer: `zip()` stops at the shortest iterable.

***

## Want Next?

I can show:

*   🔥 `zip()` vs `map()`
*   🧩 LeetCode problems using `zip()`
*   🧠 `zip()` trick questions for interviews
*   📄 A **Python cheat sheet PDF**

Just tell me 👍
