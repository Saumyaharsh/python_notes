import numpy as np
def find_knot_span(n,p,u,U):
    if u==U[n+1]:
        return n
    low = p
    high = n+1
    mid = (low + high)//2
    while u<U[mid] or u>= U[mid+1]:
        if u < U[mid]:
            high = mid
        else:
            low = mid
        mid = (low + high)//2
    return mid
p = 3 # degree of curve
U = [0.0, 0.0, 0.0, 0.0, 0.1477, 0.2789, 0.4195, 0.5785, 0.7383, 1.0, 1.0, 1.0, 1.0]
control_point = 9
n = control_point - 1
u_vec = np.linspace(0,1,51)
for i in range(0,51):
    u = u_vec[i]
    span = find_knot_span(n,p,u,U)
    print('Knot span for {} is {}'.format(u,span))



