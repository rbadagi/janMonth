# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#
#         if guess == target:
#             return mid  # Return the index where it's found
#         if guess > target:
#             high = mid - 1  # Target is in the left half
#         else:
#             low = mid + 1   # Target is in the right half
#
#     return -1  # Target not found
#
# # Example
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# result1 = binary_search(my_list, 70)
# print(f"Target found at index: {result1}")


# def binary_search_recursive(arr, target, low, high):
#     # Base Case: If the range is invalid, the target isn't here
#     if low > high:
#         return -1
#
#     # Find the middle index
#     mid = (low + high) // 2
#
#     # Case 1: Found the target
#     if arr[mid] == target:
#         return mid
#
#     # Case 2: Target is smaller, search the left half
#     elif arr[mid] > target:
#         return binary_search_recursive(arr, target, low, mid - 1)
#
#     # Case 3: Target is larger, search the right half
#     else:
#         return binary_search_recursive(arr, target, mid + 1, high)
#
#
# # Test the code
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target = 70
# result = binary_search_recursive(my_list, target, 0, len(my_list) - 1)
#
# print(f"Target found at index: {result}")

"""If asked:
# 
# “How does binary search handle duplicates?”
# 
# Correct answer:
# 
# Binary search will return any one of the matching elements. 
# To find the first or last occurrence, we must modify the algorithm 
# by continuing the search even after finding a match."""


#Standard Binary Search (Returns Any Duplicate)

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == target:
#             return mid  # could be ANY matching index
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1


# """Finding the First Occurrence of a Duplicate
# To get the leftmost index, we slightly modify binary search.
# Approach
#
# When arr[mid] == target,
# ✅ Continue searching on the left side"""

def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid      # store index
            right = mid - 1   # move left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# """Finding the Last Occurrence of a Duplicate
# Now we do the opposite.
# Approach
#
# When arr[mid] == target,
# ✅ Continue searching on the right side"""

def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid      # store index
            left = mid + 1    # move right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# """Counting Number of Duplicates Using Binary Search
# Once we have first and last occurrence:"""

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0

    last = last_occurrence(arr, target)
    return last - first + 1


# Summary Table (Conceptual)
# RequirementBinary Search Behavior
# Find any match✅ Standard binary search
# Find first occurrence✅ Modified binary search
# Find last occurrence✅ Modified binary search
# Count duplicates✅ First + last occurrence
# Stable result❌ Not guaranteed by default"""
