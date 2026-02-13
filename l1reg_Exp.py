import re

# Case-sensitive replacement
print(re.subn('ub', '~*', 'Subject has Uber booked already'))

# Case-insensitive replacement
t = re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)
print(len(t))      # tuple length
print(t[0])        # modified string