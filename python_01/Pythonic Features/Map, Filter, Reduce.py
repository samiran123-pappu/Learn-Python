from functools import reduce

nums = [1,2,3,4]
doubles = list(map(lambda x: x*2, nums))
print(doubles)
evens = list(filter(lambda x: x%2==0, nums))
print(evens)
total = reduce(lambda x,y: x+y, nums)
print(total)
