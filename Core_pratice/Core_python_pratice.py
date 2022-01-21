"""


											 Core python revision
											 --------------------


lists, tuples and sets:
-----------------------
Tuples allow us to work with the sequential data.
sets is the unordered collection of the data with no duplicates.
lists can contain the list of the values with any kind of the data type.
list, string, sets, tuples, dictionary, files, generators are iterable.
list, tuples, strings are sequences.
immutable: int, float, bool, str, tuple, unicode
mutable : list, set, dict

lists:
------
Lists are mutable and duplicates are allowed.
When you tried to print the sum of the element in a list when the list is empty, the sum operation returns zero.
example:
--------
a = []
print(sum(a)) # this returns 0

the difference between the append() and insert() method is insert() takes the position number as the argument. The common thing between the insert() and append() while adding the another list to the existing list, it is added as the sublist for the both the method, but append() don't take the position as the argument, but the insert () is. While adding the single element to another list using the append() and insert() like a.append(10) or a.insert(1,10) it is added as the single element, not as the sublist.

example:
--------
sample = ['maths','physics', 'history','economics']
new_sample = ['python', 'c']
sample.append('chemistry')
sampel.insert(1,'chemistry') #here 1 is the position where we want to insert the new data in the list.
sample.append(new_sample) #this adds the new_sample as the sub list

-->Here the insert() method must take the 2 arguments or it will give the error. Another way of adding the values to the list is using the extend() method. This method is useful when we want to add the multiple list of values to another list. If we add the single element or another list to the existing list using the extend() method, they will added as the individual elements, not as the sublist. we can aslo use the insert method to add the list of items to the existing list. but it will be added as the sub list. While adding the single element to the list using the insert() method the item will be added as the single element not as the sublist, if we try to add the another list to the existing list using the insert() the item will be added as the sublist.
example :
---------
sample = ['history','maths', 'physics','chemisty']
new_sample = ['arts', 'science']

sample.insert(1,new_sample) #this adds as the sub list
sample.extend(new_sample) # this adds as the individual items

-->To remove the items in the list we use the methods remove() or pop(). remove() takes the list item to be removed as the argument and the pop() method by default removes the last item in the list. pop() returns the value it removes. when the function is returning the value means, the result of that function must be stored in a variable. if the value that we want to remove is not found in the list, then it gives the value error, the element not in the list.
example:
--------
sample = ['maths','arts','science']
sample.remove('maths')
popped_value = sample.pop()
print(popped_value)

-->the sort() method is used to sort the items in the list. if the items in the list are text then the they will be sorted in the alphabetical order, if the items are the numbers they will be sorted in ascending order. To reverse the list we use the method reverse(). We can aslo pass the reverse = True as the argument to the sort() method.
example:
---------
sample = ['maths','economics','physics','arts']
sample.sort()
sample.sort(reverse = True)
sample.reverse()

-->the above mentioned methods, they change the original order of the list. If we don't want our original list order must not be changed. We can use the method sorted(). this only returns the modified version of the list. The sort() and reverse() methods returns None.

sorted(sample) or sorted(sample, reverse = True)

-->To find the min and the max values in the list we use the methods min() and max() for list with the numbers.
example:
----------
number = [1,2,4,5,6,6]
min(number) #this returns 1
max(number) #this returns 6

-->To find the index of the item in the list we use the method index().if the element whose index we want to find out is not in the list, then it returns the valueError saying element not in the list.
syntax : list.index(element, start, end)
sample  =['apple','mango','cherry','banana']
sample.index('apple')
sample.index("guave") #this returns the valueError

-->To check if particular list item is in the list we can use the keyword "in". This returns true or false.
sample = ['apple','mango','cheyy']
print('mango' in sample)

-->To print the list of values with the customized index we use the method enumerate(). This method returns 2 value. one is the index and the item. Here we used start = 1 means we can start the index position starting from one. we can also use any number to start.
example:
--------
sample = ['apple','cherry','mango']
for index, item in enumerate(sample, start = 1):
	print(index,item)
	print(index, " : " , item)

-->If we want make the string version of comma seperated values from our list. we use the method join().
join() method returns the value of str data type, split() method returns the value in the list format. The join() method takes only one argument either the single strig value or the list of string.
example:
--------
sample = ['apple','mango','cherry']
sample1 = ' , '.join(sample)#this means all the elements will be joined by putting comma in between them
print(sample1)
new_sample = sample1.split(' , ') #this method removes the comma seperation and forms the new list.
print(new_sample)
output:
-------
apple , mango , cherry
['apple', 'mango', 'cherry']

---------------------------------------------------------------------------------------------------------

strings:
--------
str.capitalize()
-----------------
returns the copy of the string with it's first character capitalize and the remaining in the lowercase.

str.title()
-------------
returns the copy of the string where the first character in every word is upper case.

str.istitle():
--------------
this method checks if the first letter in every word in the string is capital letter. this method return true or false.

str.casefold():
---------------
Returns case folded copy of the string. Converts string to lower case. Case folding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. This like the opposite to istitle() method.
example:
--------
a = 'Hi This Is VenKAT'
print(a.casefold())
print(a)
output:
hi this is venkat
Hi This Is VenKAT

str.swapcase():
----------------
Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

str.lower():
------------
Returns copy of the string in lowercase. Symbols and numbers are ignored.

str.upper():
------------
Returns copy of the string in uppercase. Symbols and numbers are ignored.

str.encode():
-------------
Returns an encoded version of the string in byte format.

str.encode(encoding=”encoding”,errors=”errors”)
encoding(Optional):Default encoding is “utf-8”
errors(Optional):Default errors is “strict”.Raise unicode error.

1= "example öf strings"
print (s1) #Output:example öf strings

#Use backslash for the character that can't be encoded
print(s1.encode(encoding="ascii",errors="backslashreplace")) #Output:b'example \\xf6f strings'

#ignores the character that can't be encoded
print(s1.encode(encoding="ascii",errors="ignore"))#Output:b'example f strings'


#replace the character that can't be encoded with the text explanining the character.
print(s1.encode(encoding="ascii",errors="namereplace"))#Output:b'example \\N{LATIN SMALL LETTER O WITH DIAERESIS}f strings'


#Replace the character that can't be encoded with the question mark
print(s1.encode(encoding="ascii",errors="replace"))#Output:b'example ?f strings'


#Replace the character that can't be encoded with xml character.
print(s1.encode(encoding="ascii",errors="xmlcharrefreplace"))#Output:b'example &#246;f strings'


#strict-Raise Unicode Error
print(s1.encode(encoding="ascii",errors="strict"))
#Output:UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 8: ordinal not in range(128)


#errors are not mentioned.Default is strict-Raise Unicode Error.
print(s1.encode(encoding="ascii"))
#Output:UnicodeEncodeError: 'ascii' codec can't encode character '\xf6' in position 8: ordinal not in range(128)

str.startswith():
-----------------
Returns True, if the string starts with specified value, otherwise returns False.
str.startswith(suffix,start,end)
start,end-(optional)-starting and ending index

s1="example of strings"
#starting and ending index is not given.
print (s1.startswith("ex"))#Output:True

#starts searching from index 5.
print (s1.startswith("le",5,20))#Output:True

#suffix can be tuple of suffixes also.
print (s1.startswith(("example","of")))#Output:True

print (s1.startswith("example of"))#Output:True

print (s1.startswith("hello"))#Output:False

str.endswith():
--------------
Returns True,if the string ends with specified value,otherwise Returns False
str.endswith(suffix,start,end)
start,end — (optional)-starting and ending index.

str.isalnum():
--------------
Returns True if all characters in the string are alphanumeric(alphabets [A-Za-z] and numbers[0–9] are alphanumeric) and there is at least one character. Otherwise returns False.

#space is there,so returns False
s1="example of strings"
print (s1.isalnum()) #Output:False

#empty string,so returns False
s2=''
print (s2.isalnum())#Output:False

s3="apple"
print (s3.isalnum())#Output:True

#contains special characters,so returns False
s4="#$%"
print (s4.isalnum())#Output:False


#contains numbers and alphabets,returns True
s5="123abc"
print (s5.isalnum())#Output:True

isalpha():
----------
Returns True if all characters in the string are alphabetic(A-Za-z) and there is at least one character. Otherwise returns False.

isascii():
----------
Returns True if the string is empty or all characters in the string are ASCII. Otherwise returns False.
Supported in python version 3.7 and above.

isdecimal():
------------
Returns True if all characters in the string are decimal and there is at least one character. Otherwise Returns False. which means the string should contain the number between 0-9. Even the numbers like 10.2, 220.33 are not the decimal numbers.
The decimal number are numbers that can be used to form numbers in the base of 10.

isdigit():
----------
Returns True if all characters in the string are digits and there is at least one character. Otherwise Returns False.
Superscripts, subscripts, and decimal characters are included in digits.

isnumeric():
------------
Returns True if all characters in the string are numeric characters and there is at least one character. Otherwise Returns False.
Superscripts, subscripts, decimal numbers, fractions, roman numerals in unicode are considered to be numeric.

istitle():
----------
Returns True if a string is a title case string and there is at least one character. Otherwise Returns False.

isupper():
----------
Returns True if all cased characters in the string are uppercase. Otherwise Returns False.Numbers, symbols, and spaces are not checked.

islower():
----------
Returns True if all cased characters in the string are lowercase.Other Returns False.Numbers, symbols, and spaces are not checked.

isspace():
----------
Returns True if there is only whitespace in the string and there is at least one character. Otherwise Returns False.

isidentifier():
---------------
Returns True if the string is the valid identifier.It can contain lowercase letters(a-z),upper case letters(A-Z),digits(0–9) and underscore _.It should not begin with digits or contain any spaces. Special characters are not allowed.

isprintable():
--------------
Returns True if all characters in the string are printable or empty. Otherwise Returns False.

str.split():
------------
Returns list of all words in the string using sep as the delimiter string.
If maxsplit is given, at most maxsplits are done and the list will have at most maxsplits+1 elements.
If maxsplit is not specified or -1, there is no limit for the number of splits.
If sep is given, it is used for splitting the string. By default, white space is a separator. sep argument may consist of multiple characters also.
str.split(sep=None,maxsplit=-1)

str.rsplit():
-------------
Returns a list of words in the string, using sep as the delimiter string.
If maxsplit is given, almost maxsplits are done, the rightmost ones.
If sep is not specified or None, whitespace string is a separator.
Except for splitting from the right,rsplit() behaves like split().
str.split(sep=None,maxsplit=-1)

str.splitlines():
-----------------
Returns list of all lines in the string, breaking at line boundaries.
If keepends is True, linebreaks are included in the string, Otherwise not included. The default value is False.
str.splitlines(keepends)

str.find():
-----------
Returns the lowest index in the string where the substring sub is found within the slice s[start: end].Return -1 if the sub is not found.
start, end-Optional arguments.
str.find(sub,start,end)

str.rfind():
------------
Returns the highest index in the string where the substring sub is found within the slice s[start:end].Return -1 if the sub is not found.
start ,end-Optional arguments.
str.rfind(sub,start,end)

str.index():
------------
Similar to find(), Returns the lowest index of the substring found in the string. Raises ValueError, when the substring is not found.
str.rindex(): Similar to find(), Returns the highest index of the substring found in the string. Raises ValueError, when the substring is not found.

str.strip():
------------
Returns copy of the string with leading(spaces at the beginning) and trialing (spaces at the end)characters removed.
chars- The char's argument is a string specifying the set of characters to be removed.
chars argument is not a prefix, rather all combinations of its value are stripped.
If chars is not specified, whitespace is removed.
str.strip(chars)

str.lsrtip():
-------------
Same as strip(),but only leading characters are removed.

str.rstrip():
-------------
Same as strip(),but only trailing characters are removed.

str.center():
-------------
Returns a copy of string which is aligned in the center of length(width) padded with fillchar(default fillchar is an ASCII space). If the width mentioned is less than the length of the string means, the original string is returned.
str.center(width,fillchar)
fillchar(optional)-padding character

str.rjust():
------------
Return a string right-justified in a string of length(width).Padding is done by using the fillchar. The default fillchar is an ASCII space. The original string is returned if the width is less than or equal to len(s)
str.rjust(width,fillchar)

str.ljust():
------------
Similar to rjust(),but return a string left-justified.

str.partition():
----------------
Spilt the string at the first occurrence of sep and return 3-tuple containing the part before separator, the separator itself, and the part after separator.
If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
str.partition(sep)

str.rpartition():
-----------------
Same as partition(), but split the string at last occurrence of sep.
str.rpartition(sep)

str.format():
-------------
Performs string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument or the name of a keyword argument.
Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
str.format(*args,**kwargs)

str.format_map():
-----------------
Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict.
str.format_map(mapping)
mapping- input dictionary

str.join():
-----------
Return a string which is the concatenation of all strings in the iterable. Returns a TypeError, if there are non-string values in the iterable. The separator between elements is the string providing this method.
str.join(iterable)

str.replace():
--------------
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
str.replace(old,new,count)
This method doesn't modify the original string
example:
--------
value = 'hello world'
new_value = value.replace('hello world', 'new world')
print(new_value)

str.zfill():
------------
Returns a copy of string by adding zeros(0) at the beginning of the string to make the string of length(width). If the width mentioned is less than or equal to the length of the string, then the original string is returned. A leading sign prefix (‘+’/’-’) is handled by inserting the padding after the sign character rather than before.
str.zfill(width)

str.expandtabs():
-----------------
Return a copy of the string, where all tab characters are replaced by one or more spaces, depending on the current column and given tab size.
str.expandtabs(tabsize=8)

str.maketrans():
----------------
Returns a mapping table for translation usable for translate() function.
str.maketrans(x,y,z)
x- The string specifying the list of characters that need to be replaced
y-The string specifying the list of characters which is used for replacing x
z-The string specifying the list of characters to be deleted.
If only one argument is mentioned, it should be dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths), or None
If two arguments are mentioned, it should be strings of equal length. Each character is x is mapped to the character at the same position in y.
If the third argument is mentioned, it is mapped to “None” in the result.

str.translate():
----------------
Returns copy of the string in which each character has been mapped through the given translation table.
str.translate(table)
table- translate mapping used to make the translation

count():
--------
Returns the number of occurrences of a substring in the string.
str.count(sub,start,end)
start, end(optional) — starting index and ending index
sub-substring, whose count is to be found.

Conclusion:
------------
Return Type is Boolean:
-----------------------
str.startswith(),str.endswith(),isalnum(),isalpha(),isascii(),isdigit()
isdecimal(),isnumeric(),isupper(),islower(),istitle(),isspace(),
isidentifier(),isprintable()

Return Type is String:
----------------------
str.capitalize(),str.title(),str.casefold(),str.swapcase(),str.lower(),
str.upper(),str.center(),str.encode(),str.strip(),str.rstrip(),str.lstrip(),str.rjust(),str.ljust(),str.format(),str.format_map(),str.join(),str.zfill(),
str.expandtabs(),str.translate()

Return Type is an integer value:
--------------------------------
str.count(),str.find(),str.rfind(),str.index(),str.rindex()
Return Type is List
str.split(),str.splitlines(),str.rsplit()
Return type is tuple
str.partition(),str.rpartition()
Return type is dictionary
str.maketrans()

Returns True if string is empty:
--------------------------------
isascii(),isprintable()
String methods which doesn’t take any parameters.
isalnum(),isalpha(),isascii(),isdigit(),isdecimal(),isnumeric(),islower(),
isupper(),istitle(),isspace(),isidentifier(),isprintable(),str.capitalize(),
str.title(),str.casefold(),str.swapcase(),
str.lower(),str.upper()
isascii() — Supported from Python version 3.7 and above

---------------------------------------------------------------------------------------------------------

Tuples:
-------
tuples are immutable object which follows the order like list. Once the values are assigned, they can't be modified. The below program gives the error " the tuple object doesn't support the item assignment". If it was a List, the item in the index position 1 will changed in both sample and sample1. We can't perform the operations like append(), remove() etc. Duplicates are allowed in tuples.

example:
--------
sample = ('apple','mango','chery')
sample1  = sample
sample[0] = 'banana'
print(sample)
print(sample1)

-->we can also create the tuple without the paranthesis.
example:
--------
a = 1,2,3
print(a)
output : (1,2,3)

-->If we want to create the tuple with only one item, we have to put the comma after the value.
a = (1,)
b = ('hello',)
c = 'mike',
-->if you don't put the comma, the value is not treated as the tuple. if you write like a = (1), then the type of a is int, for b = ('hello'), the type of b is string.

-->tuples has only 2 methods which are index() and count().
index():
--------
index() return the first index at which the value occures. if we give the value which is not in the tuple, it gives the 'valueError'
animals = ('lama', 'sheep', 'cat','lama')
print(animals.index('lama')) #this prints 0.

count():
--------
the count() method returns the no of times the value appeared in the tuple. If item is not in the tuple, then it returns 0.
animals = ('lama', 'sheep', 'cat', 'lama')
print(animals.count('lama')) #this returns 2

tuple unpacking:
----------------
-->tuples are useful for sequence unpacking
x,y = (10,11)
print(x,y)
output : 10 11

---------------------------------------------------------------------------------------------------------

Sets:
------
Sets are the unordered list of the value with no duplicates.
For example if we have 2 sets with common values. To find those common values we use the method intersection(). We can also perform the union operation using the method union().
Python’s set is an unordered collection in Python. It can be used to compute standard math operations, such as intersection, union, difference, and symmetric difference. Other collections — like list, tuple, and dictionary — don’t support set operations. Dict view objects are set-like, which allows set operations.

exmaple:
-------------
set1 = {'apple','mango','cherry','banana'}
set2 = {'apple','mango', 'papaya','gauva'}

new_set1 = set1.intersection(set2)
new_set2 = set1.difference(set2) #returns items in set1 not in set2
new_set3 = set.union(set2)
print(new_set1)
print(new_set2)
print(new_set3)

-->Normally to create the an empty list and tuple we can use the empty brackets or also use the methods list() and tuple(). For sets we can use the method set(). but can't creat empty set like set1 = {}. this creates an empty dictionary.
example:
------------
list1 = []
list1 = list()
print(list1)

tuple1 = ()
tuple1 = tuple()
print(tuple1)

set1 = {} #this creates a new dictionary
set1 = set()#this creates an empty set
print(set1)

-->the operations that we can perform on the sets are
union()
update()
intersection()
intersection_update()
difference()
difference_update()
symmetric_difference()
symmetric_difference_update()
isdisjoint()
issubset()
issuperset()
clear()

union():
--------
Return a new set with elements from the set and the other. It’s performed by union() or by using the | operator
Syntax : union(*others)

Difference between the union() method and the | operator:
union(): It’ll accept any iterables like list, tuples as an argument
| operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

update():
---------
It updates the set, adding elements from the other. But it won’t repeat elements. All elements in the set are unique. It’s performed by using update() or by using the |= operator. The return type is None. It’ll modify the original set itself.
Syntax : update(*others)
set |= other | ...

Difference between the update() method and the |= operator:
update(): It’ll accept any iterable as an argument
|= operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

intersection():
---------------
Return a new set with elements common to the set and the other. It’s performed by intersection() or by using the &operator.
Syntax : intersection(*others)
set & other & ...

Difference between the intersection() method and the & operator:
intersection(): It’ll accept any iterable as an argument
& operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

intersection_update():
----------------------
It updates the set, keeping only elements found in it and the other. It’s performed by using intersection_update() or by using the&= operator. The return type is None. It’ll modify the original set itself.
Syntax : intersection_update(*others)
set &= other & …

difference():
-------------
Returns a new set with elements in the set that aren’t in the other. It’s performed by difference() or by using the -operator.
Syntax
difference(*others)
set - other - ...

Difference between the difference() method and the -operator:
difference(): It’ll accept any iterable as an argument
- operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

difference_update():
--------------------
Removes the element from the set that’s also present in the other set. It’s performed by using the -= operator or by using the difference_update() method. The return type is None. It’ll modify the original set itself.
Syntax : difference_update(*others)
set -= other | ...

Difference between the difference_update() method and the
-= operator:
difference_update(): It’ll accept any iterable as an argument
-= operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError.

symmetric_difference():
-----------------------
Return a new set with elements in either the set or other but not both. It’s performed by symmetric_difference() or by using the ^ operator.
Syntax : symmetric_difference(other)
set ^ other

The symmetric_difference() method isn’t supported by multiple sets. If more than two sets are given, it’ll raise a TypeError. But we can find the symmetric_difference of multiple sets using ^

The difference between the symmetric_difference method and the& operator:
symmetric_difference(): It’ll accept any iterable as an argument. This method doesn’t allow for multiple sets.
^ operator: It’ll accept only a set as an argument. Otherwise, it’ll raise a TypeError. By using the ^ operator, you can find the symmetric_difference between multiple sets.

symmetric_difference_update():
------------------------------
Updates the set, keeping only elements found in either set but not in both. It’s performed by using symmetric_difference_update() or by using the ^= operator. The return type is None. It’ll modify the original set itself.
Syntax : symmetric_difference_update(other)
set ^= other

isdisjoint():
-------------
Returns True if the set has no elements in common with the other. Sets are disjointed if and only if their intersection is the empty set.
Syntax : isdisjoint(other)

issubset():
Test whether every element in the set is in other.
Syntax: issubset(other)
set <= other
Proper subset:
--------------
Test whether the set is a proper subset of other — that is, set <= other and set != other.
Syntax
set < other

Example: Check whether set A is a proper subset of B
If both sets are equal, this means A.issubsetset(B) returns True. But the proper subset A<B will return False.
A={1,2,3,4,5}
B={4,5,6,7,8}
print (A<B)#Output: False

A={1,2,3,4,5}
B={1,2,3,4,5}
print (A<B)#Output: False

A={1,2,3}
B={1,2,3,4,5}
print (A<B)#Output: True

issuperset():
-------------
Test whether every element in other is in the set.
Syntax : issuperset(other)
set >= other
Proper superset:
----------------
Test whether the set is a proper superset of other— that is, set >= other and set != other.
Syntax
set > other
Example: Check whether set A is a proper superset of B.
If both sets are equal, it means A.issuperset(B) returns True. But the proper superset A>B will return False.
A={1,2,3,4,5}
B={4,5}
print (A>B)#Output: True

A={1,2,3,4,5}
B={1,2,3,4,5}
print (A>B)#Output: False

A={1,2,3}
B={1,2,3,4,5}
print (A>B)#Output: True


---------------------------------------------------------------------------------------------------------

Dictinories:
------------
This allows us to work with the key value pairs. Here is key is the unique number which identifies each data value. the dictionaries are the mutable objects. To access the values in the dictinory we can write key in the square brackets or we can use the get() method. If we try to access the index value that is not exist in the dictionary, then it returns the key error, but when I tried it returned None.

exmaple:
--------
new_dict = {'name': 'venkat', 'age': 26, 'course' : ['math','science','physics']}
print(new_dict['name'])
print(new_dict.get('name'))
print(new_dict.get('phone', not_found))#this don't give the error, it returns the message not_found

-->To update the values in the dict we can directly use the square brackets. to update the no of values in the dict we use the method update(). this method takes the dictionary as the argument.
exmaple:
--------
new_dict = {'name' : 'venkat', 'age' : 26, 'courses' : ['math','physics']}
new_dict.update({'name' : 'kiran', 'age' : 28,'courses' : ['chemistry','arts']})
print(new_dict)

-->To delete the the dictionary use 'del', to delete a single element, just write "del dict[key]". pop() method returns the value it deletes. pop() takes atleast one argument.
example:
--------
new_dict = {'name' : 'venkat', 'age' : 26, 'courses' : ['math','physics']}
new_dict.update({'name' : 'kiran', 'age' : 28,'courses' : ['chemistry','arts']})

del new_dict['name']
print(new_dict.pop('age')) #here the pop() method must take one argument or it will give the error.
print(new_dict)


-->To find the length of the dict we use the method len(). To find the keys use method key(), for value use values(), for both key and the values use the method items().
exmaple:
--------
new_dict = {'name' : 'venkat', 'age' : 26, 'courses' : ['math','physics']}
new_dict.update({'name' : 'kiran', 'age' : 28,'courses' : ['chemistry','arts']})

print(len(new_dict))
print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())

-->how to traverse through the dictionary.
new_dict = {'name' : 'venkat', 'age' : 26, 'courses' : ['math', 'physics', 'chemisty']}
for key, values in new_dict.items() :
	print(key, values)

dictionaries:
-------------
-->dictionaries are the key value pairs. the keys can be any immutable data type like numbers, strings etc. lists can't be the keys. The value can be of any data type(list, tuple, str, numbers etc).
To access the value of the key you can use the square brackets []. keep in mind that it gives you valueError if you try to access the value of the key which is doesn't exist. to avoid this error we use the method get().

-->dictionary methods are update(), get(), keys(), values(), items(), pop(), delete().
creating and adding the dictionary is simple. dict[key] = value.

update():
---------
the update() method is used to update the multiple key value pairs.
Dict.update({'ran': 'past tense of run',
                     'shoes': 'plural of shoe'})

del:
----
It is possible to remove the key and it's corresponding value using the del
a = {'a':10, 'b' : 20, 'c' :30}
del a['a']
print(a)


get():
------
get method returns the value of the given key, if that value is not in the dictionary, by default it returns None. The method is very useful to look up keys you don’t know are in the dictionary to avoid KeyErrors.
dict.get('Michael')

-->you can also specify the default return value if the key doesn't exist.
dict.get('michael', 0) #it returns 0 is the key is not in the dictionary.

pop():
------
the pop(key) method delete the given key and it's value, and returns that key'a value.
a = {'a':10, 'b' : 20, 'c' :30}
print(a.pop('a')) #returns 10
print(a) #{'b': 20, 'c': 30}

-->in dictionary the pop() doesn't remove the last element by default like lists. the pop() method here takes one mandatory argument, which is the key. if we try to pop() the key which is not in the dictionary it gives the keyError.

-->you knew about the keys(), values(), items()
a = {'a':10, 'b' : 20, 'c' :30}
print(a.keys())
print(a.values())
print(a.items())
output :
dict_keys(['a', 'b', 'c'])
dict_values([10, 20, 30])
dict_items([('a', 10), ('b', 20), ('c', 30)])

adding the 2 dictionaries:
--------------------------
-->There are actually 2 ways we can add two dictionaries
solution 1:
-----------
a = {'India' : 'delhi', 'usa' : 'washington'}
b = {'sri lanka' : 'columbo', 'china' : 'beijing'}
c = {**a, **b}
print(c)

solution 2: using update()
-----------
a = {'India' : 'delhi', 'usa' : 'washington'}
b = {'sri lanka' : 'columbo', 'china' : 'beijing'}
a.update(b)
print(a)

solution 3: this is my own solution
-----------
a = {'India' : 'delhi', 'usa' : 'washington'}
b = {'sri lanka' : 'columbo', 'china' : 'beijing'}
c =  {}
for i , j in zip(a,b):
	c[i] = a[i]
	c[j] = b[j]
print(c)

solution 4: this working from python 3.9
-----------
a = {'India' : 'delhi', 'usa' : 'washington'}
b = {'sri lanka' : 'columbo', 'china' : 'beijing'}
c = a | b
print(c)


---------------------------------------------------------------------------------------------------------

								Conditions, booleans, if, else, elif statments
								----------------------------------------------


-->the boolean operators are and, or , not.
AND keyword:
-----------
and is used in the conditonal statements to check more than one conditions.
example:
---------
user = 'venkat'
logged_in = True

if user == 'venkat' and logged_in:
	print("logged in")
else:
	print("wrong credentials")

NOT keyword:
------------
not keyword works as the negation. 'not' evaluates the true to false and false to true.
example:
----------
user = 'venkat'
logged_in = False

if not logged_in:
    print("logged in")
else:
    print("wrong credentials")

-->To get the id of the object we use the method id()
example:
--------
a = [1,3,45]
b = [10,20,30]
print(id(a))
print(id(b))

-->If the condition is None or 0 then it evaluates to false. For all the negative and the position numbers it evaluates to the true.
exmaple:
--------
condition = None
if condition:
	print("this is true")
else:
	print("this is false")

-->if we condition is any empty list or sets or dictionary or tuple, then it evaluates as false. It is really helpful when we want to check if the list or sets or dict are empty. for this we don't need to write a seperate method. we can directly pass the sequence.
exmaple:
--------
condition = []
if condition:
	print("true")
else:
	print("false")

---------------------------------------------------------------------------------------------------------

										Loops and iteration(for and while loops)
										----------------------------------------

-->the break statement is used to break out of the loop. No statement will be executed after the 'break' statment.
example:
--------
numbers = [1,2,5,5]
for num in numbers:
	if num == 2:
		break
	print(num)

-->But what if we want to ignore a value and not break out the loop. At that time we use the continue.
the continue will skip the next iteration of the loop. here the continue will skip the last print statement when the num = 3.
example:
--------
numbers = [1,3,5,6]
for num in numbers:
	if num == 3:
		print("found")
		continue
	print(num)

-->The continue statement instructs a loop to continue to the next iteration. Any code that follows the continue statement is not executed. Unlike a break statement, a continue statement does not completely halt a loop. You can use a continue statement in Python to skip over part of a loop when a condition is met.

-->if we write the for loop through the string, it will give the each and every character in the string.
example:
--------
numbers = [1,3,5,6]
for num in number:
	for letter in 'abc':
		print(number, letter)

-->the range() method gives the range of values. Usually we use it in the for loop. By default the initial value of the range() method start with 0. We can also give a particular range.

example:
--------
for i in range(10):
	print(i)
for j in range(1,10):
	print(j)

-->the for loops will iterates for certain number of values. but the while loops keep going until the certain condition is matched or until we hit a break. In below program when 'if x == 5' is true, the loop breaks. so output will be 0 1 2 3 4.
example:
---------
x = 0
while True;
	if x == 5:
		break
	print(x)
	x = x + 1


---------------------------------------------------------------------------------------------------------

												Functions
												---------

-->Functions are basically some instructions that are packaged together to perform a specific task. To create a fucntion we use the "def" keyword.

example:
----------
def func() :
	pass
print(func()) #this calls the function, but it returns none becuase there nothing in the function.
print(func) #this prints the function with particular location.
print(id(func)) #this return the id of the func.

Note: the id and the memory location are different. id is an integer value and the memory location is the alpha numeric value.

-->We can also use the methods like upper and lower on the functions.
example:
def func():
	return "hello world"
print(func().upper()) #the result will be printed in the upper case
pirnt(func().lower())

-->to pass many number of the arguments to the function we have to keep on create the new variables. to avoid that we use the positional and the keyword arguments. The positional argument takes the values as the tuple and the keyword argument takes the values as the key value pairs, simply dictionary values.
example:
--------
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func('math', 'args', name = 'venkat', age = 26)

-->We can also pass the tuples and the dict as the argument to the function. But it takes the all as the tuple. So unpack these values we use the same notation, like we have to keep * and **.
example:
--------
def func(*args, **kwargs):
    print(args)
    print(kwargs)

arguments = ['venkat', 'age', ' addres']
keyword_arguments = {'name' :'venkat' , 'age' : 26}
func(*arguments, **keyword_arguments)

-->sample program for finding the days in month and the leap year
example:
--------
months =[31,28, 30, 31,30,31,30,31,30,31,30,31]

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):

def days_in_month(year, month):
    if not 1<= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return months[month]
print(days_in_month(2000,2))

example:
---------
def is_leap_year(year):

    #check if the year is divisable by 4
    if year % 4 == 0:
        #check if year is divisable by 100
        if year % 100 == 0:
            #check if year is divisable by 400
            if year % 400 == 0:
                return True
            return False
        return True

print(is_leap_year(96))


----------------------------------------------------------------------------------------------------------

											Slicing Lists and strings
											-------------------------


-->The syntax for slicing the list is "list[start:end:step]". here step allows to skip certain number of values. the same rule works with the strings. "step" means how many elements to jump over.
example:
---------
print(my_list[1:5])
print(my_list[1:])
print(my_list[:-1])
print(my_list[:])
print(my_list[-1:])
print(my_list[-1:9:2])
print(my_list[-1:2:-1])
print(my_list[::-1]) #this prints the entire list in the reverse order.


---------------------------------------------------------------------------------------------------------

											List comprehensions
											--------------------

-->the list comprehension is an easier and more readable way to create the list. Remember, while writing the for loops, just think of the comprehensions also.
example:
--------
my_list = [1,2,3,4,5,6,7,8,9]
num = []

for n in my_list:
    num.append(n)
print(num)

-->In the above program we use the append method to store the values into the list num. We can do that without the append() method.
example:
--------
my_list = [1,2,3,4,5,6,7,8,9]
num = []
num1 = []
num = [n for n in my_list]
num1 = [n*n for n in my_list] #this stores the square of the numbers.
num2 = [n for n in my_list if n % 2 == 0] #this stores only the even numbers.
print(num)
print(num1)
print(num2)

-->In the above program we did the same task in a simple and the more readable way. There is another way doing this task using the "map" and "lambda". Map runs everything in the list through a certain function.
lambda is anonymous function. Learn lambda in the later videos.
example: I want a (letter,num) pair for each letter in 'abcd' and each  number in '0123'
--------
my_list = [1,2,3,4,5,6,7,8,9]
num = []

for letter in 'abcd':
    for number in my_list:
        num.append((letter, number))
print(num)

-->Here in the first iteration the (letter, number) becomes ('a', 1), so this entire tuple is added to the list num.
-->to do the above task in the list compreshension.
example:
--------
my_list = [1,2,3,4,5,6,7,8,9]
num = []
num = [(letter, number) for letter in 'abcd' for number in my_list]
num = [(letter, number) for letter in 'abcd' for number in range(10)]
print(num)

-->using the zip() function. But the when we print the result of the zip function , it gives the memory location. So to avoid that, before we print the result of the zip function we have to convert the result into either list or tuples or dictionary(sets).

Return Value from zip()
------------------------
The zip() function returns an iterator of tuples based on the iterable objects. Actually it returns the object of the class type zip. The zip() method is to map the similar index of multiple container so that they can be used just using as single entity. This returns a single iterator object, having mapped values from all the containers.

If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.

Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements. Then, the returned iterator will contain three tuples. It's because iterator stops when the shortest iterable is exhausted.

example:
--------
my_list = [1,2,4,5]
letter = ['a', 'b' , 'c', 'd']
result = zip(my_list,letter)
print(tuple(result))
print(set(result))
print(list(result))

-->From the result of the zip() function we can create the dictionary
example:
--------
my_list = ['a','b','c','d']
letter = ['a','b', 'c','d']
my_dict = {}
for name, hero in zip(my_list,letter):
    my_dict[name] = hero
print(my_dict)

-->let's write the above program using the list comprehension.
example:
--------
my_list = ['a','b','c','d']
letter = ['a','b', 'c','d']
my_dict = {name : hero for name, hero in zip(my_list, letter)}
print(my_dict)

-->if we don't want 'a' to be printed in the result we can write the if condition.
example:
--------
my_list = ['a','b','c','d']
letter = ['a','b', 'c','d']
my_dict = {name : hero for name, hero in zip(my_list, letter) if name!= 'a'}

print(my_dict)

-->Till now we have seen the list comprehension. let's do the set comprehesion.
example:
-------
my_list = [1,2,3,4,5,6,7,8,9]
my_set = set()

for n in my_list :
    my_set.add(n)
print(my_set)

-->let's do the above program using the comprehension.
example:
--------
my_list = [1,2,3,4,5,6,7,8,9]
#my_set = set()

my_set = {n for n in my_list}
print(my_set)

----------------------------------------------------------------------------------------------------------

										Sorting lists, tuples and objects
										---------------------------------

-->To sort the list we use 2 methos sorted() and sort(). The difference is the sorted() method returns the new sorted list. The sort() method modify the original list values. By default these methods do the ascending operation. To the do the descending operation we use the keyword " reverse = True" for the both the methods.
example:
--------
my_list = [0,9,3,6,2,6,21,6,3]

my_list1 = sorted(my_list)
my_list1 = sorted(my_list, reverse = True)

print('sorted list is: \t', my_list1)

my_list.sort()
my_list.sort(reverse = True)
print('sorted list is \t', my_list)

-->For sorting the tuples we can't use the method sort() , because we can't change the order of the elements of the tuple which is immutable, so we use sorted(). Here the sorted method always returns the output as the list type.
example:
--------
my_tuples = (1,2,4,5,6,6,7)
new_tuple = sorted(my_tuples)
print('the new tuple is ', new_tuple)

-->when we apply the sorted() method on dictionary value, it only sorts the keys of the dict.
-->If the list contain the negative values or both negative and the positive values then the sorted() method will not sort the value. to sort the numbers depending on their absolute value we use the notation "key = abs". Here the abs use the function absolute. sorting depending on the absolute value mean the negative values are also considered as the positive and then be sorted.
exmaple:
--------
a = [-10,-9, 4,3 , 7]
b = sorted(a, key = abs)
print(b)

-->But when it comes to sorting of the objects. It is different process. In the above program we use the notation "key = abs". For the key attribute we can also pass the function, lambda expression or any method which is directly imported from the package as the argument.
example:In the below program we passed the method as the argument to the 'key'.
--------
class Employee():
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)

e1 = Employee('carl', 37, 80000)
e2 = Employee('sarah', 33,20000)
e3 = Employee('john', 45, 89999)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name #this means we are sorting the values based on the names.

s_employees = sorted(employees, key = e_sort, reverse = True)
s_employees = sorted(employees, key = lambda e: e.name) #we used the lambda function to sort.
print(s_employees)

-->In the above program whatever the value return by the e_sort and lambda method, 'THE ENTIRE ATTRIBUTES OF OBJECT IS SORTED BY THAT RETURN VALUE OR WHAT EVER THE VALUE IS RETURNED BY THE KEY FUNCTION.'

example: Here we used the lambda function as the argument to the key. What ever the value is returned by the lambda function, then the attributes of the object will be sorted by that return value.
----------
class Employee():
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)

e1 = Employee('carl', 37, 80000)
e2 = Employee('sarah', 33,20000)
e3 = Employee('john', 45, 89999)

employees = [e1, e2,e3]

s_employees = sorted(employees, key = lambda e: e.name) #we used the lambda function to sort.

print(s_employees)

example:Here we used the module operator.
--------
class Employee():
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return "({},{},${})".format(self.name, self.age, self.salary)

from operator import attrgetter

e1 = Employee('carl', 37, 80000)
e2 = Employee('sarah', 33,20000)
e3 = Employee('john', 45, 89999)

employees = [e1,e2,e3]

s_employees = sorted(employees, key = attrgetter('name'))

print(s_employees)

-->Here the attrgetter() method returns a callable object, which fetches attribute from it's operand.

--------------------------------------------------------------------------------------------------------

											String formatting
											-----------------

-->The string formatting is used to print the string exactly the way we want. In the string formatting we use the {} as the place holders and use the format() method to fill the placeholders. We pass the values to the format() method.
exmaple:
--------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {}, age is {}'.format(a['name'], a['age'])
print(sentence)

-->we can also grab the specific things. Directly write the values in placeholders.
example:
--------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0[name]}, age is {1[age]}'.format(a,a)
print(sentence)

-->In the above program we just write the dictionary a 2 times in the format(). Instead of the we can write the 'a' one time and write the 0 in the all the place holders. which means the values in the dictionary will be passed to the placeholders.
example:
---------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0[name]}, age is {0[age]}'.format(a)
print(sentence)

-->This is the same way that we access the list values also.
exmaple:
----------
a = {'name': 'venkat', 'age' : 26}
l = ['venkat', 26]
sentence = 'my name is {0[0]}, age is {0[1]}'.format(l)
print(sentence)

-->we can put the numbers in the placeholders, like which value should by stored in which placeholder. the number in the placeholder denotes the order of the values we passed in the fomat() method.
exmpale:
---------
a = {'name': 'venkat', 'age' : 26}
sentence = 'my name is {0}, age is {1}'.format(a['name'], a['age'])
print(sentence)

->we can also use the tags.
example:
--------
tag = h1
text  = 'this is the heading tag'
sentence = '<{0}> {1} </{0}>'.format(tag, text)
print(sentence)

----------------------------------------------------------------------------------------------------------

-->Shorthand if else statement
example:
--------
a = input(int("enter the fist number"))
b = input(int("entere the second number"))
print(" b is greater than a") if a < b else print("a is greater than b")

----------------------------------------------------------------------------------------------------------

									File objects
									-------------

-->Usually we use the function open() to open the files. This method accepts 2 arguments, one if the name of the file and the other is in which mode you want to open the file. By default the file will be opened in the read mode.
example:
--------
f = open('sample.txt')
print(f.name)
f.close()

-->In the above program we just used the open(). We can also use the "with" keyword.
example:
--------
with open('sample.txt') as f:
	pass
print(f.read()) #this line gives the error.
print(f.closed) #this returns the true.

-->In the above program the advantage of the "with" is we don't have to manually close the file. But if we open the file without the "with" we have to close the file manually. To check we write the f.closed at end of the program. Even it tried to read the file after it is closed it gives the error. It returns true because the "with" automatically closes the file.Don't get confused, the f.close() is used to close the file and f.closed is used to check whether the file is open or not. To read the data in the file we have 2 methods which are "readline()" ,"read()", "readlines()". the readline() always read a single line at a time. readlines() reads all the lines as the list and each line as the element in the list. It also add the new line character at the end of each line. In the print statement we write the end = '', because by default the readline() and readlines() methods adds the new line at at the end of the each statement. The read() method also read all the lines, not one by one.
example:
--------
with open('sample') as f:
	print(f.readlines(), end = '')
	print(f.readline(), end = '')

example:
-------
with open("sample.txt") as f:
	contents = f.read()
	print(contents)

-->To control the reading of the data in the file, we use the for loop.
example:
--------
with open("sample.txt") as f:
	for line in f:
		print(line)

-->If we want to read the only some portion of the file. we use the method read() with some value.
example:
-------
with open("sample.txt") as f:
	print(f.read(100)) #prints the first 100 characters
	print(f.read(100)) #prints the second 100 characters.

-->the above program prints the first 100 characters of the text. If we execute the same read statement again it goes for the next 100 characters. When it reaches the end of the line or the file is empty, then it returns the empty string. There a flaw in the above program. if we keep on executing the f.read() statement, eventhough there is not line to read, it prints lot of empty string. To control we use the condition statement.
example:
--------
with open("sample.txt") as f:
	size = 10
	content = f.read(size)

	while len(content) > 0:
		print(content, end = '')
		content = f.read(size) #if don't write this line, it will be an infinite loop.

-->To check if program really printing the 10 characters at time. we put end = '*' in the print statement.
example:
----------
with open("sample.txt") as f:
	size = 10
	content = f.read(size)

	while len(content) > 0:
		print(content, end = '*')
		content = f.read(size)

-->the tell() method is used to tell the current position of the character in the file. it takes the number as the argument
exmaple :
----------
with open("sample.txt") as f:
	content = f.read(10)
	print(f.tell()) #this prints 10, which means we are at the 10 character in the file.

-->the seek() method is used to set the reading position at wherever we want. if we write seek(0) means at the begining, seek(3) put the reading position at the 3rd character.
example:
--------
with open("sample.txt") as f:
	content = f.read(10)
	print(content)

	f.seek(0)

	content = f.read(10)
	print(content)

-->till now we have seen the file read operation. lets see the writing . for this we use the write() method. While writing into the file we have to mention the mode. If we try to write some text into a file which is not present, there this creates a new file.
example:
--------
with open("sample_write.txt") as f:
	f.write("this is the file for writing")
	f.write("this is the second line")

-->In the above program, the second write statement writes the data into the file from a position where the first line ends. Which means the 2 sentences will be displayed like, they 2 are joined. While writing into the file we can use the seek() method to control writing point. We can also copy the text from a file and write it into another file.
example:
--------
with open("sample.txt") as rf:
	with open("sample_write.txt", mode = 'w') as wf:
		for line in rf:
			wf.write(line)

-->Not only the text, we can also read the images. Lets make the copy of image file. But we can't read the images in the form of bytes as we did for the text before. We have to read the images in the form of the binary files. While opening a file we have mention the name of the with extension like .txt, .jpg.
example:
--------
with open("image.jpg", 'rb') as rf:
	with open('image1.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)

-->Sometimes we want the more control over what we are reading and writing. Instead of doing this line by line let's do this interms of the chunk size as we did previosly for the text files. In this we take the size in terms of the pixels.
example:
--------
with open("image.jpg", 'rb') as rf:
	with open("image1.jpg", 'wb') as wf:
		size = 2000
		content = rf.read(size)

		while len(content) < 0:
			wf.write(content)
			content = rf.read(size)











Important Note:
---------------
By default the print() always go for the new line.
the "is" keyword checks whether the 2 values belongs to the same memory location. "==" only checks the 2 values are equal. We can write an empty function which don't perform any task by using the keyword "pass".
In python the memory is managed dynamically, which means the values exist until there is no more references. As long as the names still refering to a value, the values are still there and once all the names are gone, all the values are inaccessible.

scenario1:
----------
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor






Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

Solution:
----------
students = [('john', 'a', 22), ('amar', 'b', 20), ('ravi', 'c', 30)]
students_sorted = sorted(students, key = lambda a: a[2])
print(students_sorted)

{  OR   }

def last(n):
	return n[-1]

students = [('john', 'a', 22), ('amar', 'b', 20), ('ravi', 'c', 30)]
students_sorted = sorted(students, key = last)
print(students_sorted)


scenario2:
----------
printing the 3*4*6 3D matrix where all the elements are '*', this means we are creating 4*6 matrix in a 3 layer form.

Solution:
---------
a = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(a)

explantion:
-----------
-->the 3*4*6 matrix means we are creating 4*6 matrix with 3 layers. but to create that we go in the reverse order. first create the 3 layers, then create the 4 rows and then 6 columns.
first we start with 3. so we write [for row in range(3)]
then we start with 4, we add another dimention []
[[]for row in range(3)]
[[for col in range(4)] for row in range(3)]
the we start with 6, we add another dimention []
[[[]for col in range(4)] for row in range(3)]
[[[for col in range(6)] for col in range(4)] for row in range(3)]
the finally we add the element to be print
[[['*' for col in range(6)] for cols in range(4)] for row in range(3)]


Scenario3:
-----------
def true(x):
	return lambda y:x
print(true('5v'))

In the above program we only passed the value to x but not to the lambda. So if we try to print the result, it returns the "<function true.<locals>.<lambda> at 0x0055F348>". It simply printing the location of the lambda function. Here the function true is the parent function of the lambda function. So while calling the true method we have to pass the arguments for the lambda function also. Look at the below program. which gives the correct result.

def true(x):
	return lambda y : x
print(true('5v')('gnd'))


Scenario4:(this is the truth table by david beazly)-->for more watch lambda calculus video
----------
def true(x):
    return lambda y: x

def false(x):
    return lambda y:y

def NOT(x):
    return x(false)(true)

assert NOT(true) is false
assert NOT(false) is true

def AND(x):
    return lambda y: x(y)(x)

def OR(x):
    return lambda y: x(x)(y)



print(NOT(true))
print(NOT(false))

print(AND(true)(false))
print(AND(true)(true))
print(AND(false)(true))
print(AND(false)(false))

print(OR(true)(false))
print(OR(true)(true))
print(OR(false)(true))
print(OR(false)(false))


python by raymond hettinger:
---------------------------
ABC(abstract base classes)
-----------------------------
What exactly they are used for..? They are the form of the communication between the subclasses and the parent classes. why to use the subclass. The subclasses are for to reuse the code from some other classes. So the subclass and the other class has to talk to each other.

There are mainly 3 reasons why we need the ABC.
1)The parent can communicate with the subclass. Here is the structure that I demand of you.
2)The class can identify itself as "hey I meet those requirements, I can work with those parent".
3)There is an enforcement mechanism built inside to check and make sure we meet those requirements.

example:
--------
from abc import ABC, abstractmethod

class Entertainer(ABC):
	@abstractmethod
	def sing(self, song):
		pass
	@abstractmethod
	def dance(self):
		pass

explanation for the above program:
----------------------------------
Here we have the Entertainer class. In order to built the ABC, we need to import the abc module and inherit the ABC. The abstactmethod above is an decorator to mark the abstract methods. The sing() and the dance() methods are the not the concrete implementations, they are abstract implimentations, which means we define the code as pass and it doesn't actually do anything.


"""