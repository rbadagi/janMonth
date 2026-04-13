In **Python**, the **LEGB rule** defines how Python **resolves variable names** (i.e., determines which variable value to use when a name is referenced).

**LEGB** stands for:

> **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in

Python looks for a variable in this order.

***

## 1️⃣ Local Scope (L)

Variables **defined inside the current function**.

```python
def my_func():
    x = 10  # local variable
    print(x)

my_func()
```

✅ `x` is found immediately in the local scope.

***

## 2️⃣ Enclosing Scope (E)

Variables in the **outer (enclosing) function** of a nested function.

```python
def outer():
    x = 20  # enclosing variable

    def inner():
        print(x)  # found in enclosing scope

    inner()

outer()
```

✅ `x` is not local to `inner()`, so Python checks the enclosing function.

***

## 3️⃣ Global Scope (G)

Variables **defined at the top level** of the script or module.

```python
x = 30  # global variable

def my_func():
    print(x)

my_func()
```

✅ `x` is found in the global scope.

***

## 4️⃣ Built-in Scope (B)

Names that are **built into Python**, such as `len`, `print`, `sum`, etc.

```python
print(len("Python"))
```

✅ `len` comes from the built-in namespace.

***

## ✅ Full LEGB Lookup Order

When Python encounters a variable name, it searches in this exact sequence:

    Local
    → Enclosing
    → Global
    → Built-in

If the variable is **not found anywhere**, Python raises:

```python
NameError: name 'x' is not defined
```

***

## 🧠 Example Showing All Scopes Together

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

**Output:**

    local

✅ Python stops searching once it finds the name.

***

## ⚠️ Important Notes

### 🔹 Modifying global variables

To modify a global variable inside a function:

```python
x = 5

def change():
    global x
    x = 10

change()
print(x)
```

### 🔹 Modifying enclosing variables

Use `nonlocal`:

```python
def outer():
    x = 5

    def inner():
        nonlocal x
        x = 10

    inner()
    print(x)

outer()
```

***

## ✅ Why LEGB Rule Matters

*   Prevents **unexpected variable clashes**
*   Makes code **predictable and clean**
*   Essential for understanding **functions, closures, and lambdas**

***

If you’d like, I can also give:

*   Interview questions on LEGB
*   Common bugs caused by LEGB
*   Visual diagrams
*   Practice exercises

Just tell me 👍
