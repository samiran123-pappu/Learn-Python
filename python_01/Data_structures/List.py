nums = [1, 2, 3]
nums.append(4)
print(nums)  # [1, 2, 3, 4]


nums = [1, 2]
nums.extend([2,3, 4, 5])
print(nums)  # [1,2, 2, 3, 4, 5]



nums = [1, 2, 4]
nums.insert(2, 3)
print(nums)  # [1, 2, 3, 4]


nums = [1, 2, 3, 2, 4]
nums.remove(2)
print(nums)  # [1, 3, 2, 4]



nums = [1, 2, 3, 4]
a = nums.pop()
print(a)     # 4
print(nums)  # [1, 2, 3]

b = nums.pop(0)
print(b)     # 1
print(nums)  # [2, 3]



nums = [1, 2, 3]
nums.clear()
print(nums)  # []




nums = [1, 2, 3, 2]
print(nums.index(1))  # 1




nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3


nums = [3, 1, 4, 2]
nums.sort()
print(nums)  # [1, 2, 3, 4]



nums.sort(reverse=True)
print(nums)  # [4, 3, 2, 1]



nums = [1, 2, 3, 4]
nums.reverse()
print(nums)  # [4, 3, 2, 1]



nums = [1, 2, 3]
new_nums = nums.copy()
print(new_nums)  # [1, 2, 3]



nums = [1, 2, 3]
print(len(nums))  # 3



nums = [1, 5, 2, 9]
print(max(nums))  # 9




print(min(nums))  # 1


print(sum(nums))  # 17


nums = [1, 2, 3]
print(2 in nums)  # True
print(5 in nums)  # False


print(5 not in nums)  # True




nums = [1, 2, 3, 4, 5]
print(nums[1:4])   # [2, 3, 4]
print(nums[:3])    # [1, 2, 3]
print(nums[2:])    # [3, 4, 5]
print(nums[-3:])   # [3, 4, 5]



nums = [1, 2]
print(nums * 3)  # [1, 2, 1, 2, 1, 2]



a = [1, 2]
b = [3, 4]
print(a + b)  # [1, 2, 3, 4]


nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
print(squares)  # [1, 4, 9, 16]


nums = [10, 20, 30]
for i, v in enumerate(nums):
    print(i, v)
# Output:
# 0 10
# 1 20
# 2 30



a = [1, 2, 3]
b = ['a', 'b', 'c']
for x, y in zip(a, b):
    print(x, y)
# Output:
# 1 a
# 2 b
# 3 c



nums = [1, 2, 3, 4]
del nums[1]
print(nums)  # [1, 3, 4]

del nums[:2]
print(nums)  # [4]




s = "hello"
chars = list(s)
print(chars)  # ['h', 'e', 'l', 'l', 'o']
