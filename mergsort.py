#merge sort
def merge_sort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # 1. Split: Find the middle and divide the list
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. Conquer: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. Combine: Merge the sorted halves back together
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # If elements remain in left or right, add them to the result
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Test the code
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print(f"Sorted array: {sorted_numbers}")


#method 3
def merge_sort3(left, right):
    result = []
    i = j = 0
