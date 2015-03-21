# prints list of common words in frankenstein

import operator

fo = open('frankenstein.txt')
lineList = fo.read().split('\n')
fo.close()


wordList = {}
for line in lineList:
    words = line.split(' ')
    for word in words:
        if word not in wordList:
            wordList[word] = 1
        else:
            wordList[word] += 1

sorted_wordList = sorted(wordList.items(), key=operator.itemgetter(1))

for i in range(len(sorted_wordList) - 100, len(sorted_wordList)):
    print(sorted_wordList[i])
