import numpy as np


def sum_array(vec1, vec2):
    vec = vec1 + vec2
    print(vec)


if __name__ == "__main__":
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    sum_array(vec1, vec2)
