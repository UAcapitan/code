
import numpy as np


def act(x):
    return 0 if x < 0.5 else 1

def go(C):
    # Example C = 1,1

    x1 = np.array([C[0], C[1], 1]) # [1, 1, 1]

    # x2 = -1 * x1 + 1.5      w1 = w2 = 1, w3 = -1.5
    # x2 = -1 * x1 + 0.5      w1 = w2 = 1, w3 = -0.5
    w1 = np.array(
        [[1, 1, -1.5], 
        [1, 1, -0.5]]
    )
    res = np.dot(w1, x1) # [0.5, 1.5]

    out = [act(i) for i in res] # [0.5, 1.5] => [1, 1]
    out.append(1) # [1, 1, 1]
    x2 = np.array(out)
    w2 = np.array([-1, 1, -0.5])

    return act(np.dot(w2, x2)) # -0.5 => 0

if __name__ == "__main__":
    C1 = [[1, 1], 0]
    C2 = [[1,0], 1]

    print(go(C1[0]), go(C2[0]))
