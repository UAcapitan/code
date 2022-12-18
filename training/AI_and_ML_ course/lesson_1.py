
import numpy as np


def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr_):
    x = np.array([house, rock, attr_])

    w1 = [0.3, 0.3, 0]
    w2 = [0.4, -0.5, 1]

    weight1 = np.array([w1, w2])
    weight2 = np.array([-1, 1])

    sum_hidden = np.dot(weight1, x)
    print(sum_hidden)

    out_hidden = np.array([act(x) for x in sum_hidden])
    print(out_hidden)

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)

    match y:
        case 1:
            return "Like"
        case 0:
            return "Don't like"


if __name__ == "__main__":
    print(go(1,0,1))
    print(go(1,1,1))
    print(go(1,0,0))
