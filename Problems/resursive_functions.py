# Write a recursive function to count the items in a list

def countlst(lst):
    if lst == []:  #The base case
        return 0
    else:
        return 1 + countlst(lst[1:])

lst = [1,2,3,4,5]
print(countlst(lst))


# Write a recursive function to find the max item in a list of numbers

def maxlst(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] if lst[0] > maxlst(lst[1:]) else maxlst(lst[1:])


# Write a recursive function to find x!

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

# Write a recursive function to find the sum of a list of numbers

def sumlst(lst):
    if len(lst) == 1:
        return(lst[0])
    else:
        return lst[0] + sumlst(lst[1:])
