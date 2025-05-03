# **MatrixProduct**

The entry of the resulting matrix `C` at row `i` and column `j`, denoted as $c_{ij}$, is computed using the following summation:  

$ c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj} $
     
This means:
- Fix a row `i` from matrix `A`
- Fix a column `j` from matrix `B`
- Multiply each corresponding element $a_{ik}$ (from row `i` of `A`) with $b_{kj}$ (from column `j` of `B`)
- Sum all these products to get the value $c_{ij}$

## **Function:** `MatrixProduct(A, B, C, n)`

Multiplies matrices `A` and `B` of dimensions `n x n` and stores the result in `C`.

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
MatrixProduct(A, B, C, 3)
print(C)
# Output: [[4, 20, 80],
#          [-8, -33, 67],
#          [10, 17, -123]]
```

## **Time Complexity**

- **Big-Oh:** $O(n^3)$

---

© 2025 Byron Velasco