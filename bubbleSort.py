##Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [5, 1, 4, 2, 8]
bubble_sort(nums)
print(nums)

def bubble_sort_verbose(arr):
    n = len(arr)
    for i in range(n):
        print(f"Pass {i + 1}:")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
        print()

nums = [3, 2, 1]
bubble_sort_verbose(nums)

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

nums = [1, 2, 3, 4, 5]
bubble_sort_optimized(nums)
print(nums)

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [10, 3, 7, 1]
bubble_sort_desc(nums)
print(nums)

def bubble_sort_while(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1

nums = [4, 2, 6, 1]
bubble_sort_while(nums)
print(nums)

