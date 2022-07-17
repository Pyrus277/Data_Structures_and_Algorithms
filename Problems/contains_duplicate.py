# Topic: Arrays and Hashing
# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

def contains_dup(nums):
        """
        Function sets up a hash set. Then it iterates thru the list
        of numbers adding the number to the set each time. If we hit
        a value that is already in the set, we know it's a dup and 
        can return True.
        """
        nums_set = set()
        
        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        return(False)