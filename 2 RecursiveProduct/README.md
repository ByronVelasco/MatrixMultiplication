# **Recursive Matrix Multiplication**

Recursive matrix multiplication is a **divide and conquer algorithm** that multiplies two square matrices by **recursively breaking them into smaller submatrices**.

Instead of computing the result in a single loop over all entries, the recursive approach:

1. **Divides** each matrix into four equal-sized submatrices (quadrants).
2. Computes the resulting submatrices of the product matrix using the rule: 

    $C_{ij} = \sum_{k=1}^{2} A_{ik} \cdot B_{kj}$  

   where each multiplication $A_{ik} \cdot B_{kj}$ is itself a **recursive call** on smaller matrices.
3. **Combines** the four resulting submatrices to build the final product matrix.

This process continues until the matrices are of size 1×1, where scalar multiplication is performed directly (base case).

## **Function:** `RecursiveProduct(A, B, C, n)`

Multiplies matrices $A$ and $B$ of size n x n and stores the result in the matrix $C$.

**Example:**
```python
A = [[2, 6, -2],
     [0, 4, -5],
     [-1, -9, 6]]

B = [[8, 10, 9],
     [-2, 3, 8],
     [0, 9, -7]]

C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
RecursiveProduct(A, B, C, 3)
print(C)
# Output: [[4, 20, 80],
#          [-8, -33, 67],
#          [10, 17, -123]]
```

## **Time Complexity**

- **Big-Oh:** $O(n^3)$

---

© 2025 Byron Velasco
