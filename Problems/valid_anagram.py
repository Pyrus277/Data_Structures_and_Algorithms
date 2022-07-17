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

    if count_s == count_t:
        return True
    
    else:
        return False


print(is_anagram(word_1,word_2))