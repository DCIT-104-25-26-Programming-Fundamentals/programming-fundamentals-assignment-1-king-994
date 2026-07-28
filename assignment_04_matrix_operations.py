# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(name):
    """Read an M x N matrix from the user, row by row."""
    print(f"\n--- Enter Matrix {name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = [int(val) for val in row_values]
        matrix.append(row)

    return matrix


def print_matrix(matrix, title="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        print("  ".join(f"{val:>4}" for val in row))


def transpose(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    """Return the matrix product A x B."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":
    # ---------------- PART A: Transpose ----------------
    print("=== PART A: Transpose a Matrix ===")
    matrix_a = read_matrix("A")
    print_matrix(matrix_a, "Original Matrix A")
    transposed = transpose(matrix_a)
    print_matrix(transposed, "Transposed Matrix")

    # ---------------- PART B: Addition ----------------
    print("\n=== PART B: Add Two Matrices ===")
    print("(Both matrices must be the same size.)")
    matrix_b1 = read_matrix("B1")
    matrix_b2 = read_matrix("B2")

    if len(matrix_b1) != len(matrix_b2) or len(matrix_b1[0]) != len(matrix_b2[0]):
        print("Error: Matrices must be the same size to add.")
    else:
        sum_result = add_matrices(matrix_b1, matrix_b2)
        print_matrix(matrix_b1, "Matrix B1")
        print_matrix(matrix_b2, "Matrix B2")
        print_matrix(sum_result, "Sum (B1 + B2)")

    # ---------------- PART C: Multiplication ----------------
    print("\n=== PART C: Multiply Two Matrices ===")
    print("(Columns of A must equal rows of B.)")
    matrix_c1 = read_matrix("C1")
    matrix_c2 = read_matrix("C2")

    if len(matrix_c1[0]) != len(matrix_c2):
        print("Error: Number of columns in first matrix must equal "
              "number of rows in second matrix.")
    else:
        product = multiply_matrices(matrix_c1, matrix_c2)
        print_matrix(matrix_c1, "Matrix C1")
        print_matrix(matrix_c2, "Matrix C2")
        print_matrix(product, "Product (C1 x C2)")