nums = [1,2,3,4,5,6,7,8,9]

def binary_sort(nums, item):
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == item:
            return mid

        if nums[mid] < item:
            low = mid + 1

        if nums[mid] > item:
            high = mid - 1

    return None

if __name__ == '__main__':
    print(binary_sort(nums, int(input('From 1 to 9:\n'))))