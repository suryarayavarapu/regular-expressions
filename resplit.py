from re import split
#split strings  by the occurence of character or a pattern
#wherever the pattern matches.the ramaining characters are return as list elements
#re.split(pattern,string,maxsplit=0,flags=0)
#only split
print(split('\W+','Wofdh dfdf fhd fhg'))
print(split('\d+','gsrg34 324 5g4 fw3'))
print(split('\W+', "Word's words Words"))
print(split('\W+', 'Words, words , Words'))
import re
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))

import re

# Case-insensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# Case-sensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# Replace only the first 'ub', case-insensitive
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))

# Replace "AND" with "&", ignoring case
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

#re.subn is like re.sub (returning modified string)instead return a tuple
#i.e., to know how many times string replaced
msg=re.subn('sf','oo',"sfsf gfsg sefs eqefsdsf SFVD SFSf sfSF",flags=re.IGNORECASE)
print(msg)