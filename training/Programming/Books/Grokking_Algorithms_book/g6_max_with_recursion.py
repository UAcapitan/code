nums = [1,14,2,3,4,5,6,7,8,9]

def max_with_recursion(n):
	if len(n) == 0:
		return 0
	m = max_with_recursion(n[1:])
	return m if n[0] < m else n[0]

print(max_with_recursion(nums))
