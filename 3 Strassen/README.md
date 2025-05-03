# **Strassen's Method**

This module contains the file `Strassen.ipynb`, which implements the Strassen's method for matrix multiplication.

## **Explanation**

Strassen's algorithm is an optimized method for multiplying two square matrices. It reduces the number of recursive multiplications needed, making it faster than the standard divide-and-conquer approach for large matrices.

Strassen realized that it's possible to compute the result with only **7 multiplications** (instead of 8) and some additional additions and subtractions. He defines 7 intermediate matrices:

- $M_1 = (A_{11} + A_{22}) \times (B_{11} + B_{22})$
- $M_2 = (A_{21} + A_{22}) \times B_{11}$  
- $M_3 = A_{11} \times (B_{12} - B_{22})$  
- $M_4 = A_{22} \times (B_{21} - B_{11})$  
- $M_5 = (A_{11} + A_{12}) \times B_{22}$  
- $M_6 = (A_{21} - A_{11}) \times (B_{11} + B_{12})$  
- $M_7 = (A_{12} - A_{22}) \times (B_{21} + B_{22})$

Then the submatrices of the result `C` are computed as:

- $C_{11} = M_1 + M_4 − M_5 + M_7$  
- $C_{12} = M_3 + M_5$  
- $C_{21} = M_2 + M_4$  
- $C_{22} = M_1 + M_3 − M_2 + M_6$

## **Function:** `add_matrix(A, B)`

Addition of matrices A and B.

## **Function:** `sub_matrix(A, B)`

Substraction of matrices A and B.

## **Function:** `split_matrix(M)`

Splits matrix M into 4 equal-sized submatrices.

## **Function:** `join_quadrants(C11, C12, C21, C22, C)`

Joins submatrices $C_{11}, C_{12}, C_{21}, C{22}$ into the matrix $C$.

## **Function:** `Strassen(A, B, C, n)`

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

- **Big-Oh:** $O(n^{\lg 7}) = O(n^{2.81})$

where $\lg 7$ means $\log_2 7$

---

© 2025 Byron Velasco
