<h2><a href="https://leetcode.com/problems/check-if-array-is-sorted-and-rotated">1752. Check if Array Is Sorted and Rotated</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code>, return <code>true</code><em> if the array was originally sorted in non-decreasing order, then rotated <strong>some</strong> number of positions (including zero)</em>. Otherwise, return <code>false</code>.</p>

<p>There may be <strong>duplicates</strong> in the original array.</p>

<p><strong>Note:</strong> An array <code>A</code> rotated by <code>x</code> positions results in an array <code>B</code> of the same length such that <code>B[i] == A[(i+x) % A.length]</code> for every valid index <code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no sorted array once rotated that can make nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

---

# Brute Force

### Problem Explanation
The basic idea is to try all possible rotation values $x$ (from $0$ to $n-1$). For each rotation, we construct the rotated version of the array and check if it is sorted in non-decreasing order. If we find any rotation that results in a sorted array, we return `True`. If we try all rotations and none are sorted, we return `False`.

### Algorithm
1. Get the length of the array $n$.
2. For each rotation count $x$ from $0$ to $n-1$:
   - Construct a new array representing the rotated state: `rotated = nums[x:] + nums[:x]`.
   - Check if this `rotated` array is sorted (i.e., `rotated[i] <= rotated[i+1]` for all valid $i$).
   - If it is sorted, return `True`.
3. If no rotation results in a sorted array, return `False`.

### Dry Run
Let's dry run with `nums = [3,4,5,1,2]`, $n = 5$:
- **$x = 0$**: `rotated = [3,4,5,1,2]`. Check if sorted: `5 > 1` (Not sorted).
- **$x = 1$**: `rotated = [4,5,1,2,3]`. Check if sorted: `5 > 1` (Not sorted).
- **$x = 2$**: `rotated = [5,1,2,3,4]`. Check if sorted: `5 > 1` (Not sorted).
- **$x = 3$**: `rotated = [1,2,3,4,5]`. Check if sorted: `1 <= 2 <= 3 <= 4 <= 5` (Sorted!). Return `True`.

Visual rotation splitting and rejoining:
```diff
Original: [3, 4, 5, 1, 2]
For x = 3:
- Left part (to rotate):  [3, 4, 5]
+ Right part (to front):  [1, 2]
Combined (Rotated):       [1, 2, 3, 4, 5]
```

### Complexity Analysis
> [!WARNING]
> - **Time Complexity:** $\color{#d9534f}{O(n^2)}$ because we try $n$ different rotations, and for each rotation we check if the array of size $n$ is sorted.
> - **Space Complexity:** $\color{#f0ad4e}{O(n)}$ to store the rotated array copy.

### Code Implementation
```python
class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        for x in range(n):
            rotated = nums[x:] + nums[:x]
            is_sorted = True
            for i in range(n - 1):
                if rotated[i] > rotated[i+1]:
                    is_sorted = False
                    break
            if is_sorted:
                return True
        return False
```

---

# Optimal Solution

### Problem Explanation
An array is sorted and rotated if, when we traverse it, there is at most one point where the array "drops" (i.e., the current element is strictly greater than the next element). 
- If the array is sorted and NOT rotated, there are no drops, except when wrapping around from the last element to the first element (which might or might not be a drop).
- If the array is sorted and rotated, there will be exactly one drop (where the original end of the array meets the original start of the array).
- If the count of such drop points is $\le 1$, then the array is a sorted and rotated array. Otherwise, it is not.

### Algorithm
1. Initialize a counter `count = 0`.
2. Iterate through the array from $0$ to $n-1$:
   - Check if `nums[i] > nums[(i + 1) % n]`. Note that `% n` handles the wrap-around from the last element back to the first.
   - If yes, increment `count`.
3. Return `count <= 1`.

> [!IMPORTANT]
> The wrap-around check comparing `nums[i]` and `nums[(i + 1) % n]` ensures that we check if the array transitions correctly from the last element back to the first.

### Dry Run
Let's dry run with `nums = [3,4,5,1,2]`, $n = 5$:
- **$i = 0$**: Compare `nums[0]` ($3$) and `nums[1]` ($4$). $3 > 4$ is False.
- **$i = 1$**: Compare `nums[1]` ($4$) and `nums[2]` ($5$). $4 > 5$ is False.
- **$i = 2$**: Compare `nums[2]` ($5$) and `nums[3]` ($1$). $5 > 1$ is True $\rightarrow$ `count` becomes $1$.
- **$i = 3$**: Compare `nums[3]` ($1$) and `nums[4]` ($2$). $1 > 2$ is False.
- **$i = 4$**: Compare `nums[4]` ($2$) and `nums[0]` ($3$). $2 > 3$ is False (wrap-around check).
- **Result:** `count` is $1$, which is $\le 1$. Return `True`.

### Complexity Analysis
> [!TIP]
> - **Time Complexity:** $\color{#5cb85c}{O(n)}$ as we loop through the array exactly once.
> - **Space Complexity:** $\color{#5cb85c}{O(1)}$ since we only use a single counter variable.

### Code Implementation
```python
class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
        return count <= 1
```
