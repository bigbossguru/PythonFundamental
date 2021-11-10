def even(k):
	if k == 1:
		return 0
	else:
		return even(k-1) + 2

print(even(2))