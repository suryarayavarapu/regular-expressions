from collections import Counter

def maxAnagramSize(input_str):
    words = input_str.split(" ")

    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))

    freqDict = Counter(words)

    print(max(freqDict.values()))

if __name__ == "__main__":
    input_str = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input_str)