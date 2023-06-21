# def f1(x):
#     return x * x
#
# res = f1(5)
# print(res)
#
# nums = [1, 2, 3]
# nums2 = []
# for i in nums:
#     t = f1(i)
#     nums2.append(t)
#
# print(nums2)
#
# nums2 = list(map(lambda x: x * x, nums))
# print(nums2)
#
# n1 = [1, 2, 3]
# n2 = [4, 5, 6]
# n3 = list(map(lambda x, y: x * y, n1, n2))
# print(n3)
#
#
# m1 = ['cat', 'dog', 'parrot']
# m2 = list(filter(lambda r: len(r) <= 3, m1))
# print(m1, m2)


from random import randint as rand
nums = []
for i in range(10):
    nums.append(rand(10, 20))
print(nums)
nums = list(filter(lambda x: x % 5 == 0, nums))
print(nums)

names = ['пётр', 'степан', 'Иван']
names = list(map(lambda x: x.upper(), names))
print(names)