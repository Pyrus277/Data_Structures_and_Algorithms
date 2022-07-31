# Algorithm Notes

Notes taken as I read thru the book Grokking Algorithms by Aditya Y. Bhargava

## Big O Notation

- It's not enough to know how long an algorithm takes to run. You need to know how the running time increases as the list
size increases! 
- For example, simple search entails linear time, but binary search entails log time.  
- Big O doesn't tell you the speed in seconds-- it lets you compare the number of operations. It tells you
how fast the algorithm grows.  
- Big O always assumes the worst case scenario, the maximum number of operations it would take to finish.  
- Logs are always expressed in base 2 and n is the number of operations.  
- Constants are ignored-- so for a sorting algo O(n * 1/2 * n), it's just O(n**2)
  
>&nbsp;&nbsp; Common Big O run times:  
>&nbsp;&nbsp; O(log n)-- log time, ex. Binary Search  
>&nbsp;&nbsp; O(n)-- linear time, ex. Simple search  
>&nbsp;&nbsp; O(n * log n)-- ex. A fast sorting algorithm, like quicksort  
>&nbsp;&nbsp; O(n**2)-- ex. A slow sorting algorithm, like selection sort  
>&nbsp;&nbsp; O(n!)-- factorial time, ex. A really slow algorithm, like traveling salesperson.  
  
## Binary Search  

- Useful when you have a list in sorted order. 
- For an ordered list of n items, in a worst case scenario, it will take binary search log2n steps to run.  
- Speed: O(log n)  

```python
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        
my_list = [1,3,5,7,9]
print(binary_search(my_list, 10))
```  

## The Traveling Salesperson

Example - you have a salesperson that has to visit 5 cities, but wants to
minimize travel time. To do this, every travel permutation must be considered
and from that, the lowest travel distance selected.  
  
There is no known way to solve this faster.

Speed(n!) - Factorial time
This becomes exceedingly slow as the list grows. For 15 cities, it would take 1.3 
TRILLION operations. 

## Selection Sort  
Example - Organizing a list of artists by number of plays.
One approach is to look at all the artists, select the one with the highest count, append, and do it again.  
Speed is O(n * 1/2 * n), but since big O ignores constants, speed is just listed as O(n^2)  
  
Code example - sort an array from smallest to largest:

```python
# Write a function to find the smallest element in the array:

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Now use the function above to write selection sort

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))
```
  
## Recursion
Say we're looking for a key and we know it's in this box.  
But among the items in this box are other boxes, and each of those may contain further boxes still.  
A recursive algorithm is one approach to finding this key. 
**This is a kind of function that refers to itself:**  
We're going to LOOK FOR THE KEY.  
For each item in the box, if it's a box, we're gonna open it and LOOK FOR THE KEY (this is the recusion)  
If the item is the key, we can stop.  
To put this in code:
```python
def look_for_key(box): # box == a list
    for item in box:
        if item == box: # Recursive case
            look_for_key(item) 
        if item == "key": # Base base
            print("found it!"
            break
````
As seen above, every recursive function has a **base case** and a **recursive case**.
Gotta make sure you program the base case correctly, or you'll have an infinite loop.
  
Using the call stack by way of recursion can be convenient, but it can take up a lot of memory. Consider writing a loop instead. 


## Quicksort
Much faster than Selection Sort and often used irl.   
This algorithm makes use of recursion. The base case is a list with a length of 2 items or less-- these lists obbiously don't need sorting.  
Our recursive case takes any list with a length of 2 or greater and from that selects a *pivot*  
We then look at the other numbers and determine if they are greater than or less than the pivot.    
This process is called *partitioning* and it gives us three items:  
-The pivot  
-A list of items that are all less than or equal to the pivot (sub_a)  
-A list of items that are all greater than the pivot (sub_b)  
We then return: sub_a + pivot + sub_b.    
If either sub_a or sub_b is longer than 3 items, we recursively call quicksort on each. 
```python
def quicksort(lst):
    if len(lst) < 2:
        return lst 
    else:
        pivot = lst[0]
        sub_a = [i for i in lst[1:] if i <= pivot]
        sub_b = [i for i in lst[1:] if i > pivot]
                
        return quicksort(sub_a) + [pivot] + quicksort(sub_b)
```
Quicksort is unique in that its Big O depends on the constant.  
When we make a Big O notation like O(n), we really mean c * n, c being the length of time per operation and the constant.  
However, we usually omit the constant because it doesnt matter. When comparing, say, Simple Search O(n) to Binary Search O(log(n)),
even if the constant for simple search is a fraction of that of binary search, binary search is still going to be much, much faster.  
But in the case of Quicksort, the constant *does* matter, and it depends on the *pivot* we choose.  
In the **worse case**, Quicksort will take O(n^2) time, but in the **average case** it will take O(n log n) time. 

####Average case vs Worst case



