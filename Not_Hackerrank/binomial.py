# 16.4 Compute the binomial coefficients

# def binomial(n, c):
# 	if c in [0, n]:
# 		return 1

# 	includen = binomial(n-1, c-1)
# 	excluden = binomial(n-1, c)

# 	return includen + excluden

def binomial(n, c):
	n_choose_c = [[0] * (c + 1) for _ in range(n + 1)] # caching matrix n x c

	def helper(n, c):
		if c in [0, n]:
			return 1

		if n_choose_c[n][c] == 0:
			includen = helper(n-1, c-1)
			excluden = helper(n-1, c)
			n_choose_c[n][c] = includen + excluden

		return n_choose_c[n][c]

	return helper(n, c)

print(binomial(4 ,2))