# Topic: Arrays and Hashing
# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.

word_1 = input()
word_2 = input()
print('')

# My initial solution-- O(s + t) (I think?)
def is_anagram(s,t):
    ''' Interior function makes a dictionary of
    the letters and repsective counts. Exterior
    fuction calls this for each input word and then
    makes the comparison to determine the return value.
    '''
    def letter_ct(wrd):
        lett_dict = {}
        for letter in wrd:
            if letter in lett_dict:
                continue
            else: 
                lett_dict[letter] = wrd.count(letter)
        
        return lett_dict

    count_s = letter_ct(s)
    count_t = letter_ct(t)

    return count_s == count_t


# Alternate solution from the youtubes

def is_anagram2(s: str, t: str) -> bool:
    # First make sure they're the same length before you
    # go through all the trouble to make a comparison. Why
    # didn't I think of that.
    if len(s) != len(t):
        return False
    # set up your dictionaries
    count_s, count_t = {}, {} 

    for i in range(len(s)):
        # This line condenses down with the .get() function what 
        # you did in your code when populating your letter count
        # dictionary. 
        # We're incrementing the count of the letters, but if the
        # letter key does not yet exist in the dictionary, .get()
        # will add it with a default value of zero! 
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    if count_s == count_t:
        return True
    else:
        return False

# A very pythonic solution:
def is_anagram3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# A solution with O(1)
#   This one is good for memory, assuming the sort doesn't use extra
#   space (A question to ask. In general, sort methods are assumed not
#   to), but it might take a hit on time.
def is_anagram4(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)




print(is_anagram(word_1,word_2))

