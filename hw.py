from collections import Counter
words = ['cars', 'bikes', 'arcs', 'steer']
max_anagrams = max(map(lambda x: sum(Counter(y) == Counter(x) for y in words), words), default=0)
print(max_anagrams)