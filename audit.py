if __name__ == '__main__':
	n = 4794
	total = 1
	for x in range(0, 299):
		total *= (n - x) / (n - x + 6)
	print(total)