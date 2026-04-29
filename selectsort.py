#basic example in ascending order
"""def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        print("current arr is", arr)
        print("value of min_index value", arr[min_index])

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                print("current values of arr[j] and arr[min_index] are", arr[j], arr[min_index])
                print(arr[j], "<", arr[min_index])
                min_index = j

        # Swap the found minimum with the first element
        if min_index != i:
            print("before swap ", arr[i],arr[min_index])
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print("after swap ", arr[i],arr[min_index])
    print("current sorted arr is", arr)
    return arr


numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))

#Selection Sort With Step-by-Step Output (For Learning)
def selection_sort_verbose(arr):
    n = len(arr)
    print(f"Before pass: {arr}")

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index!= i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"After pass {i + 1}: {arr}")

data = [29, 10, 14, 37, 13]
selection_sort_verbose(data)

#Selection Sort (Descending Order)
def selection_sort_desc(arr):
    n = len(arr)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


nums = [5, 3, 8, 6, 2]
print(selection_sort_desc(nums))

#Selection Sort Without Modifying Original List
def selection_sort_copy(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


original = [7, 4, 1, 9]
sorted_list = selection_sort_copy(original)

print("Original:", original)
print("Sorted:", sorted_list)"""

# Selection Sort Using Index Logic Only (Interview-Friendly)
def selection_sort_index(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[smallest]:
                smallest = j

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr

nums = [69, 24, 13, 26, 10, 8]
print(selection_sort_index(nums))

