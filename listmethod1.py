k=[45,78,95,11,11,11,12,11,56]
print(k)
k.append(23)
print(k)
k.insert(2,44)
print(k)
k.extend([32,30,28])
print(k)
k.remove(95)
print(k)
k.pop(6)
print(k)
k.sort()
print(k)
k.reverse()
print(k)
print(k.count(11))
print(k.index(11))

#12
s=set(k)
print(s)

i=0
#without using set function
while i< len(k)-1:
        
        if k[i]==k[i+1]:
            k.pop(i+1)
        else:
            i+=1
        
print(k)
















    