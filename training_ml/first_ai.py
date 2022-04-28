import numpy as np

def sigmoid(x):
    return 1 / (1 - np.exp(-x))

def main():
    training_inputs = np.array([
        [1,0,1],
        [0,1,1],
        [0,1,1],
        [0,1,0]
    ])
    training_outputs = np.array([
        [0,0,0,1]
    ]).T

    np.random.seed(1)
    sw = 2 * np.random.random((3,1)) - 1

    print(sw)

    for i in range(20000):
        input_layer = training_inputs
        outputs = sigmoid(np.dot(input_layer, sw))

        err = training_outputs - outputs
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    print(outputs)

if __name__ == '__main__':
    main()