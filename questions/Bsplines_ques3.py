import numpy as np
import matplotlib.pyplot as plt

# 1. Degree
p = 3

# 2. Knot vector
U = [0.0, 0.0, 0.0, 0.0, 0.1477, 0.2789, 0.4195, 0.5785, 0.7383, 1.0, 1.0, 1.0, 1.0]

# 3. Control points
control_points = [
    (0, 30),
    (10, 36),
    (20, 37.5),
    (30, 35),
    (40, 29),
    (50, 21),
    (60, 14),
    (70, 9),
    (80, 6)
]

n = len(control_points) - 1  # Last control point index

# 4. Span-finding function
def find_knot_span(n, p, u, U):
    if u == U[n+1]:
        return n
    low = p
    high = n + 1
    mid = (low + high) // 2
    while u < U[mid] or u >= U[mid + 1]:
        if u < U[mid]:
            high = mid
        else:
            low = mid
        mid = (low + high) // 2
    return mid

# 5. Basis function computation
def basis_functions(span, u, p, U):
    N = [0.0 for _ in range(p+1)]
    left = [0.0 for _ in range(p+1)]
    right = [0.0 for _ in range(p+1)]
    N[0] = 1.0
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

# 6. Generate 51 u values
u_values = np.linspace(0, 1, 51)

# 7. Compute curve points
curve_points = []

for u in u_values:
    span = find_knot_span(n, p, u, U)
    N_vals = basis_functions(span, u, p, U)

    # Compute curve point C(u)
    Cx = 0.0
    Cy = 0.0
    for j in range(p+1):
        i = span - p + j
        x, y = control_points[i]
        Cx += N_vals[j] * x
        Cy += N_vals[j] * y

    curve_points.append((Cx, Cy))

# 8. Extract for plotting
curve_x = [pt[0] for pt in curve_points]
curve_y = [pt[1] for pt in curve_points]
ctrl_x = [pt[0] for pt in control_points]
ctrl_y = [pt[1] for pt in control_points]

# 9. Plot
plt.figure(figsize=(8, 5))
plt.plot(curve_x, curve_y, label="B-spline Curve", color='blue')
plt.plot(ctrl_x, ctrl_y, '--o', label="Control Polygon", color='gray')
plt.title("Cubic B-spline Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
