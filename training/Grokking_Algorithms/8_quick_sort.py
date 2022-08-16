nums = [1,5,4,3,7,9,6,8,2]

def quick_sort(n):
	if len(n) < 2:
		return n
	else:
		n1 = n[0]

		low = [i for i in n[1:] if i <= n1]

		high = [i for i in n[1:] if i > n1]

		return quick_sort(low) + [n1] + quick_sort(high)

print(quick_sort(nums))
