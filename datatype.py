#A1.1

age =18
current_year = 2026
birth_year = current_year - age
print((type(age)))
print("Age in 2050:",2050-birth_year)
'''
<class 'int'>
Age in 2050: 42
'''

#A1.2

x=17
y=5
print(x//y)
print(x%y)
print(x**2)
'''
3
2
289
'''

#A2.1

F_name ="nikola"
L_name ="tesla"
full_name =F_name+" "+L_name
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(len(full_name))
print(full_name[0],full_name[-1])
#A2.2
print(full_name[0:6])

'''
NIKOLA TESLA
nikola tesla
Nikola Tesla
12
n a
nikola
'''

#A3.1

is_raining = True
is_umbrella =False
print(type(is_raining))
print(type(is_umbrella))
print(is_raining and is_umbrella)
print(is_raining or is_umbrella)
print(not is_raining)
print(True +False*5)

'''
class 'bool'>
<class 'bool'>
False
True
False
1
'''
