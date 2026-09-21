my_tuple = (10, 20, 30)
try:
    my_tuple[1] = 50
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
    
    
    
    
    
    
    
    
t=([1,[2,3]],[4])
t[1][0]=5
print(t)


t1=23,98,97,56,55,34
t2=list(t1)
t2.sort()
print(t2)