#1.
import sys as s
n=s.argv[1]
print("Hello,",n,"!")

'''
C:\Users\Pavan\Documents\py>python greet.py jeevan
Hello, jeevan !
'''
#2.
a=s.argv[2]
b=s.argv[3]
print("a+b = ",int(a)+int(b))

'''
C:\Users\Pavan\Documents\py>python greet.py  20 15
a+b = 35
'''
#3.

import sys

print("Script name:", sys.argv[0])
print("Total arguments passed:", len(sys.argv) - 1)
'''
C:\Users\Pavan\Documents\py>python greet.py  apple banana grapes
Script name: demo.py
Total arguments passed: 3
'''