import re

# backslash
match=re.search("\.","integr.fs")
print(match)


#square brackets
#[0,5]=[012345]
#[a-f]=[abcdef]
#[^1-5]=not in the range 1 to 5 .i.e., reamining
#[#a--c]=except abc
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)


import re
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')