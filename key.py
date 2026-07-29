
#1.
import keyword
print("Total number of keywords:", len(keyword.kwlist))
print("\nList of Python keywords:")
print(keyword.kwlist)
'''
Total number of keywords: 35

List of Python keywords:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#2.
import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
    
'''
Enter a word: pass
pass is a Python keyword.
'''
#3.
for = 5
True = 10

# SyntaxError: invalid syntax        
# SyntaxError: cannot assign to True 
