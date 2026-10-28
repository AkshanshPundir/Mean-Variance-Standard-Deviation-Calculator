# Mean-Variance-Standard Deviation Calculator

A Python-based data analysis tool developed as part of the freeCodeCamp *Data Analysis with Python* certification. This program uses **NumPy** to process a list of 9 numbers, reshape it into a $3 \times 3$ matrix, and compute key statistical metrics across multiple axes.

---

## Key Features

* **Statistical Computations:** Calculates the mean, variance, standard deviation, maximum, minimum, and sum.
* **Multi-Axis Analysis:** Evaluates metrics across columns (`axis=0`), rows (`axis=1`), and the flattened matrix.
* **Input Validation:** Automatically checks inputs and raises a `ValueError` with the message *"List must contain nine numbers."* if fewer than 9 elements are provided.
* **Testing Suite:** Fully validated using Python's `unittest` framework to ensure complete accuracy.

---

## Tech Stack

* **Language:** Python
* **Library:** NumPy
* **Testing:** Unittest

---

## Project Structure

* `mean_var_std.py`: Contains the core `calculate()` function logic using NumPy.
* `main.py`: Entry point script used for testing the function locally.
* `test_module.py`: Official unit test module verifying function output and error handling.
