import numpy as np

generator_matrix = np.array([
	[1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
	[1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
	[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
])

NUM_ELEM = 128


def pretty_print(matrix):
	for vector in matrix:
		print vector

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
		encoded.append(word.dot(generator_matrix))

	return encoded

def module(element):
	return int(element % 2)

def encode_as_binary(word):
	return map(module, word)

def compute():
	raw_words = generate_words()
	encoded = generate_encoded_words(raw_words)
	return map(encode_as_binary, encoded)

def main():
	binary_encoded = compute()
	pretty_print(binary_encoded)

if __name__ == '__main__':
	main()
