nums = [5,4,9,1,3,2,6,8,7]

def bubble_sort(n):
	for i in range(len(n)-1):
		for j in range(0, len(n)-1-i):
			if n[j] > n[j+1]:
				n[j], n[j+1] = n[j+1], n[j]
	return n

if __name__ == "__main__":
	print(nums)
	print("Results after sorting:\n")
	print(bubble_sort(nums))
