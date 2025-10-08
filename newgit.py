
'''
list
List --> sequence type 
used to store multiple values in sequence way
it will declared using []
each value separated with (,) 
there is no memory limitation(n no.of values)
it will follow the insertion order
each value in stored in different indexes 
indexes starts with 0
it will allow the duplicate
it will allow multiple type datas
list is mutable

'''

children_age=[10,12,15,14,63,52,14,25,23,6,2,5,1,4,15]
print(children_age)
children_age.append(74)
print(children_age)
children_age.pop(5)
print(children_age)
print(children_age[1])
children_age.insert(5,52)
print(children_age)
children_age.remove(15)
print(children_age)
children_age.insert(2,15)
print(children_age)
children_age.reverse()
print(children_age)
children_age.reverse()
print(children_age)

'''
Slicing
[start: stop: step]


print(children_age [0:4])
print(children_age[1::2])
take every secound elemts
print(children_age[0::3])
print(children_age[::2])

print(children_age[::-1])
children_age.reverse()
children_age.extend(["Welcome to indias",23.43,34.45])
print(children_age)
'''
print(children_age.index(14))
print(children_age.count(15))

print(children_age)
children_age.sort()
print(children_age)
children_age.sort(reverse=True)
print(children_age)


'''
tuple
multiple type of values
it is immutable
+ve and -ve index
declare tuple ()
'''


phone_number=(984055632,23514789,2315489,2325654748,51562174989,23514789)
print(phone_number)
print(phone_number[4])
print(phone_number[-1])
print(phone_number[::-1])
'''
String --> 
use '' or ""
sequence of character
Immutable
string variable --> store values in the String pool.
string pool presents inside the heap memory

string pool wont allow the duplicate values

if your creating multiple variables with same value
in string pool it will create one value and that value have multiple references

'''

student_name="siddarth tester"
Company="Infosys"

print(student_name)
print(student_name.upper())
print(student_name.lower())
print(student_name.title())
print(student_name.upper())
print(student_name.lower())
print(student_name.capitalize())
print(student_name[::-1])
print(student_name.replace("r","t"))
print(student_name.count("t"))
print(student_name.swapcase())
print(student_name[2])
print(student_name.isascii())
print(student_name.isdigit())
print("siddarth Anandkumar".capitalize())
print("Siddarth Anandkuamr".join(["a", "b"," c"," d"]))
print("my name is siddarth" + f" my age is {26}")

name="siddarth is working in IT sector"
print(len(name))
print(name.split())
date ="14/01/1999"
print(date.split("/"))
print(date.split("-"))
print(name.split("i"))