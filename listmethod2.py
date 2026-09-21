h=[24,77,53,44,57,52,1]
h.sort()
print(h)
s=0
for i in range(len(h)):
    s+=h[i]
print('max=',h[-1])
print('min=',h[-0])
print(s)





#a14
g=[1,2,3]
m=g+h
print(m)
m.sort(reverse=True)
print(m)