# Theoretical Analysis of Matrix Multiplication Algorithms

## Summary

This project presents a theoretical comparison of three different algorithms for square matrix multiplication:

1. **Iterative Multiplication**
2. **Recursive Multiplication**
3. **Strassen's Algorithm**

Each algorithm is described in terms of its logic, structure, and computational complexity. While all three aim to compute the product of two square matrices $\left( A \times B = C \right)$, their strategies and efficiencies differ significantly.

Due to the high time cost of recursive and Strassen-based methods in practical Python implementations, this project focuses on **theoretical insight and algorithmic understanding**, rather than performance benchmarks.

## Objectives

- Describe and implement three core matrix multiplication strategies:
  - The classical triple-loop method.
  - The divide-and-conquer recursive approach.
  - Strassen's algorithm, which reduces the number of multiplications.
  
- Analyze the **computational complexity** of each method:
  
- Highlight theoretical advantages and limitations of each algorithm.
  
- Provide clean and pedagogical implementations of these algorithms.

## Conclusion

Although Strassen’s algorithm is theoretically faster than the classical and recursive approaches, **practical performance** may not reflect this due to:

- The **overhead of recursive calls and matrix splitting**, especially in interpreted languages like Python.
- **Memory consumption** and deep recursion for large matrices.

In actual testing with matrices of size $\left( 2^{10} \times 2^{10} \right)$, the naive element-wise multiplication **performed faster** than Strassen’s method by a large margin.

Hence, this project concludes that:

- The **classical method is best for general use** in Python unless highly optimized libraries are used.
- The **recursive and Strassen methods** are better suited for theoretical study, teaching, or implementation in low-level languages with tight memory and speed control.
- Understanding these algorithms builds foundational knowledge in algorithm design, divide-and-conquer techniques, and computational complexity.

## **Project Structure**

The repository is organized into the following components:

- **Individual Algorithm Folders**:  
  Each matrix multiplication algorithm is placed in its own folder. Every folder contains the implementation, tests and a detailed explanation in its corresponding `README.md`.

## **How to Run This Project**

1. **Clone the repository**  
   Open a terminal and run:

   ```bash
   git clone https://github.com/ByronVelasco/MatrixMultiplication.git
   cd MatrixMultiplication

2. **Install the required libraries**
   
   Make sure you have Python installed (preferably 3.8+), then install the dependencies:
   
   ```bash
   pip install -r requirements.txt

3. **Open each notebook for details**
   
   Use your preferred Python environment (like Jupyter, VS Code, or Google Colab) and open:

   ```
   1 MatrixProduct/MatrixProduct.ipynb
   2 RecursiveProduct/RecursiveProduct.ipynb
   3 Strassen/Strassen.ipynb

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

© 2025 Byron Velasco