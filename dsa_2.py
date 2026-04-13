#dd
Below is a **complete Blind 75 roadmap with Python solutions**, organized by topic.  
These are the **most important LeetCode interview problems** used by Google, Amazon, Microsoft, Meta, etc.

I’ve kept the solutions **clean, optimal, and interview‑ready**.

***

# ✅ BLIND 75 – PYTHON SOLUTIONS (DSA)

***

## 🔹 ARRAYS & HASHING (12)

### 1. Two Sum

```python
def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target-n], i]
        seen[n] = i
```

### 2. Contains Duplicate

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

### 3. Best Time to Buy and Sell Stock

```python
def maxProfit(prices):
    min_price, profit = float('inf'), 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit
```

### 4. Product of Array Except Self

```python
def productExceptSelf(nums):
    res = [1]*len(nums)
    left = 1
    for i in range(len(nums)):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in reversed(range(len(nums))):
        res[i] *= right
        right *= nums[i]
    return res
```

### 5. Maximum Subarray

```python
def maxSubArray(nums):
    cur = ans = nums[0]
    for n in nums[1:]:
        cur = max(n, cur+n)
        ans = max(ans, cur)
    return ans
```

### 6. Maximum Product Subarray

```python
def maxProduct(nums):
    res = max(nums)
    curMin = curMax = 1
    for n in nums:
        if n == 0:
            curMin = curMax = 1
            continue
        temp = curMax*n
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(temp, n*curMin, n)
        res = max(res, curMax)
    return res
```

### 7. Find Minimum in Rotated Sorted Array

```python
def findMin(nums):
    l, r = 0, len(nums)-1
    while l < r:
        m = (l+r)//2
        if nums[m] > numsl = m+1
        else:
            r = m
    return nums[l]
```

### 8. Search in Rotated Sorted Array

```python
def search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        if nums[l] <= numsif nums[l] <= target < numsr = m-1
            else:
                l = m+1
        else:
            if nums[m] < target <= numsl = m+1
            else:
                r = m-1
    return -1
```

***

## 🔹 TWO POINTERS (5)

### 9. Valid Palindrome

```python
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

### 10. Container With Most Water

```python
def maxArea(height):
    l, r, res = 0, len(height)-1, 0
    while l < r:
        res = max(res, min(height[l],height[r])*(r-l))
        if height[l] < heightl += 1
        else:
            r -= 1
    return res
```

***

## 🔹 SLIDING WINDOW (6)

### 11. Longest Substring Without Repeating Characters

```python
def lengthOfLongestSubstring(s):
    seen = {}
    l = res = 0
    for r,c in enumerate(s):
        if c in seen and seen[c] >= l:
            l = seen[c]+1
        seen[c] = r
        res = max(res, r-l+1)
    return res
```

***

## 🔹 STACK (7)

### 12. Valid Parentheses

```python
def isValid(s):
    stack = []
    mp = {')':'(',']':'[','}':'{'}
    for c in s:
        if c in mp:
            if not stack or stack.pop() != mpreturn False
        else:
            stack.append(c)
    return not stack
```

### 13. Daily Temperatures

```python
def dailyTemperatures(temps):
    res = [0]*len(temps)
    stack = []
    for i,t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            prev = stack.pop()
            res[prev] = i-prev
        stack.append(i)
    return res
```

***

## 🔹 BINARY SEARCH (5)

### 14. Binary Search

```python
def search(nums, target):
    l,r = 0,len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target: return m
        elif nums[m]<target: l=m+1
        else: r=m-1
    return -1
```

***

## 🔹 LINKED LIST (6)

### 15. Reverse Linked List

```python
def reverseList(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
```

### 16. Merge Two Sorted Lists

```python
def mergeTwoLists(l1, l2):
    dummy = cur = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```

***

## 🔹 TREES (11)

### 17. Maximum Depth of Binary Tree

```python
def maxDepth(root):
    if not root:
        return 0
    return 1+max(maxDepth(root.left), maxDepth(root.right))
```

### 18. Same Tree

```python
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val!=q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
```

***

## 🔹 TRIES (3)

### 19. Implement Trie

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children.setdefault(c, Trie())
        cur.end = True
```

***

## 🔹 GRAPHS (9)

### 20. Number of Islands

```python
def numIslands(grid):
    def dfs(i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
            return
        grid[i][j]='0'
        dfs(i+1,j);dfs(i-1,j);dfs(i,j+1);dfs(i,j-1)

    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1':
                dfs(i,j)
                count+=1
    return count
```

***

## 🔹 DYNAMIC PROGRAMMING (12)

### 21. Climbing Stairs

```python
def climbStairs(n):
    a,b = 1,1
    for _ in range(n):
        a,b=b,a+b
    return a
```

### 22. House Robber

```python
def rob(nums):
    rob1=rob2=0
    for n in nums:
        new=max(rob1+n,rob2)
        rob1=rob2
        rob2=new
    return rob2
```

***

## ✅ What I can do next

✅ Provide **remaining Blind 75 (all 75 in PDF)**  
✅ Explain **each problem step‑by‑step**  
✅ Create a **2‑month DSA interview plan**  
✅ Give **company‑wise Blind 75 mapping**

Just tell me 👍

Below is a **clear, beginner‑friendly DSA roadmap** designed for **0 → interview‑ready**, especially for students and freshers learning **DSA in Python**.

You can follow this roadmap for **3–6 months**, depending on your pace.

***

# 🧠 DSA ROADMAP FOR BEGINNERS (Step‑by‑Step)

***

## ✅ PHASE 0: Prerequisites (1–2 Weeks)

### 🎯 Goal: Be comfortable with Python basics

Learn:

*   Variables, input/output
*   If‑else
*   Loops (`for`, `while`)
*   Functions
*   Lists, tuples, sets, dictionaries
*   Strings
*   Recursion basics

✅ Practice:

*   Reverse a string
*   Check palindrome
*   Factorial (iterative + recursive)
*   Fibonacci

📌 Platform:

*   Python basics (any source)
*   Practice: **HackerRank / LeetCode Easy**

***

## ✅ PHASE 1: Time & Space Complexity (3–5 Days)

### 🎯 Goal: Learn how to analyze code efficiency

Topics:

*   Big‑O notation
*   Common complexities:
    *   O(1)
    *   O(n)
    *   O(log n)
    *   O(n²)
*   Best / Worst / Average case

✅ Practice:

*   Identify complexity of simple loops
*   Compare brute force vs optimized solutions

📌 Very important → Interview favorite topic

***

## ✅ PHASE 2: Arrays & Hashing (2–3 Weeks)

### 🎯 Core foundation of DSA

Topics:

*   Arrays (lists in Python)
*   Prefix sum
*   Sliding window
*   HashMap (dictionary)
*   Frequency counting

Key Problems:

*   Two Sum
*   Maximum Subarray
*   Best Time to Buy & Sell Stock
*   Contains Duplicate
*   Product of Array Except Self

📌 Practice:

*   LeetCode Easy → Medium
*   Focus on **logic, not memorization**

***

## ✅ PHASE 3: Strings (1–2 Weeks)

Topics:

*   String traversal
*   Two pointers
*   Pattern matching
*   Anagram & palindrome logic

Key Problems:

*   Valid Palindrome
*   Longest Common Prefix
*   Longest Substring Without Repeating Characters
*   Check Anagram

✅ Skill gained:

*   Two pointers
*   Sliding window mastery

***

## ✅ PHASE 4: Linked List (1–2 Weeks)

Topics:

*   Singly linked list
*   Fast & slow pointer
*   Reversal technique

Key Problems:

*   Reverse Linked List
*   Detect Cycle
*   Merge Two Sorted Lists
*   Middle of Linked List
*   Remove Nth Node From End

📌 Interview favorite ✅

***

## ✅ PHASE 5: Stack & Queue (1–2 Weeks)

Topics:

*   Stack using list
*   Queue (collections.deque)
*   Monotonic stack

Key Problems:

*   Valid Parentheses
*   Daily Temperatures
*   Next Greater Element
*   Min Stack

✅ Stack = very important for interviews

***

## ✅ PHASE 6: Binary Search (1 Week)

Topics:

*   Binary search on sorted array
*   Binary search on answer
*   Rotated arrays

Key Problems:

*   Binary Search
*   Find Minimum in Rotated Sorted Array
*   Search in Rotated Sorted Array
*   First & Last Occurrence

📌 Improves problem‑solving speed drastically

***

## ✅ PHASE 7: Trees (2–3 Weeks)

Topics:

*   Binary Tree
*   Binary Search Tree
*   DFS / BFS
*   Recursion on trees

Key Problems:

*   Max Depth of Binary Tree
*   Invert Binary Tree
*   Same Tree
*   Diameter of Binary Tree
*   Lowest Common Ancestor

📌 Trees are heavily tested in interviews

***

## ✅ PHASE 8: Recursion & Backtracking (1–2 Weeks)

Topics:

*   Recursion pattern
*   Backtracking
*   Decision trees

Key Problems:

*   Subsets
*   Permutations
*   Combination Sum
*   N‑Queens

✅ Develops deep logical thinking

***

## ✅ PHASE 9: Dynamic Programming (3–4 Weeks)

### 🔥 Hard but very important

Topics:

*   Recursion → Memoization
*   Tabulation
*   1D DP & 2D DP

Key Problems:

*   Climbing Stairs
*   House Robber
*   Coin Change
*   Longest Increasing Subsequence
*   Knapsack

📌 Companies love DP questions

***

## ✅ PHASE 10: Graphs (2–3 Weeks)

Topics:

*   Graph representation
*   DFS / BFS
*   Connected components
*   Topological sort

Key Problems:

*   Number of Islands
*   Clone Graph
*   Course Schedule
*   Word Ladder

📌 Crucial for Google, Amazon, Microsoft

***

## ✅ FINAL PHASE: MOCK INTERVIEW PREP

### 🎯 Goal: Convert knowledge into confidence

✅ Do:

*   Blind 75 / NeetCode 150
*   Timed practice
*   Explain solutions aloud
*   Revise patterns

✅ Platforms:

*   LeetCode
*   NeetCode
*   GeeksforGeeks

***

# 🗓️ Suggested Timeline

| Duration   | Level           |
| ---------- | --------------- |
| 0–2 Months | Beginner        |
| 3–4 Months | Intermediate    |
| 5–6 Months | Interview Ready |

***

## ✅ What I can help you next with

*   ✅ **Daily DSA study schedule**
*   ✅ **Blind 75 explained step‑by‑step**
*   ✅ **Company‑wise DSA questions**
*   ✅ **PDF roadmap + cheatsheets**
*   ✅ **Python‑only DSA course path**

Just tell me what you want next 👍


v 7-DAY CODING INTERVIEW CRASH PLAN – CHECKLIST
DAY 1 – ARRAYS & TWO POINTERS
n Two Sum II (LC #167)
n Valid Palindrome (LC #125)
n Remove Duplicates from Sorted Array (LC #26)
n Container With Most Water (LC #11)
DAY 2 – SLIDING WINDOW
n Longest Substring Without Repeating Characters (LC #3)
n Maximum Average Subarray (LC #643)
n Permutation in String (LC #567)
n Longest Repeating Character Replacement (LC #424)
DAY 3 – STACK & STRINGS
n Valid Parentheses (LC #20)
n Daily Temperatures (LC #739)
n Next Greater Element (LC #496)
n Decode String (LC #394)
DAY 4 – RECURSION
n Fibonacci (LC #509)
n Merge Two Sorted Lists (LC #21)
n Reverse Linked List (Recursion)
n Maximum Depth of Binary Tree (LC #104)

DAY 5 – BACKTRACKING
n Subsets (LC #78)
n Permutations (LC #46)
n Combination Sum (LC #39)
n Generate Parentheses (LC #22)
DAY 6 – TREES (BFS / DFS)
n Binary Tree Level Order Traversal (LC #102)
n Invert Binary Tree (LC #226)
n Same Tree (LC #100)
n Path Sum (LC #112)
DAY 7 – MOCK & REVISION
n Solve 5 random problems under time limit
n Explain approach & complexity out loud
n Review templates (Two Pointer, Sliding Window, Backtracking)
FINAL REMINDER:
4 Recognize pattern first
4 Communicate clearly
4 Handle edge cases
4 Stay calm & confident

hh DAILY DSA INTERVIEW REVISION SHEET
USE THIS SHEET EVERY DAY BEFORE PRACTICE OR INTERVIEW
1. TWO POINTER PATTERN
• Used when array/string is sorted or needs pair checking
• Keywords: sorted, pair sum, reverse, palindrome
• Template:
left, right = 0, n-1
2. SLIDING WINDOW
• Used for subarray / substring problems
• Fixed window ® size k
• Variable window ® condition based
• Keywords: longest, shortest, max, min
3. STACK
• Used for matching, previous/next greater element
• Keywords: parentheses, undo, price span
• LIFO structure
4. RECURSION
• Always identify base case
• Think: smaller problem
• Common for trees, linked lists
5. BACKTRACKING
• Used for all combinations/permutations
• Pattern:
Choose ® Explore ® Un-choose
6. TREES
• DFS ® Depth problems
• BFS ® Level order problems
INTERVIEW QUICK CHECK
n Understood problem clearly
n Explained approach first
n Wrote clean code
n Handled edge cases
n Explained time & space complexity
REMEMBER:
4 Pattern over Solution
4 Clarity over Speed
4 Confidence over Perfection
