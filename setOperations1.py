a={1,2,3,4,5}
b={4,5,6,7,8}
c={1,2}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

print(c.issubset(a))
print(a.issuperset(c))



a.remove(5)
print(a)# produces a key error if it doesnt exist
print(a.discard(5))#produces nothing if it doesnt exist

print(c.isdisjoint(b))