# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def valid_anagram(s, t):
    """checks if t is an anagram of s
    parameters: two strings
    returns: true if anagram, false if not"""

    # sort each string
    # test if equal to each other
    # return boolean
    return sorted(s) == sorted(t) # runtime O(n log n)


s1 = "car"
t1 = "rac"
# return true

s2 = "bee"
t2 = "ebb"
# return false

print(valid_anagram(s1, t1))
print(valid_anagram(s2, t2))

# account for lowercase/uppercase. we will assume it is all lowercase

def valid_anagram2(s, t):
    """checks if t is an anagram of s
    parameters: two strings
    returns: true if anagram, false if not"""
    if len(s) != len(t):
        return False

    # count each char in strings and store in dict
    countS, countT = {}, {} # space O(s + t)

    for i in range(len(s)): #runtime O(s)
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    # check if each char has same count in both s and t
    for char in countS: # runtime O(s)
        if countS[char] != countT.get(char, 0):
            return False
    # if not, return False

    return True


s1 = "car"
t1 = "rac"
# return true

s2 = "bee"
t2 = "ebb"
# return false

print(valid_anagram2(s1, t1))
print(valid_anagram2(s2, t2))