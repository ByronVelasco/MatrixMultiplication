import numpy as np

def matrix_product(A, B, C, n):
	for i in range(n):  # Iterate over each row of A
		for j in range(n):  # Iterate over each column of B
			# Compute the dot product of the i-th row of A and the j-th column of B
			C[i, j] = np.dot(A[i], B[:, j])
			

def recursive_matrix_product(A, B, C, n):
	# Base case: if the matrix is 1x1, multiply the single elements
	if n == 1:
		C[0, 0] = A[0, 0] * B[0, 0]
		return

	mid = n // 2  # Find the midpoint to partition the matrices

	# Partition matrices A, B, and C into four quadrants each
	A11, A12 = A[:mid, :mid], A[:mid, mid:]
	A21, A22 = A[mid:, :mid], A[mid:, mid:]
	B11, B12 = B[:mid, :mid], B[:mid, mid:]
	B21, B22 = B[mid:, :mid], B[mid:, mid:]
	C11, C12 = C[:mid, :mid], C[:mid, mid:]
	C21, C22 = C[mid:, :mid], C[mid:, mid:]

	# Temporary matrices to store intermediate results for addition
	S1 = np.zeros((mid, mid), dtype=A.dtype)
	S2 = np.zeros((mid, mid), dtype=A.dtype)

	# Compute C11 = A11*B11 + A12*B21
	recursive_matrix_product(A11, B11, C11, mid)   # C11 += A11 * B11
	recursive_matrix_product(A12, B21, S1, mid)    # S1 = A12 * B21
	C11 += S1                           # Add S1 to C11

	# Compute C12 = A11*B12 + A12*B22
	recursive_matrix_product(A11, B12, C12, mid)   # C12 += A11 * B12
	recursive_matrix_product(A12, B22, S2, mid)    # S2 = A12 * B22
	C12 += S2                           # Add S2 to C12

	# Prepare S1 and S2 for reuse
	S1.fill(0)
	S2.fill(0)

	# Compute C21 = A21*B11 + A22*B21
	recursive_matrix_product(A21, B11, C21, mid)   # C21 += A21 * B11
	recursive_matrix_product(A22, B21, S1, mid)    # S1 = A22 * B21
	C21 += S1                           # Add S1 to C21

	# Compute C22 = A21*B12 + A22*B22
	recursive_matrix_product(A21, B12, C22, mid)   # C22 += A21 * B12
	recursive_matrix_product(A22, B22, S2, mid)    # S2 = A22 * B22
	C22 += S2                           # Add S2 to C22
	

def strassen(A, B, C, n):
	# Base case: use standard multiplication for 1x1 matrices
	if n == 1:
		C[0, 0] = A[0, 0] * B[0, 0]
		return

	mid = n // 2  # Find the midpoint to partition the matrices

	# Partition matrices A, B, and C into four quadrants each
	A11, A12 = A[:mid, :mid], A[:mid, mid:]
	A21, A22 = A[mid:, :mid], A[mid:, mid:]
	B11, B12 = B[:mid, :mid], B[:mid, mid:]
	B21, B22 = B[mid:, :mid], B[mid:, mid:]
	C11, C12 = C[:mid, :mid], C[:mid, mid:]
	C21, C22 = C[mid:, :mid], C[mid:, mid:]

	# Allocate temporary matrices for Strassen's 7 products
	M1 = np.zeros((mid, mid), dtype=A.dtype)
	M2 = np.zeros((mid, mid), dtype=A.dtype)
	M3 = np.zeros((mid, mid), dtype=A.dtype)
	M4 = np.zeros((mid, mid), dtype=A.dtype)
	M5 = np.zeros((mid, mid), dtype=A.dtype)
	M6 = np.zeros((mid, mid), dtype=A.dtype)
	M7 = np.zeros((mid, mid), dtype=A.dtype)

	# Compute the 7 products using Strassen's formulas
	strassen(A11 + A22, B11 + B22, M1, mid)      # M1 = (A11 + A22) * (B11 + B22)
	strassen(A21 + A22, B11, M2, mid)            # M2 = (A21 + A22) * B11
	strassen(A11, B12 - B22, M3, mid)            # M3 = A11 * (B12 - B22)
	strassen(A22, B21 - B11, M4, mid)            # M4 = A22 * (B21 - B11)
	strassen(A11 + A12, B22, M5, mid)            # M5 = (A11 + A12) * B22
	strassen(A21 - A11, B11 + B12, M6, mid)      # M6 = (A21 - A11) * (B11 + B12)
	strassen(A12 - A22, B21 + B22, M7, mid)      # M7 = (A12 - A22) * (B21 + B22)

	# Combine the results into C using Strassen's recombination formulas
	C11[:, :] = M1 + M4 - M5 + M7   # C11 = M1 + M4 - M5 + M7
	C12[:, :] = M3 + M5             # C12 = M3 + M5
	C21[:, :] = M2 + M4             # C21 = M2 + M4
	C22[:, :] = M1 - M2 + M3 + M6   # C22 = M1 - M2 + M3 + M6