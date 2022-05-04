nums = [5,4,9,1,3,2,6,8,7]

def bubble_sort(n):
	p, l = len(n)-2, len(n)-1
	for i in range(len(n)):
		n[p], n[l] = n[l], n[p]

if __name__ == "__main__":
	print(bubble_sort(nums))
