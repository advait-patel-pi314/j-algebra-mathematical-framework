import numpy as np

def make_j_matrix(a0, a1, a2, a3, a4):
    return np.array([
        [a0, a1, a2, a3, a4],
        [0,  a0, a1, a2, a3],
        [0,  0,  a0, a1, a2],
        [0,  0,  0,  a0, a1],
        [0,  0,  0,  0,  a0]
    ])

# Define element z = 2 + 3j + 1j^2
Z = make_j_matrix(2, 3, 1, 0, 0)

# Verify nilpotency: J matrix where a1 = 1, all others 0
J = make_j_matrix(0, 1, 0, 0, 0)
J_5 = np.linalg.matrix_power(J, 5)

print("Matrix Z:\n", Z)
print("\nIsomorphism Verification (J^5 should be all zeros):\n", J_5)
