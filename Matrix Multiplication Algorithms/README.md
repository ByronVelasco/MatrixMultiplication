# **Matrix Product**

The entry of the resulting matrix `C` at row `i` and column `j`, denoted as $c_{ij}$, is computed using the following summation:  
$$
c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
$$
This means:
- Fix a row `i` from matrix `A`
- Fix a column `j` from matrix `B`
- Multiply each corresponding element $a_{ik}$ (from row `i` of `A`) with $b_{kj}$ (from column `j` of `B`)
- Sum all these products to get the value $c_{ij}$

## **Function: `matrix_product(A, B, C, n)`**

Multiplies two square matrices `A` and `B` of size `n x n`, storing the resulting matrix product in `C`.

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
matrix_product(A, B, C, 3)
print(C)
# Output: [[4, 20, 80],
#          [-8, -33, 67],
#          [10, 17, -123]]
```

## **Time Complexity**

- **Big-Oh:** $O(n^3)$

# **Recursive Matrix Multiplication**

Recursive matrix multiplication is a **divide and conquer algorithm** that multiplies two square matrices by **recursively breaking them into smaller submatrices**.

Instead of computing the result in a single loop over all entries, the recursive approach:

1. **Divides** each matrix into four equal-sized submatrices (quadrants).
2. Computes the resulting submatrices of the product matrix using the rule: 

    $C_{ij} = \sum_{k=1}^{2} A_{ik} \cdot B_{kj}$  

   where each multiplication $A_{ik} \cdot B_{kj}$ is itself a **recursive call** on smaller matrices.
3. **Combines** the four resulting submatrices to build the final product matrix.

This process continues until the matrices are of size 1×1, where scalar multiplication is performed directly (base case).

## **Function:** `recursive_matrix_product(A, B, C, n)`

Multiplies two square matrices `A` and `B` of size `n x n`, storing the resulting matrix product in `C`.

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
recursive_matrix_product(A, B, C, 3)
print(C)
# Output: [[4, 20, 80],
#          [-8, -33, 67],
#          [10, 17, -123]]
```

## **Time Complexity**

- **Big-Oh:** $O(n^3)$

# **Strassen's Method**

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

## **Function:** `strassen(A, B, C, n)`

Multiplies two square matrices `A` and `B` of size `n x n`, storing the resulting matrix product in `C`.

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