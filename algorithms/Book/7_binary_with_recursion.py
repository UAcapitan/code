nums = [1,2,3,4,5,6,7,8,9]

def binary_with_recursion(n, i, low=0, high=None):
	if high is None:
		high = len(n) - 1
	if len(n) == 0:
		return None
	mid = (low + high) // 2
	if i == n[mid]:
		return mid
	else:
		if i > n[mid]:
			return binary_with_recursion(n, i, mid+1, high)
		else:
			return binary_with_recursion(n, i, low, mid-1)

print(binary_with_recursion(nums, 7))
