p=[12,11,13,12,12,12,11]
e=set(p.copy())

p=list(e.copy())
p.sort()
print(p)

c={x**2 for x in range(1,21) if x%2!=0}
print(c)