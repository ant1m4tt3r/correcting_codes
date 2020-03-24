import numpy as np
from numpy import genfromtxt
from main import pretty_print, encode_as_binary
from numpy.polynomial import Polynomial

error_vectors = genfromtxt('error_vectors.csv', delimiter=';')

polynomial_definitions = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1],
]


polynomials = map(Polynomial, polynomial_definitions)


def generate_rxs():
    rxs = []
    for error_vector in error_vectors:
        polys = []
        for i in range(len(polynomials)):
            poly = error_vector[i] * polynomials[i]
            polys.append(poly)

        rxs.append(polys)
    return list(map(sum, rxs))


def compute():
    return generate_rxs()


def get_coef(poly):
    return poly.coef


def padarray(A):
    t = 8 - len(A)
    return np.pad(A, pad_width=(0, t), mode='constant')


def main():
    polys = compute()
    coeffs = list(map(get_coef, polys))
    coefficients = list(encode_as_binary, list(map(padarray, coeffs)))
    pretty_print(coefficients)


if __name__ == '__main__':
    main()

# pretty_print(error_vectors)
