<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter Notebook" />
  <img src="https://img.shields.io/badge/Status-Learning_%26_Building-success?style=for-the-badge" alt="Status" />

  <h1>🚀 Python Data Structures & Algorithms</h1>
  
  <p><i>A comprehensive and interactive collection of Python scripts and Jupyter Notebooks for mastering DSA, core Python concepts, and building practical mini-projects.</i></p>
</div>

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
  - [Core Python Concepts](#-core-python-concepts)
  - [Math & Logic](#-math--logic)
  - [Data Structures](#-data-structures)
  - [Algorithms](#-algorithms)
  - [Mini Projects](#-mini-projects)
  - [LeetCode Problem Solutions](#-leetcode-problem-solutions)
  - [File Handling](#-file-handling)
- [How to Use](#-how-to-use)
- [Contributing](#-contributing)
- [LeetCode Topics](#leetcode-topics)

---

## 📖 Overview

Welcome to my **DSA Python** learning repository! This project serves as a personal knowledge base and practical playground for mastering **Data Structures**, **Algorithms**, and essential Python programming techniques. It includes various Jupyter Notebooks covering everything from basic algorithms to practical, real-world mini-projects.

---

## 📂 Repository Structure

### 🧠 Core Python Concepts (`01_Python_Concepts`)
| Concept | File | Description |
| :--- | :--- | :--- |
| **Functions** | [`function.ipynb`](./01_Python_Concepts/function.ipynb) | Deep dive into Python functions and parameter passing. |
| **Function Examples** | [`all_in_one.ipynb`](./01_Python_Concepts/function_examples/all_in_one.ipynb) | Comprehensive collection of function examples. |
| **Lambda Functions** | [`lambda.ipynb`](./01_Python_Concepts/lambda.ipynb) | Anonymous functions and shorthand operations. |
| **Map Function** | [`map.ipynb`](./01_Python_Concepts/map.ipynb) | Transforming iterables using `map()`. |
| **Filter Function** | [`filter.ipynb`](./01_Python_Concepts/filter.ipynb) | Filtering elements from iterables using `filter()`. |
| **Modules & Imports** | [`modules.ipynb`](./01_Python_Concepts/modules.ipynb) | Understanding Python modules and standard libraries. |
| **Recursion Basics** | [`recursion.ipynb`](./01_Python_Concepts/recursion.ipynb) | Fundamentals of recursive functions in Python. |

### 🧮 Math & Logic (`02_Math_and_Logic`)
| Topic | File | Description |
| :--- | :--- | :--- |
| **Armstrong Number** | [`armstrong.ipynb`](./02_Math_and_Logic/armstrong.ipynb) | Check if a number is an Armstrong number. |
| **Common Numbers** | [`common_num.ipynb`](./02_Math_and_Logic/common_num.ipynb) | Finding common numbers between collections. |
| **Digit Count** | [`count.ipynb`](./02_Math_and_Logic/count.ipynb) | Counting digits in a given number. |
| **Factorial** | [`facto_of_number.ipynb`](./02_Math_and_Logic/facto_of_number.ipynb) | Computing factorial recursively and iteratively. |
| **Find Factors** | [`factors.ipynb`](./02_Math_and_Logic/factors.ipynb) | Finding all factors / divisors of a number. |
| **Fibonacci Series** | [`fib.ipynb`](./02_Math_and_Logic/fib.ipynb) | Generating Fibonacci series terms. |
| **Palindrome Number** | [`palindrome.ipynb`](./02_Math_and_Logic/palindrome.ipynb) | Checking numerical and string palindromes. |
| **Palindrome Logic** | [`palin.ipynb`](./02_Math_and_Logic/palin.ipynb) | Alternative palindrome checking techniques. |
| **Reverse Number** | [`reverse.ipynb`](./02_Math_and_Logic/reverse.ipynb) | Reversing digits of an integer. |
| **Sum of N Numbers** | [`sum_of_n.ipynb`](./02_Math_and_Logic/sum_of_n.ipynb) | Calculating sum of first N natural numbers. |

### 🏗 Data Structures (`03_Data_Structures`)
#### 📊 Arrays & Hashing
| Concept | File | Description |
| :--- | :--- | :--- |
| **Array Basics** | [`array.ipynb`](./03_Data_Structures/array.ipynb) | Array creation, indexing, and basic operations. |
| **Reverse Array** | [`reverseArray.ipynb`](./03_Data_Structures/reverseArray.ipynb) | Reversing an array in-place and out-of-place. |
| **Frequency Map** | [`freq_map.ipynb`](./03_Data_Structures/freq_map.ipynb) | Counting element frequencies using Hash Maps / Dicts. |
| **Largest Element** | [`largest_element.ipynb`](./03_Data_Structures/Arrays/largest_element.ipynb) | Finding maximum element in an array. |
| **Second Largest** | [`second_largest.ipynb`](./03_Data_Structures/Arrays/second_largest.ipynb) | Finding second largest element efficiently. |

#### 🔲 Matrix Operations
| Concept | File | Description |
| :--- | :--- | :--- |
| **Matrix Demo** | [`demo.ipynb`](./03_Data_Structures/Matrix/demo.ipynb) | Introduction to 2D matrices in Python. |
| **Transpose Matrix** | [`transpose.ipynb`](./03_Data_Structures/Matrix/transpose.ipynb) | Transposing a 2D grid matrix. |
| **Set Matrix Zeroes** | [`Set Matrix Zeros.ipynb`](./03_Data_Structures/Matrix/Set%20Matrix%20Zeros.ipynb) | Setting rows and columns to zero if element is 0. |
| **Upper Triangle** | [`print_upper_triangle.ipynb`](./03_Data_Structures/Matrix/print_upper_triangle.ipynb) | Extracting upper triangular matrix elements. |

### 🔍 Algorithms (`04_Algorithms`)
#### 🔎 Searching Algorithms
| Algorithm | File | Description | Complexity |
| :--- | :--- | :--- | :--- |
| **Linear Search** | [`linear.ipynb`](./04_Algorithms/Searching/linear.ipynb) | Sequential search through array. | `O(N)` |
| **Binary Search** | [`binSearch.ipynb`](./04_Algorithms/Searching/binSearch.ipynb) | Search in sorted array via divide-and-conquer. | `O(log N)` |

#### 🔄 Sorting Algorithms
| Algorithm | File | Description | Complexity |
| :--- | :--- | :--- | :--- |
| **Bubble Sort** | [`bubblesort.ipynb`](./04_Algorithms/Sorting/bubblesort.ipynb) | Repeatedly swap adjacent elements. | `O(N²)` |
| **Selection Sort** | [`selectionSort.ipynb`](./04_Algorithms/Sorting/selectionSort.ipynb) | Repeatedly select minimum element. | `O(N²)` |
| **Insertion Sort** | [`insertionSort.ipynb`](./04_Algorithms/Sorting/insertionSort.ipynb) | Build sorted array one item at a time. | `O(N²)` |
| **Merge Sort** | [`merge_sort.ipynb`](./04_Algorithms/Sorting/merge_sort.ipynb) | Divide and conquer sorting algorithm. | `O(N log N)` |

### 🛠 Mini Projects (`05_Mini_Projects`)
| Project | File | Description |
| :--- | :--- | :--- |
| **Inventory System** | [`inventory.ipynb`](./05_Mini_Projects/inventory.ipynb) | Simple inventory management application. |
| **Student Grades** | [`organizning_student_grades.ipynb`](./05_Mini_Projects/organizning_student_grades.ipynb) | Calculate and rank student performance. |
| **To-Do List** | [`to_do_list.ipynb`](./05_Mini_Projects/to_do_list.ipynb) | Interactive task manager application. |
| **User Feedback** | [`userfeedback.ipynb`](./05_Mini_Projects/userfeedback.ipynb) | Process and analyze user feedback data. |

### 🧩 LeetCode Problem Solutions (`06_Leetcode`)
| # | Problem Name | Difficulty | Problem Folder | Python Solution | Jupyter Notebook |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0001** | Two Sum | 🟢 Easy | [`0001-two-sum`](./06_Leetcode/0001-two-sum) | [0001-two-sum.py](./06_Leetcode/0001-two-sum/0001-two-sum.py) | [`2sum.ipynb`](./06_Leetcode/0001-two-sum/2sum.ipynb) |
| **0007** | Reverse Integer | 🟡 Medium | [`0007-reverse-integer`](./06_Leetcode/0007-reverse-integer) | [0007-reverse-integer.py](./06_Leetcode/0007-reverse-integer/0007-reverse-integer.py) | - |
| **0009** | Palindrome Number | 🟢 Easy | [`0009-palindrome-number`](./06_Leetcode/0009-palindrome-number) | [0009-palindrome-number.py](./06_Leetcode/0009-palindrome-number/0009-palindrome-number.py) | - |
| **0026** | Remove Duplicates from Sorted Array | 🟢 Easy | [`0026-remove-duplicates...`](./06_Leetcode/0026-remove-duplicates-from-sorted-array) | [0026-remove-duplicates...py](./06_Leetcode/0026-remove-duplicates-from-sorted-array/0026-remove-duplicates-from-sorted-array.py) | [`remove_dup.ipynb`](./06_Leetcode/0026-remove-duplicates-from-sorted-array/remove_dup.ipynb) |
| **0053** | Maximum Subarray | 🟡 Medium | [`0053-maximum-subarray`](./06_Leetcode/0053-maximum-subarray) | [0053-maximum-subarray.py](./06_Leetcode/0053-maximum-subarray/0053-maximum-subarray.py) | [`maxi_subaaray_sum.ipynb`](./06_Leetcode/0053-maximum-subarray/maxi_subaaray_sum.ipynb) |
| **0073** | Set Matrix Zeroes | 🟡 Medium | [`0073-set-matrix-zeroes`](./06_Leetcode/0073-set-matrix-zeroes) | [0073-set-matrix-zeroes.py](./06_Leetcode/0073-set-matrix-zeroes/0073-set-matrix-zeroes.py) | - |
| **0121** | Best Time to Buy and Sell Stock | 🟢 Easy | [`0121-best-time...`](./06_Leetcode/0121-best-time-to-buy-and-sell-stock) | [0121-best-time...py](./06_Leetcode/0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | [`stock buy & sell.ipynb`](./06_Leetcode/0121-best-time-to-buy-and-sell-stock/stock%20buy%20%26%20sell.ipynb) |
| **0128** | Longest Consecutive Sequence | 🟡 Medium | [`0128-longest-consecutive...`](./06_Leetcode/0128-longest-consecutive-sequence) | [0128-longest-consecutive...py](./06_Leetcode/0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | [`longest_sqanc.ipynb`](./06_Leetcode/0128-longest-consecutive-sequence/longest_sqanc.ipynb) |
| **0189** | Rotate Array | 🟡 Medium | [`0189-rotate-array`](./06_Leetcode/0189-rotate-array) | [0189-rotate-array.py](./06_Leetcode/0189-rotate-array/0189-rotate-array.py) | [`rotate_array_by_k_places.ipynb`](./06_Leetcode/0189-rotate-array/rotate_array_by_k_places.ipynb) |
| **0268** | Missing Number | 🟢 Easy | [`0268-missing-number`](./06_Leetcode/0268-missing-number) | [0268-missing-number.py](./06_Leetcode/0268-missing-number/0268-missing-number.py) | [`find_missing_number.ipynb`](./06_Leetcode/0268-missing-number/find_missing_number.ipynb) |
| **0283** | Move Zeroes | 🟢 Easy | [`0283-move-zeroes`](./06_Leetcode/0283-move-zeroes) | [0283-move-zeroes.py](./06_Leetcode/0283-move-zeroes/0283-move-zeroes.py) | [`move_zeroes_end.ipynb`](./06_Leetcode/0283-move-zeroes/move_zeroes_end.ipynb) |
| **0485** | Max Consecutive Ones | 🟢 Easy | [`0485-max-consecutive-ones`](./06_Leetcode/0485-max-consecutive-ones) | [0485-max-consecutive-ones.py](./06_Leetcode/0485-max-consecutive-ones/0485-max-consecutive-ones.py) | [`Max_Consecutive.ipynb`](./06_Leetcode/0485-max-consecutive-ones/Max_Consecutive.ipynb) |
| **0509** | Fibonacci Number | 🟢 Easy | [`0509-fibonacci-number`](./06_Leetcode/0509-fibonacci-number) | [0509-fibonacci-number.py](./06_Leetcode/0509-fibonacci-number/0509-fibonacci-number.py) | - |
| **0704** | Binary Search | 🟢 Easy | [`0704-binary-search`](./06_Leetcode/0704-binary-search) | [0704-binary-search.py](./06_Leetcode/0704-binary-search/0704-binary-search.py) | - |
| **1752** | Check if Array Is Sorted and Rotated | 🟢 Easy | [`1752-check-if-array...`](./06_Leetcode/1752-check-if-array-is-sorted-and-rotated) | [1752-check-if-array...py](./06_Leetcode/1752-check-if-array-is-sorted-and-rotated/1752-check-if-array-is-sorted-and-rotated.py) | [`check_array_is-sort.ipynb`](./06_Leetcode/1752-check-if-array-is-sorted-and-rotated/check_array_is-sort.ipynb) |
| **2149** | Rearrange Array Elements by Sign | 🟡 Medium | [`2149-rearrange-array...`](./06_Leetcode/2149-rearrange-array-elements-by-sign) | [2149-rearrange-array...py](./06_Leetcode/2149-rearrange-array-elements-by-sign/2149-rearrange-array-elements-by-sign.py) | [`Rearrange Array...ipynb`](./06_Leetcode/2149-rearrange-array-elements-by-sign/Rearrange%20Array%20Elements%20by%20Sign.ipynb) |

### 📁 File Handling (`07_File_Handling`)
| File | Type | Description |
| :--- | :--- | :--- |
| [`source.txt`](./07_File_Handling/source.txt) | Plain Text | Source input text file. |
| [`destination.txt`](./07_File_Handling/destination.txt) | Plain Text | Output text file destination. |
| [`example.csv`](./07_File_Handling/example.csv) | CSV Data | Sample CSV dataset file. |

---

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vaidik-Pipaliya/DSA_python.git
   ```

2. **Navigate to the directory:**
   ```bash
   cd DSA_python
   ```

3. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

4. **Explore the files!** Open any `.ipynb` file to run the cells, learn from the code, and experiment on your own.

---

## 💡 Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the implementations! Learning is better together. ✨

> [!NOTE]  
> 🚧 **More content is coming soon!** I'm continually learning and adding new algorithms, data structures, and mini-projects to this repository. Stay tuned!

---

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0001-two-sum](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0001-two-sum/) | Easy |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0026-remove-duplicates-from-sorted-array/) | Easy |
| [0048-rotate-image](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/0048-rotate-image/) | Medium |
| [0053-maximum-subarray](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0053-maximum-subarray/) | Medium |
| [0073-set-matrix-zeroes](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0073-set-matrix-zeroes/) | Medium |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0121-best-time-to-buy-and-sell-stock/) | Easy |
| [0128-longest-consecutive-sequence](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0128-longest-consecutive-sequence/) | Medium |
| [0189-rotate-array](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0189-rotate-array/) | Medium |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0268-missing-number/) | Easy |
| [0283-move-zeroes](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0283-move-zeroes/) | Easy |
| [0485-max-consecutive-ones](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0485-max-consecutive-ones/) | Easy |
| [0704-binary-search](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0704-binary-search/) | Easy |
| [1752-check-if-array-is-sorted-and-rotated](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/1752-check-if-array-is-sorted-and-rotated/) | Easy |
| [2149-rearrange-array-elements-by-sign](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/2149-rearrange-array-elements-by-sign/) | Medium |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [0048-rotate-image](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/0048-rotate-image/) | Medium |
| [0073-set-matrix-zeroes](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0073-set-matrix-zeroes/) | Medium |
## Binary Search
| Problem Name | Difficulty |
| ------- | ------- |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0268-missing-number/) | Easy |
| [0704-binary-search](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0704-binary-search/) | Easy |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [0001-two-sum](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0001-two-sum/) | Easy |
| [0073-set-matrix-zeroes](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0073-set-matrix-zeroes/) | Medium |
| [0128-longest-consecutive-sequence](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0128-longest-consecutive-sequence/) | Medium |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0268-missing-number/) | Easy |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [0007-reverse-integer](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0007-reverse-integer/) | Medium |
| [0009-palindrome-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0009-palindrome-number/) | Easy |
| [0048-rotate-image](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/0048-rotate-image/) | Medium |
| [0189-rotate-array](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0189-rotate-array/) | Medium |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0268-missing-number/) | Easy |
| [0509-fibonacci-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0509-fibonacci-number/) | Easy |
## Dynamic Programming
| Problem Name | Difficulty |
| ------- | ------- |
| [0053-maximum-subarray](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0053-maximum-subarray/) | Medium |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0121-best-time-to-buy-and-sell-stock/) | Easy |
| [0509-fibonacci-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0509-fibonacci-number/) | Easy |
## Recursion
| Problem Name | Difficulty |
| ------- | ------- |
| [0509-fibonacci-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0509-fibonacci-number/) | Easy |
## Memoization
| Problem Name | Difficulty |
| ------- | ------- |
| [0509-fibonacci-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0509-fibonacci-number/) | Easy |
## Two Pointers
| Problem Name | Difficulty |
| ------- | ------- |
| [0026-remove-duplicates-from-sorted-array](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0026-remove-duplicates-from-sorted-array/) | Easy |
| [0189-rotate-array](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0189-rotate-array/) | Medium |
| [0283-move-zeroes](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0283-move-zeroes/) | Easy |
| [2149-rearrange-array-elements-by-sign](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/2149-rearrange-array-elements-by-sign/) | Medium |
## Bit Manipulation
| Problem Name | Difficulty |
| ------- | ------- |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/06_Leetcode/0268-missing-number/) | Easy |
## Sorting
| Problem Name | Difficulty |
| ------- | ------- |
| [0268-missing-number](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0268-missing-number/) | Easy |
## Divide and Conquer
| Problem Name | Difficulty |
| ------- | ------- |
| [0053-maximum-subarray](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0053-maximum-subarray/) | Medium |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [2149-rearrange-array-elements-by-sign](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/2149-rearrange-array-elements-by-sign/) | Medium |
## Union-Find
| Problem Name | Difficulty |
| ------- | ------- |
| [0128-longest-consecutive-sequence](https://github.com/Vaidik-Pipaliya/DSA_python/tree/main/06_Leetcode/0128-longest-consecutive-sequence/) | Medium |
<!---LeetCode Topics End-->

<br>

<div align="center">
  <i>Happy Coding! 💻</i>
</div>
