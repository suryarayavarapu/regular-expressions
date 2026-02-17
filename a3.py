import re

# Case-insensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

# Case-sensitive replacement of all 'ub'
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# Replace only the first 'ub', case-insensitive
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))

# Replace "AND" with "&", ignoring case
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))