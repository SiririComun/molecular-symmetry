import numpy as np

tau = (1.0 + np.sqrt(5.0)) / 2.0

classes = ["E", "C5", "C5_2", "C3", "C2", "i", "S10", "S10_3", "S6", "sigma"]
order = [1, 12, 12, 20, 15, 1, 12, 12, 20, 15]
G_order = 120

# Character table matrix: 10 irreps x 10 classes
chars = np.array([
    # Ag
    [1,  1,       1,      1,  1,  1,  1,       1,      1,  1],
    # Au
    [1,  1,       1,      1,  1, -1, -1,      -1,     -1, -1],
    # T1g
    [3,  tau,     1-tau,  0, -1,  3,  tau,     1-tau,  0, -1],
    # T1u
    [3,  tau,     1-tau,  0, -1, -3, -tau,     tau-1,  0,  1],
    # T2g
    [3,  1-tau,   tau,    0, -1,  3,  1-tau,   tau,    0, -1],
    # T2u
    [3,  1-tau,   tau,    0, -1, -3,  tau-1,  -tau,    0,  1],
    # Gg
    [4, -1,      -1,      1,  0,  4, -1,      -1,      1,  0],
    # Gu
    [4, -1,      -1,      1,  0, -4,  1,       1,     -1,  0],
    # Hg
    [5,  0,       0,     -1,  1,  5,  0,       0,     -1,  1],
    # Hu
    [5,  0,       0,     -1,  1, -5,  0,       0,      1, -1]
], dtype=float)

irreps = ["Ag", "Au", "T1g", "T1u", "T2g", "T2u", "Gg", "Gu", "Hg", "Hu"]

print("=== VERIFYING ROW ORTHOGONALITY ===")
row_pass = True
for i in range(10):
    for j in range(10):
        val = np.sum(np.array(order) * chars[i] * chars[j])
        expected = G_order if i == j else 0.0
        if not np.isclose(val, expected, atol=1e-6):
            print(f"FAILED: <{irreps[i]} | {irreps[j]}> = {val} != {expected}")
            row_pass = False

if row_pass:
    print("SUCCESS: All 100 row-orthogonality relations satisfied strictly (|G| = 120).\n")

print("=== VERIFYING COLUMN ORTHOGONALITY ===")
col_pass = True
for p in range(10):
    for q in range(10):
        val = np.sum(chars[:, p] * chars[:, q])
        expected = (G_order / order[p]) if p == q else 0.0
        if not np.isclose(val, expected, atol=1e-6):
            print(f"FAILED: Col {classes[p]} x Col {classes[q]} = {val} != {expected}")
            col_pass = False

if col_pass:
    print("SUCCESS: All 100 column-orthogonality relations satisfied strictly.")
