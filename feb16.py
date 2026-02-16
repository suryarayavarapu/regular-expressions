import re
s= "fer tklgm 5434  kg 5.4 6.3g5g5g6 543ggg3 3gg6"
match=re.search(r'543ggg3',s)#regular search r' of string in the string statement
print("start index",match.start())#start (),end () 
print("last index",match.end())
#it will check for only string present or not and it index
#now pattern matched and list how many times occureed in the statement using re.findall()
#those are in the list
k=re.findall(r'4',s)
print(k)
m=re.findall(r'\d+',s)# now all kind of digits in string statement listed
print(m)
n=re.findall(r'\s',s)#print all spaces
print(n)
o=re.findall(r'\S',s)#no spaces only characters
print(o)
#re.compile :compiles regexpr into matching pattern for reused for matching or substitutions
msg=re.compile('[a-f]')
print(msg.findall(s))

import re

# Compile the regex pattern
pattern = re.compile(r"\d+")   # matches one or more digits

text = "Order 123, item 456, code 789"

# Use the compiled pattern
matches = pattern.findall(text)
print(matches)   # ['123', '456', '789']

# You can also use search or match
m = pattern.search(text)# pattern returns untill find its first match
print(m)
print(m.group()) # '123'

