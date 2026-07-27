#1.
a=200
if a>100:
    print("a is greater than 100")
#IndentationError: expected an indented block after 'if' statement on line 2
#a is greater than 100

#2.
i=0
for i in range(11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
'''
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd
10 is even
'''
#3.
x=5
if x>0:
   print("x is positive")
else:
    print("x is non-positive")
#x is positive