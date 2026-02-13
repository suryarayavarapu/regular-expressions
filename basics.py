#Reg_exp=a special sequence of characters that uses a search pattern to find a string or set of strings.
import re
s="hi hello world"
found=re.search(r'hello',s)# you can use any variable found or match or any understanble meaning varibale
#r' means raw string its different from regular string . 
# r' usage: it won’t interpret the \ character as an escape character
print("start_index",found.start())
print("end_index",found.end())


#re.findall()
#if i want find all intergers in a string
msg="fgklgnmm 234 mg;mfb 4435 kmvlfd4333 "
numeric_in_string=re.findall('\d+',msg)
print(numeric_in_string)
string_upto_space=re.findall('\S+',msg)
print(string_upto_space)               
only_space=re.findall('\s+',msg)
print(only_space)


#re.compile()

print(re.compile('[a-g]').findall(msg))

print(re.compile('\d').findall(msg))

print(re.compile('\d+').findall(msg))


p = re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

p = re.compile('\W')
print(p.findall("he said *** in some_language."))


 #re.sub(pattern, repl, string, count=0, flags=0)
 #pattern : which pattern need to search in variable string
 #repl: it replaced word 
 #string:variable string
 #count: nuber of times such pattern must repeat
msg="i am amstrong american"
print(re.sub('am',"--",msg,count=3,flags=re.IGNORECASE))

# Replace "AND" with "&", ignoring case
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))