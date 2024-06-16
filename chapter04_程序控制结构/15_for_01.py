# 编写一个程序，可以打印10句 “hsp” 。
# 定义一个列表（后面详细介绍），可以视为一个数据集
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums, type(nums))

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("hsp", i)

for i in nums:
    print("hsp", i)

# 代码执行内存分析法
print(nums, id(nums), nums[0], id(nums[0]))
print(nums, id(nums), nums[1], id(nums[1]))
print(id(1))
nums2 = [1, 2]
print(nums2, id(nums2), nums2[0], id(nums2[0]))
