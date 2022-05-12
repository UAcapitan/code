nums = [1,2,3,4,5,6,7,8,9]

def count_with_recursion(n):
	if len(n) == 0:
		return 0
	return 1 + count_with_recursion(n[1:])

print(count_with_recursion(nums))
