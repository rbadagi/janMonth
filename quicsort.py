##
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # choose last element as pivot
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [10, 7, 8, 9, 1, 5]
sorted_nums = quick_sort(nums)
print(sorted_nums)

def partition_1(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition_1(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)

def partition(arr, low, high):
    pivot = arr[high]      # choose last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort_iterative(arr):
    n = len(arr)

    # Stack to store (low, high) pairs
    stack = []
    stack.append((0, n - 1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            # Push right side to stack
            stack.append((pivot_index + 1, high))

            # Push left side to stack
            stack.append((low, pivot_index - 1))

arr = [10, 7, 8, 9, 1, 5]
quick_sort_iterative(arr)
print(arr)


