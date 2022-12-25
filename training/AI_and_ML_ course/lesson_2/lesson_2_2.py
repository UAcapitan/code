
import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(x,y):
    inp = np.array([x,y,1])

    w = np.array([0.3, -0.3, 0.5])

    return act(np.dot(w, inp))

if __name__ == "__main__":
    print(go(0,0))
    print(go(0,1))
    print(go(1,0))
    print(go(1,1))
