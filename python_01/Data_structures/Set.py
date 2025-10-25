s = {1, 2, 3}
s.add(4)
print(s)


s = {1, 2, 3, 4}
s.remove(2)  # will give error if 2 not in set
print(s)


s = {1, 3, 4}
s.discard(3)  # 5 not in set, no error
print(s)


s = {1, 3, 4}
x = s.pop()
print(x)  # element removed
print(s)



s = {1, 3, 4}
s.clear()
print(s)



a = {1, 2}
b = {2, 3, 4}
c = a.union(b)
print(c)


a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
print(c)



a = {1, 2, 3}
b = {2, 3, 4}
c = a.difference(b)
print(c)


a = {1, 2, 3}
b = {2, 3, 4}
c = a.symmetric_difference(b)
print(c)


s = {1, 2, 3}
print(2 in s)  # True
print(5 in s)  # False




s = {1, 2, 3, 4}
print(len(s))  # 4


s = {1, 2, 3}
new_s = s.copy()
print(new_s)
