



def f(n):

	if n==1:
		return 1
	return f(n-1) + n


def g(n):
	total=0
	row = n
	while row > 0:
		total += f(row)
		row -=1
	return total

print(f(12))
print(g(12))

