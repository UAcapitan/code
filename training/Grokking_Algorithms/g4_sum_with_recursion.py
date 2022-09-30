nums = [1,3,7]

def sum_with_recursion(n):
	if len(n) == 0:
		return 0
	if len(n) == 1:
		return n[0]
	return n[0] + sum_with_recursion(n[1:])

print(sum_with_recursion(nums))
