n=int(input("n:"))
i=1
while i<=n:
  print(i)
  i+=1
print('\n\n')



x=int(input("enter number to find its sum and avg of its digits : "))
temp=x
c=0
s=0
while temp>0:
    d=temp%10
    s+=d
    temp//=10
   
    c+=1
print("the sum of its digits = ",s)
print("the average of its digits = ",s/c)

print('\n\n')
y=int(input("enter number to find palindrome :"))
rev=0
t=y
while t>0:
    d=t%10
    rev=rev*10+d
    t//=10
    
print("the reverse of given number : ",rev)
if rev==y:
    print(rev," is palindrome ")
print('\n\n')

z=int(input("z for fibonacci series:"))
a=0
b=1
print(0,1,end=",")
for i in range(z-2):
    c=a+b;
    print(c,end=",")
    a=b
    b=c
    



