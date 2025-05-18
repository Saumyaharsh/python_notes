import numpy as np

# 1. Degree of the B-spline
p = 3

# 2. Knot vector (length = number of control points + degree + 1)
U = [0.0, 0.0, 0.0, 0.0, 0.1477, 0.2789, 0.4195, 0.5785, 0.7383, 1.0, 1.0, 1.0, 1.0]

# 3. Number of control points = 9, so n = 8 (last index is 8)
n = 8

# Function to find the knot span (i such that U[i] <= u < U[i+1])
def find_knot_span(n, p, u, U):
    if u == U[n+1]:  # Special case: if u is at the end, return last valid span
        return n
    low = p
    high = n + 1
    mid = (low + high) // 2

    # Binary search to find the correct span
    while u < U[mid] or u >= U[mid + 1]:
        if u < U[mid]:
            high = mid
        else:
            low = mid
        mid = (low + high) // 2
    return mid

# Function to compute the p+1 non-zero basis functions N[i-p] to N[i]
def basis_functions(span, u, p, U):
    N = [0.0 for _ in range(p+1)]      # Store the basis function values
    left = [0.0 for _ in range(p+1)]   # Left differences
    right = [0.0 for _ in range(p+1)]  # Right differences

    N[0] = 1.0  # Start with zeroth-degree basis function

    # Loop to compute all higher degree basis functions
    for j in range(1, p+1):
        left[j] = u - U[span + 1 - j]
        right[j] = U[span + j] - u
        saved = 0.0

        for r in range(j):
            denom = right[r + 1] + left[j - r]
            if denom == 0:
                temp = 0.0
            else:
                temp = N[r] / denom
            N[r] = saved + right[r + 1] * temp
            saved = left[j - r] * temp
        N[j] = saved
    return N

# 4. Generate 51 u-values from 0 to 1 (inclusive)
u_values = np.linspace(0, 1, 51)

# 5. For each u, compute span and basis functions
print("u-value\t\tNon-zero basis functions (N[i-3] to N[i])")
print("-" * 60)

for u in u_values:
    span = find_knot_span(n, p, u, U)      # Step 1: Find the span
    N_vals = basis_functions(span, u, p, U)  # Step 2: Compute basis functions
    start_idx = span - p                   # The first basis function index

    # Format and print the 4 non-zero basis functions
    basis_str = ", ".join([f"N[{start_idx + i}]={N_vals[i]:.4f}" for i in range(p+1)])
    print(f"{u:.4f}\t\t{basis_str}")
