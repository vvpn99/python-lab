s=int(input("enter rows :"))
for i in range(1,s+1):
   print("* "*i)

print("\n\n")



for i in range(s,0,-1):
    print("* " *i)
    
print("\n\n")



for i in range(s):
        print(" "*(s-i)+"*"*(2*i+1))
print("\n\n")

for i in range(s,0,-1):
        print(" "*(s+1-i)+"*"*(2*i-1))
        
print("\n\n")




for i in range(s):
        print(" "*(s-i)+"*"*(2*i+1))
for i in range(s,0,-1):
        print(" "*(s+1-i)+"*"*(2*i-1))
print("\n\n")

for i in range(1,6):
   for j in range(0,i):
     print(i,end=" ")
   print()
print("\n\n")





for i in range(1,6):
   for j in range(0,i):
     print(j+1,end=" ")
   print()
print("\n\n")





for i in range(0,s):
   for j in range(0,2*i+1):
      if j<i:
         print(j+1,end=" " )
      elif j>i:
         print(j-i,end=" " )
   print()

print("\n\n")

for i in range(s):
    print(" " * (s- i), end="")

    num = 1

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print('\n\n')


for i in range(s):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()
print("\n\n")





for i in range(s):
   for j in range(s):
      if i==0 or j==0 or j==s-1 or i==s-1:
         print("*",end=" ")
      else:
         print(" ",end=" ")

   print()




print('\n\n')



for i in range(1, s + 1):
    print(" " * (s - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(s - 1, 0, -1):
    print(" " * (s- i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

print('\n\n')    
c=0
for i in range(1,s+1):
   for j in range(i):
      c+=1
      print(c,end=" ")
   print()


print('\n\n')

for i in range(1, s+ 1):
    print("*" * i + " " * (2 * (s - i)) + "*" * i)

for i in range(s, 0, -1):
    print("*" * i + " " * (2 * (s - i)) + "*" * i)
