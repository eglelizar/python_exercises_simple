#Given an array of strings, group them by sub-arrays those ones detected to be anagrams of other ones.
from collections import defaultdict

dictionaries = defaultdict(list)

def getDictionary(string):
    if string not in dictionaries:
        dict = set()
        for x in string:
            dict.add(x)
        #print ("dictionary--->", dict)
        dictionaries [string] = dict
        return dict
    else:
        return dictionaries[string]

def areAnagram(string1, string2):
    if (len(string1) != len(string2)):
        return False
    dictionaryOne = getDictionary(string1)
    dictionaryTwo = getDictionary(string2)
    if (len(dictionaryOne) != len(dictionaryTwo)):
        #print ("they are now equal = ", dictionaryOne, ", ", dictionaryTwo)
        return False
    for x in dictionaryOne:
        if x not in dictionaryTwo:
            return False
    return True

def getAnagramsGroups(words):
    result = []

    wordsDict = set()

    for x in words:
        wordsDict.add(x)

    for x in range(0, len (words)-1):
        for y in range(x+1, len (words)):
            if areAnagram(words[x], words[y]):
                newPair = [words[x], words[y]]
                result.append(newPair)
                wordsDict.remove(words[x])
                wordsDict.remove(words[y])
                break

    for x in wordsDict:
        result.append([x])
    return result



#input words = [ "saco", "arresto", "programa", "rastreo", "caso" ] 5
#Output: [["saco","caso"], ["arresto", "rastreo"], ["programa"]]
words = [ "saco", "arresto", "programa", "rastreo", "caso" ]
print(getAnagramsGroups(words))
