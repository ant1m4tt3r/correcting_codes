import numpy as np

NUM_ELEM = 128

GENERATOR_MATRIX = np.array([
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
])

H_MATRIX = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]]


def pretty_print(matrix):
    for vector in matrix:
        print(vector)


def bin_array(num, m):
    """Convert a positive integer num into an m-bit bit vector"""
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)


def generate_words():
    words = []
    i = 0
    while i < NUM_ELEM:
        array = bin_array(i, 7)
        words.append(array)
        i = i + 1

    return words


def generate_encoded_words(raw_words):
    encoded = []
    for word in raw_words:
        encoded.append(word.dot(GENERATOR_MATRIX))

    return encoded


def remainder(element):
    return element % 2


def encode_as_binary(word):
    return list(map(remainder, word))


def multiply_vector_by_H(vector):
    return np.array(H_MATRIX).dot(vector)


def multiply_by_H(elements_matrix):
    return list(map(multiply_vector_by_H, elements_matrix))


def compute():
    raw_words = generate_words()
    encoded = generate_encoded_words(raw_words)
    binary_encoded = list(map(encode_as_binary, encoded))
    matrix_multiplication_result = multiply_by_H(binary_encoded)
    return list(map(encode_as_binary, matrix_multiplication_result))


def main():
    binary_encoded = compute()
    pretty_print(binary_encoded)


if __name__ == '__main__':
    main()
