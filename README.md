# Moore-s-Voting-Algorithm.

The **Moore's Voting Algorithm** is an efficient algorithm for finding the majority element in an array, where the **majority element** is defined as an element that appears more than \( \lfloor n/2 \rfloor \) times in an array of size \( n \). The algorithm works in **linear time \( O(n) \)** and uses **constant space \( O(1) \)**, making it highly optimized for this problem.

---

### Problem Statement
Given an array \( arr \) of size \( n \), find the element that appears more than \( n/2 \) times (if such an element exists). If no such element exists, report that no majority element is present.

---

### Key Idea
The algorithm consists of two phases:
1. **Candidate Selection Phase:**
   - Use a counter and a candidate variable.
   - Traverse the array, and identify a potential majority candidate.
2. **Verification Phase:**
   - Verify if the identified candidate is indeed the majority element by counting its occurrences.

---

### Algorithm Steps

#### **1. Candidate Selection Phase**
- Initialize `count = 0` and `candidate = None`.
- Traverse the array:
  - If `count` is 0, set `candidate = arr[i]`.
  - If the current element is the same as `candidate`, increment `count`.
  - Otherwise, decrement `count`.

This phase relies on the observation that if an element is the majority, it will remain as the candidate after balancing out against other elements.

#### **2. Verification Phase**
- Count the occurrences of the candidate in the array.
- If the count exceeds \( \lfloor n/2 \rfloor \), return the candidate. Otherwise, return "No majority element."

---

### Implementation (Python)
```python
def majority_element(nums):
    # Phase 1: Candidate Selection
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Phase 2: Verification
    count = sum(1 for num in nums if num == candidate)
    if count > len(nums) // 2:
        return candidate
    return "No majority element"

# Example
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(arr))  # Output: 4
```

---

### Dry Run Example
For \( arr = [3, 3, 4, 2, 4, 4, 2, 4, 4] \):

#### Phase 1: Candidate Selection
| Index | Current Element | Candidate | Count |
|-------|-----------------|-----------|-------|
| 0     | 3               | 3         | 1     |
| 1     | 3               | 3         | 2     |
| 2     | 4               | 3         | 1     |
| 3     | 2               | 3         | 0     |
| 4     | 4               | 4         | 1     |
| 5     | 4               | 4         | 2     |
| 6     | 2               | 4         | 1     |
| 7     | 4               | 4         | 2     |
| 8     | 4               | 4         | 3     |

Candidate after Phase 1: \( 4 \).

#### Phase 2: Verification
- Count occurrences of 4: \( 5 \).
- Majority threshold: \( \lfloor n/2 \rfloor = 4 \).

Since \( 5 > 4 \), the majority element is \( 4 \).

---

### Complexity Analysis
1. **Time Complexity:**
   - Candidate Selection: \( O(n) \) (single traversal of the array).
   - Verification: \( O(n) \) (another traversal to count occurrences).
   - Total: \( O(n) \).

2. **Space Complexity:**
   - \( O(1) \) (only a few variables are used).

---

### Applications
1. **Finding Majority Elements in Voting Systems.**
2. **Analyzing Data Streams.**
3. **Determining Frequent Items in Large Datasets.**

---

### Limitations
1. The algorithm works only when there **is a majority element**. Without it, the verification phase is essential.
2. If the majority element is defined differently (e.g., appears more than \( n/3 \) times), Moore's algorithm doesn't apply directly.

Let me know if you'd like to explore variations or practice problems!
