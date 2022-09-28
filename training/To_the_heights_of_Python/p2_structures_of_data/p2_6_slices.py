
nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[:2])
print(nums[2:])
print(nums[:1:-1])
print(nums[2:][::-1])

nums[2:] = [100]
print(nums)


# Example with table
table_for_example = '''
0....5..........17......
723   Avocado      3
724   Apple        8
725   Banana      10
'''

ID = slice(0, 5)
NAME = slice(5, 17)
COUNT = slice(17, None)

line_items = table_for_example.split("\n")[1:-1]

for item in line_items:
    print(item[ID], item[COUNT], item[NAME])
