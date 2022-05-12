nums = [1,2,3,4,5,6,7,8,9]

def binary_with_recursion(n, i):
	if len(n) == 0:
		return None
	mid = len(n) // 2
	if i == n[mid]:
		return mid
	else:
		if i > n[mid]:
			return binary_with_recursion(n[mid+1:], i)
		else:
			return binary_with_recursion(n[:mid], i)

print(binary_with_recursion(nums, 3))
