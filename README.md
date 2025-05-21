# Theoretical Analysis of Matrix Multiplication Algorithms

## Summary

This project presents a theoretical comparison of three different algorithms for square matrix multiplication:

1. **Iterative Matrix Multiplication**
2. **Recursive Matrix Multiplication**
3. **Strassen's Method**

Each algorithm is described in terms of its logic, structure, and computational complexity. While all three aim to compute the product of two square matrices $\left( A \times B = C \right)$, their strategies and efficiencies differ significantly.

## Objectives

- Describe and implement three core matrix multiplication strategies:
  - The classical method.
  - The divide-and-conquer recursive approach.
  - Strassen's method, which reduces the number of multiplications.
  
- Analyze the **computational complexity** of each method:
  
- Highlight theoretical advantages and limitations of each algorithm.
  
- Provide clean and pedagogical implementations of these algorithms.

## Conclusion

In this notebook, we explored and implemented three matrix multiplication algorithms: the standard iterative method, the recursive approach, and Strassen's algorithm. Through both correctness validation and experimental performance analysis, we observed that all three methods produce accurate results for square matrices of various sizes.

The performance comparison revealed that the standard iterative method (`matrix_product`) consistently outperforms the recursive and Strassen's algorithms for the tested matrix sizes (up to 128×128). Although Strassen's algorithm is theoretically more efficient for very large matrices, its practical advantages are not apparent at these scales due to overhead from recursion and additional matrix operations. To observe the theoretical benefits of Strassen's method, experiments with significantly larger matrices would be required.

Overall, for small to moderately sized matrices, the standard iterative approach remains the most practical and efficient choice. Strassen's algorithm may become advantageous only for much larger matrices, where its reduced asymptotic complexity can outweigh its overhead.

## **Project Structure**

The repository is organized into the following components:

- `Matrix Multiplication Algorithms` Folder:

  This folder contains the implementation of algorithms `matrix_product`, `recursive_matrix_product` and `strassen` and their performance comparison with each other. It includes an experiment measuring and analyzing their execution times.

- `img` Folder:

  Stores the output images generated during experimentation.

- `project_functions.py` Python Script:

  This Python script includes all the algorithms developed specifically for this project.

- `requirements.txt` Text File:

  This file lists all the dependencies required to run the project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

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

---

© 2025 Byron Velasco