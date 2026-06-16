# compiler vs interpretor:
A compiler translates the entire high-level source code into machine code (object code) at once before execution, creating an independent executable file that runs fast. Conversely, an interpreter translates and executes code line-by-line, which is slower but allows for easier debugging and faster development. 

## Range:
for i in range(0, 5)   --> iteration from 1,2,3,4,5 \
for i in range(5, 0, -1) --> iteration 5,4,3,2,1   or for i in range(5, -1, -1)  --> 5,4,3,2,1,0 \
for i in range(0, 10, 2) --> 0,2,4,6,8 \
for i in range(10, 0, -2)  --> 10, 8, 6, 4, 2  or for i in range(10, -1, -2) ---> 10, 8, 6, 4, 2, 0 

## Operator:
%   will give reminder
/ division
// truncate division.

19%10 --> 9
19/10 --> 1.9
19//10 --> 1.9 --> 1  

## join:  
use to concatenate elements 
''.join(data)   --> '-', ',' '.'.....
data = list, tuple, set) 

** not the loop itertable elements.

## String
String:    index starts from 0. \
Slicing: s[1:]  --> start to end  \
s[1:5] --> start to 5 characters \
s[-1:]  --> last one character \
s[::-1] --> string reverse \
s[1:n:2] --> s='durgasoftware' n = len(s)  print(s[1:n:2])  == ugsfwr --> pick every second element.
s.upper('hello') --> HELLO  ||    s.lower/casefold('Hello') --> hello   ||   s.capitalize() --> Hello (First letter capital) \
s.count('l') --> 2 (count no of characters in the string). \
s.endswith('geeks') --> end search word should also be string  || s.endswith('geeks', 'com', 'end') --> ends with any one of the value \
s.startswith('geeks')   --> returns true/false values \
s.find(ss, start, end) --> find return the position, if not return -1 \
s.index(e, start, end) --> return index, if not return valueerror \
a = 'john', b = 10 \
print("my name is {} and I am {} old".format(a, b))   \
format_map() --> a ={'x':'john', 'y':'wick'} \
print("My name {x} is and {y}".format_map(a)) \
s.isalnum()  --> s is Python123 return True \
s.isalpha() --> s is "python" return True else false \
s.isdigit() || s.islower() || s.isnumeric() || s.isspace() ||s.istitle() first letter of each character is string then return true \
s.isupper() \
s.rjust(length, fillchar) --> length size of string, fillchar anything \
s.ljust() \
s.lstrip() || s.rstrip()  \
s = 'Learn Python with GeeksforGeeks'  --> s.partition('with') --> split the string into three as ('Learn Python', 'with', 'GeeksforGeeks') \
s.replace('a', 'b') 
## Limitation of string slicing:
Need extra space for every slicing and since many slice increase allocation overhead and garbage collection workload.

## Delete a character in string if character is duplicate:
direct method we don't have it we have create a empty string iteration original string over the loop
and append to list if char is not in the list and end join it.
```
s = 'xyyz'
emp_list  = []
for i in s:
    if i in emp_list:
        pass
    else:
        emp_list.append(i)

print(''.join(emp_list))
```

## sort string:
sorted(string) --> return each character in sorting order in the list.

## reverse string
abc = 'abcdef' \
print(''.join(reversed(abc)))

## split
s.split() --> ['Hello', 'World'] 

## reverse string
```  
a = 'Hello' 
for i in range(len(a)-1, -1, -1):
    print(a[i], end = "")

s =''
for i in a:
    s = i + s
print(s)

reverse list:
str =" geeks quiz practice code"
str_split = str.split()
using list slicing, for loop negative using range, while loop, list reversed function
```
## String compare current and previous char
```
test_str = "geekksforgggeeks"
prev_char = None
empt_list = []
for i in test_str:
    if i == prev_char:
        count = count + 1 
    else:
        prev_char = i
        count = 1
    print(count)
    
```

## character ASCII values
print(ord('A')) --> 67
print(chr(67)) --> A


# List: mutable, duplicated allowed, orderer preserve, heterogenous
empty = [], nestlist = [[],[]], accessing nl[][], comprehension l =[x*x for x in list] \
repeat = [0]*5 = [0,0,0,0,0],  slicing_list [1:3] \
append, remove, extended --> data1.extend(data2) extending data1, list.sort, reverse, pop, insert, copy, index(i) #first occurance \
data.reverse()   reverse a list in-place \
#list(reversed(a))  reverse a list \
sum(list) --> add all elements \
remove(list_value) -- remove the value from list, need to define value from the list \
pop(), del -- delete the object from list based on index and pop will return the deleted value. \
sorted(list, reverse=True/False) --> True is descending order, False is ascending order \
max(list), min(list), max(sublist, key = len), max(a, b) --> max  on both values.

# List Limitations: 
Slow for large-sclae insertion/deletions \
memory overhead(list stores references of objects, not the raw objects. this lead to higher memory) \
Modifying a list from multiple threads may lead to unexpected results unless you use explicit locks. \
No Fixed Size


# sort menthd:
list.sort()  [1,2,3,4]
list.sort(reverse = True) [4,3,2,1]
custom sorting with key:
list.sort(key = len)  --> list has string value it will sort based on len
                          no need to define more than that internally it will handle
list.sort(key = str.lower())
list.sort(key = lambda x:x[1])


## reverse list:
using slicing, for loop with negative range, while loop length check and decrease iterations 

## list vs tuple:
mutuable -- Immutable \
consume more memory -- less memory \
Iterations time consuming -- faster \
good for insertion and delete operations -- accessing elements efficiently \
multiple built-in methods -- fewer built in methods.


## Set: 
mutable, no duplicate, no index, no order, heterogenous objects allowed, \
search, insertion and delete operations are fast because it is using hashing \


s.add('element')
print(set(s1) & set(s2))  # intersection  \
print(set(s1) ^ set(s2))  # difference  \
print(set(s1) - set(s2))  # minus from 1 \
print(set(s1) | set(s2)) # union \ 

set(str1).intersection(str2)
set1.difference(Set2)

append() from list vs add() from set:
Both are adding elements only but difference is append add element last to data set.
add in set is also adding element but order is not guaranty.

methods:
clear() \
remove()  --> remove element, if doesn't exist it will return KeyError \
discard() --> remove element, if doesn't exist it will not return KeyError. \
pop()  --> set is unorder, it will remove and return not element order is not gauranty 


## subset
A.issubset(B)
here A is set otherwise convert it into set. --> set(A) \
then A values is subset of B or not if it subset then return True else False.


# Dictionary:  
## key-value pair, mutable (which means you can modify its contents (add, remove, or change key-value pairs) after it has been created)
d = {},  d.keys(), d.values(), for key, value in d.items(): \
d.pop(key), d.clear(), d1.update(d2), d.copy()  --> deepcopy, d.popitem() \
d.get('key', default_value(default meand if key didn't exist return this value)) \
d['key'] = value -- adding/updating \
del d['key'] \
dict(ac1 & ac2 & ac3)    # intersection in dictionary \
d.keys() or d.values() will return as a list. \
d.fromkeys(key, value) --> create a dictionary, if value not mention default to Non ea


## Nested dict:
d[main_key][nested_key],   d[main_key][nested_key] = value -- update \
using value getting a key directly is not possible. changing keys to values and values to keys then access it. \
or directly knowing the value then getting a key. \
** we can sort dicitionary direclty because of insertion order preserved in dictionary. \
dict(sorted(my_dict.items(),   key = lambda item:item[1]))  ----> sort using values in python. 

## pop() vs popitem():
pop(key) removes based on key and return value \
popitem() removes last inserted key with out key (LIFO) prior 3.7 remove random.

## sort dictionary:
using key sort the data and assign it list p_keys = list(d.keys()) \
accesing list and get value and create a new dictionary
```
p_keys = list(d.keys())
p_keys.sort()
new_d = {i:d[i] for i in p_keys}
print(new_d)
```
sort based on keys:
print(dict(sorted(d.items(), reverse = True)))    --> sort based on keys in descending order \
sort based on values:
print(dict(sorted(d.items, key = lambda x:x[1], reverse = True ))) --> sort based on values in descending order \

d1 = dict(sorted(d.items(), key = lambda x: (-x[1], x[0]))) --> sort based on values if value match then sort by key with in the dictonary  \

## Why dictionary is mutable:
adding, updating, delete are easy ( no extra memory required for every change) \
Dictionaries use hash tables for fast lookups: \
The hash table is efficiently updated when keys or values are changed, which fits naturally with mutability


Yield vs break vs continue:
yield keyword is used within a function to create a generator.
when yield keyword is encounter exection is paused and return the value, again when the function is called then 
exection will resume were it stoped.

break: exit from the loop.

continune: skip the iteration.



*args --> multiple arguments
**kwargs --> key value pair arguments.


Local 			--> with in the function
instance  		--> with self key word
static/class	--> define in the class a global variable	
					can be accessed outside of class
class abc:
	a = 1

s1 = abc()
print(s1.a)

class method
static method  @staticmethod does not depend on any instance or class
instance method

# object: collection of data and its functionality
# class  (blue print for the objects)
class Dog:   ----> class
    species = "Canine"  --> Class attribute/static variable

    def __init__(self, name, age):
        self.name = name  --> Instance attribute
        self.age = age  -->  Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
 
print(dog1.name) 
print(dog1.species)

# inheritance:
allows a class (child class) to acquire properties and methods of another class(parent class)

animal class (p)
dog class (c)
cat class (c)
cow class (c)

# polymorphism
means same operation different behaviour. It allows function or method to have same name to work differently.
1. Method overloading  multiple methods with the same name but different parameters.
2. method overriding  A parent class has a method and child class is inheritance the parent class. In child class specific implementation of a method which is already define in parent class. It is called over riding.
3. duct typing 
4. operator overloading  (1+2 = 3, 'A'+'B' = AB, 3 * 4 = 12, A * 4 = AAAA)
same operator works differently.

# Encapsulation:
is a bundling of data and methods with in a class, restricting access to some components to control intersections.
meaning method and variables are defining as private. 
If a class or method is defined as private these can't be accessed outside the class.
private variable can be override with in the class.
__name is private
_name is public

# Abstraction:
hides the internal implementationd details while expose only the necessary functionality.
it helps focus on "what to do" rather than "how to do it".







Filter(function, iterable):
function is custom function or lambda.
iterable means sequences.


Replace:
s.replace(old, new)
direct replace method we don't have in list, dictionary. need to follow regualr approach  


# Recursion:  
## useful for small identical smaller tasks such as mathematical calculations, tree traversals and divide-and-conquer algorithms. 
A function call by itself is called recursion. \
In the return statement we need to make fail the condition and return it. \
return n*factorial(n-1)   # n= 5 --> 120 backend it store previous iteration value..... \
return n+fibonacci(n-1) \
Type of Recursion: \
Linear/simple Recursion: With out return call itself and decrease the value. (use for loop here) \
Tree/Multiple Recursion: call itself and return the value. \
Tail Recursion: accumulate the calcualte value to next iteration. \
Tail recursion can theoretically be optimized by interpreters, but note that Python does NOT optimize tail calls.

# Memory Management in python:
a = 10 
10 is object
a  = reference 

reference will store in stack
object will store in heap, for each object address will be created.
This address will be store in stack for the reference.
When accessing object then address will be sent to heap and get the value of the address.
https://www.geeksforgeeks.org/python/memory-management-in-python/

ASCII value for the characters is 
ord('A') will return a value


# Collections:
pros: \
minimal code, code readability, improving performance, cleaner and faster implementation and additional functinoalites.

## Counter
Counter: counting words, votes and item frequencies. \
OrderDict: insertion order is preserved, regualr dict before 3.7 release insertion order is not preserved. \
3.7+ insertion order preseved in dict.

```
from collections import Counter
ctr1 = Counter(data)    ## defining counter
ctr1 = Counter([1, 2, 2, 3])
ctr2 = Counter([2, 3, 3, 4])
print(ctr1 + ctr2)   # Addition
print(ctr1 - ctr2)   # Subtraction 
print(ctr1 & ctr2)   # Intersection
print(ctr1 | ctr2)   # Union

print(list(ctr1.elements()))
print(ctr1.most_common(1))
ctr1.update([20, 10, 11])

```

## OrderDict
OrderDict vs Dict  both are preseving insertion order but difference is more control on ordering using OrderDict.\
Control means inserting first/last, deleting first/last etc.. \
od=OrderDict(), OrderedDict(reversed(list(d1.items())))  -- reversing dictionary. \
od.popitem(last=True)   # default true, remove last inserted item \
od.popitem(last=False) # remove first inserted item \
od.pop(key) # delete items \
od.move_to_end('a', last=True) # move to last ** with in the data it will move first and last \
od.move_to_end('a', last=False) # move to first. 
 

## defaultdict 
defaultdict:if we are trying to access key not in the dicitionary it will return KeyError \
but by using defaultdict it will not return error it will return default_factory.

default_factory is list, int and str. \
d = defaultdict(list)  return [] \
d = defaultdict(str)   return blank \
d = defaultdict(int)   return 0



# File Handling
File reading:   \
a = 'This'  \
count = 0   \
file = open('Data/data.txt', 'r')   \
data = file.readline()  \
for line in file:   \
    if a in line:   \
    count = count + 1   

print(count) \
file.close()

file.read()  all data onces \
file.readline()  only read first line \
for line in file:   \
    print(line)

file.readlines()    read line by line, return each line as list end with \n

### chunk:
size = 1024 \
while True:     \
    chunk = file.read(size) \
    if not chunk: \
        break 
    
    print(chunk)



write:
write() \
writelines()

w = write   \
a = append  \
x = create filer \ 
r = read \
b = binary \
encoding = 'utf-8' \
+ - combine with other reading and writing modes \
a+ = append and read \
r+ = read and write \
rb = binary read \
libe by line write: \
for line in file: \
    file.write(line)

### write line by line but doing all in single shot
lines = ["line1\n", "line2\n", "line3\n"] \
file.writelines(lines)

with open("Data.data.txt", "r") as file: \
    data = file.read() \
    print(data)

with open("Data/data.txt", "w") as file: \
    file.write("new content added to the file.\n")

## First and Last line in file
```
with open('Data\Data.txt', 'r') as data:
    first_line = data.readline()
    last_line = None
    for file in data:
        if file is not None:
            last_line = file
```
# directories
os.getcwdb()
os.chdir('C:\\Python33')
os.listdir()
os.listdir('G:\\')
os.mkdir('test')
os.rename('test','new_one')
os.remove('old.txt')
os.rmdir('new_one')
os.walk(path) --> iterates through all subfolders and files
os.stat()
os.path.isfile()
os.path.sidir()
os.chown()
os.chmod()
In order to remove a non-empty directory we can use the rmtree() method inside the shutil module.
import shutil

shutil.rmtree('test')
shutil.copy(source, destination)
shutil.move(source, destination)


Exception: \
try: \
except: \
else: \
finally:


try: except Exception as e: \
    print(f"an error occurred : {e}")


custom exception: \
raise MycustomError("This is a custom error message.", 400)

Handle custom exception: \
try: \
except MyCustomError as e: \
    print(f"Custom error occurred: {e}, Error code: {e.error_code}")

# Error Vs Exception:
Error occured at the time of program writing  (ex: syntax, memory errors)
exception are occuring during run time (ex: missing files, invalid input, divided by zero)

Exceptions:
ZeroDivisionError, ValueError, TypeError, IndexError, FileNotFoundError, Import Error, Indentation Error




JSON File reading:




Data Structures:
Hashing



# max, min, lambda
max(iterable, *iterables, key=None, default=None) \
min(iterable, *iterables, key=None, default=None) \
lambda(argument: expression) \
res = max(test_dict, key = lambda sub: test_dict[sub][key]) \
res_min = min(test_dict, key = lambda sub: test_dict[sub][key]) \
ex: 25_nested_dictionary.py


# Map:
map(function, iterable...)


# subarray, subset, subsequence
subaray means in a given array any consective number is called subarray.
[2,5,1,0,8,10]
entire list is subarray
[2] is sub array because it starts from here
[2,5] is subarray
[5,1,8] is sub array
[1, 10] is not sub array.
formula to calculate no of subarray is n(n+1)/2

all subarrays:
nums = [1,2,3,4]
count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        print(nums[i:j+1])
        count += 1
print(count)

## subsequence:
if given string all element present in the other string, irrespective of order it is called subsequence.
Example:
For the string "abcde":Subsequences: "ace", "abd", "a", "abcde", and "".
here blank is also a subsequence.

# Queue: (FIFO)

## deque
ticket booking, CPU task scheduling, sliding window problems and real-time data processing.
popleft() efficiently removes the first element without shifting, making deque ideal for queues.

dq.append()   -- add end
dq.appendleft() --add front
dq.pop() -- remove end
dq.popleft() -- remove front
dq.remove() -- remove from front
dq.rotate(3) -- last 3 elements move to front.
dq.rotate(-3) -- first 3 elements move to end.
dq.reverse()
dq.clear()
dq.len()


Implementing queue using list:
Removing an item from the front of a list (pop(0)) is costly. All remaining elements must be shifted one position to the left to fill the gap.
Why It’s a Problem: For large queues, this leads to slow performance, especially if you have a high volume of enqueue and dequeue operations
Time Complexity: O(n) per dequeue operation.
n is one loop.

Inflexible for Double-Ended Operations.
While you can add to the end efficiently, removing from both ends (like a double-ended queue or "deque") is not efficient with a list.

Not Thread-Safe by Default
Problem: Standard list operations aren't thread-safe, risking data corruption in concurrent-threaded environments.

Using list we can add element to end.

If we use list inserting will be done in O(1) but dequeue will be done on O(n). both need to be done in O(1).
using deque will be done.


## queue:
thread-safe and efficient.
from queue import Queue
q = Queue(maxsize =3)
q.put()
q.get()
q.full()
q.empty()


# Stack:
Stack:
Last-In/First-Out or First-In/Last-Out.
Insertion and deletion from one end, which is called top of the stack.

No direct concept of stack, it can be implemented in different ways.
1. List  -- append / pop.
2. collections - deque  -- append / pop 

# searching technique

## Linear Search / Sequentical Search :
start from the left side, if key match return true else false.
Compare key element with each element in the list, if matches return true else false.
```
key = 6
list1 = [10, 2, 5, 9, 20, 6, 1, 4]
for i in list1:
if i == key:
    print('True')
else:
print('False')
 ```

## Binary Search / Half Interval search:
1. Findout the middle element in the sorted list.
2. Compare key with the middle element.
3. if key matches with middle element, print message key found.
4. else if key is greater than the middle element then key is searched in right sublist. start with step 1.
5. else if key is smaller than the middle element key searched in left sublist. start with step 1.
6. else print key is not found.

Below is the not exact code refer binary search examples.
```
sort the list first
low = 0
high = len(data)-1
mid = (low + high)//2
 if key == data[mid]:
        first = mid 
        high = mid - 1
    elif key < data[mid]:
        high = mid - 1
    else:
        low = mid + 1 
```
Duplicate data First occurance: \
elif data[mid] < key \
Last occurance: \
key < data[mid]


# Selection Sort Algorithm:
 Ascending order (min()) 
1. find out the minimum value
2. swap minimum value at 0th position
3. take sublist(except sorted part) and repeat step1 and step2 untill list is completely sorted.

min_val = min(data[i:])
min_ind = data.index(min_val)
data[i], data[min_ind] = min_val, data[i]   # this is way od swap is compulsary other wise use temp variable
refer 5_selection_sort_algorithm.py

list.index(element, start, end)



# Bubble Sort:  (sinking sort)
some times reffered as sinking sort, is a simple  sorting algorithm \
which sorts n number of elements in the list by comparing the each pair \
of adjacents items and swaps them if they are in wrong order.

Algorithm Ascending order:
1. starting with the first elemen(index = 0) compare the current element with the next element of the list.
2. If the current element is greater than the next element of the list swap them 
3. If the current element is less than the next element, move to the next element. Repeat step1.



# Quick Sort Algorithm:
works on 1. divide
         2. conquer
         3. combine

pivot element:
first element
last element
random element
medain of three values (first, middle, last) those are based on index
first = 0 index
last = last index 
middle = (low + high)//2 --> index
ex: values (1, 3, 10)  sort it then 3 is median.

Algorithm:
1. select the pivot element
2. find out the correct position of pivot element in the list by rearranging it.
3. Divide te list based on pivot element
4. sort the sublist recursively.


How Algorithm works:
for ascending order below is the condition
pivot value is last element
left <= right
a[left] <= pivot
a[right] >= pivot

for descending order below one is the condition.
pivot value is first element.
left <= right
a[left] >= pivot
a[right] <= pivot


last element is pivot then swap left <--> right
left and right cross swap pivot with left element <-->

First element is pivot then swal left <--> right
left and right cross swap pivot with right element <-->

```
pivot  is first element
ascending order data[left] <= pivot and data[right] >= pivot
descending order data[left] >= pivot and data[right] <= pivot
swaping element is same for both ascending and descending orders (first and right).
pivot = data[first], left = 1,  right = last

pivot  is last element
ascending order data[left] <= pivot and data[right] >= pivot
descending order data[left] >= pivot and data[right] <= pivot
swaping element is same for both ascending and descending orders (last and left).
pivot = data[last], left = 0,  right = last -1 
```


# Two-Pointer Algorithm:
left-right:
1. if left and right starts at same position then increment only right.  (LC - 283)

slow-fast alogrithm: slow and fast algorithm is used cycle detection, finding middle elements and locating intersection points.

cycle detection means: 3 2 0 4 --> 4 is connect to 2 if the connection is thier return True else False.
slow = head, fast = head.next while fast and fast.next is none --> slow = slow.next, fast = fast.next.next

middle elements: 1-2-3-4-5 --> 3 is middle
1-2-3-4-5-6 --> 4 is middle
slow=head=fast 
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow


sliding window:
1. Fixed size
Using a sliding window of fixed size k, we select each subarray of length k and compute its sum. The subarray with the largest sum is the result. We then slide the window forward by one position, continuing until we’ve checked all possible length‑k subarrays.

Ex:
for i in range(k, len(nums)+1):
        windowSum = sum(nums[(i-k):i])

2. variable-size
smallest sub array with positive integers
largest sub array with positive integers.

Same problem with negitive numbers, it will not work.
use prefix sums + a monotonic deque (still “two-ended pointer” style, O(n)):

# max subarray, max subarray sum, max value in subarray.
* subarray sum first k then add next and remove first (refer max_subarray_sum.py)
* subarray sum first k then move to right with slicing(same above point but add next and removing first no need to do it) sum(nums[(i-k):i]) k =5, i=5 
nums[(0:5)] --> k=6, i=6 nums[1:6].....

# small and large sub array.
for and while loop --> iterate each element as right, if sum >= target inside while loop and 
find current subarray length cur_len >< len_data, pos = (left, right),  remove last element from window and increment left, return pos.



import math
math.sqrt(16)  --> 4
abs(-10) --> 10
floor() low closet
ceil()  high closet

Convert number into binary and binary to number --> 32bit
convrt = format(n, '032b')
revrse = convrt[::-1]
org_no = int(revrse, 2)

import re
newstr = re.sub(r'[a-zA-Z0-9\s]', '', srting)

negitive to positive
-15 to 15 use abs(-15) = 15

find a character or symbol:
test.email+alex@leetcode.com
i.split('@')  # ['test.email+alex', 'leetcode.com']

pivot element --> exclude element for sum of list left and right.
LL - 724
count() --> count substring in string how many times it appears 
words = ["mass","as","hero","superhero"]
ex: massasherosuperhero.count('mass') --> mass 1, as 2, hero 2 superhero 1

Power notation: 2**31  is 2 power 31
32-bit --> 2**31


# Findall():
import re
res = re.findall(r'\b\w*o\w*\b', target_string) 

syntax:
re.findall(pattern, string, flags=0)   --> return matching data in list

\d --> matches any digit from 0 to 9 in a target string.
+  --> number contain at minimum one or maximum any number of digits.

\b is a word boundary, [] must start with letter (mention letter in square brackets, ex: 'P')
\w+ means one or more alphanumerical characters after a letter p 
\b end of the word


## '\b[p]\w+\b'   or # '\bp\w+\b'   --> start of the word
## '\bp\w+d\b'                      --> start and end of the word
## '\bpl\w+d\b'                     --> pl two words of start and end with d of the word
## '\be\w+\b | \w+e\b'             --> start or end with of the word
## '\b\w*o\w*\b'                    --> anywhere in the word has 0 letter



# Linked list types:
singly linked list
doubly linked list
circular linked list.


singly linked list:
move forward direction
Add|insertion
--> Add begin, Add end, Add inbetween.
--> delete begin, Add end, Add inbetween.
--> traversal   
Traversing a linked list means visiting every node in the list sequentially, 
starting from the head node and following the links (or pointers) from one node to the next until the end of the list is reached.


doubly Linked List:
forward/backward
Add|insertion
--> Add begin, Add end, Add inbetween.
--> delete begin, Add end, Add inbetween.
--> traversal  

Circular Linked List:
Circular Singly Linked List
Circular Doubly Linked List
Add|insertion
--> Add begin, Add end, Add inbetween.
--> delete begin, Add end, Add inbetween.
--> traversal
Concept: 
same as singly and doubly one the difference is once list formed then need to make circle.
first node with last node.
n.next = self.head 

doubly make circle:
n = self.head
n.next = self.head 
self.head.prev = n


Circular Singly Linked List:
1010    -->  5100 -->   4200
10|5100     20|4200    30|1010



prefix alogirthm approach:
Prefix array: stores cumulative information from start of array up to current index.
Suffix array: stores cumulative information from current index to end of array.



Linked list Pros and Cons:
Pros:
dynamic size
efficient insertions and delections
flexible memory allocations

cons:
slow random access
memory overhead


# Monotonic stack:
finding the nearest smaller or larger element in a sequence for each element in the sequence.
The monotonic stack is a stack that maintains elements in either non-increasing or non-decreasing order from the bottom to the top.

problems:
next greatest element:
nums[stack[-1]] < nums[i]
idx = stack.pop()
result[idx] = nums[i]
stack.append(i)

previous greatest element.
nums[stack[-1]] >= nums[i]:
            stack.pop()
            stack.pop()
if stack:
    result[i] = nums[stack[-1]]
stack.append(i)

next smallest element  same as next greatest element only < less than condition change
previous smallest element same as next greatest element only >= less than condition change

# Hash Table:

Hash Table:
works on Hashing algo
Hash(): takes key as input and outputs hash value
Index: hash(key) % table size
hask(key): hash value


Hash Table terminology:
key, value, Hash Function, index, hashing, table size, rehashing/resizing, load factor

Hash Function:
key --> hash() --> hash code
key = 's0001'
hash(key) --> hash('s0001')
ASCII('s') + ASCII('0') + ASCII('0') + ASCII('0') + ASCII('1')
115 + 48 + 48 + 48 + 49 = 308 (hash code)

Index:
index = hashcode of key % table size 
308 % 10 = 8 

Hashing: calculating hash code and index is called hashing.

table size: no of slots or buckets in the hash table.

** How hash table works is, for every key it will create a hash code as above 
and based on hash code index will be calculated and store in hash table.
Hash table is also called as bucket array.


Hash Tables: ("a", "apple") ("b", "bat") ("c", "cat") ("e", "egg") ("k" "king")
key    hash(key)  index = hash(key) % table size 
"a"		97			97%10 = 7
"b"		98			98%10 = 8
"c"		99			99%10 = 9
"e"		101			101%10 = 1
"k"		107			107%10 = 7

hash table
0
1	("e", "egg")
2
3
4
5
6
7	 ("a", "apple")
8	 ("b", "bat")
9    ("c", "cat")

a and k has same index, this is called collision.
collision resolution technique can be handled using
chaining         both key store in the same index as [("a", "apple"),("k" "king")] both are linked as linked list
open addressing  In open addressing it will be solved using probing technique (in this approach it will go and search for empty row and insert it).
				 1. Linear probing 
				 2. quadratic probing

				Linear formula:
				newIndex = (hashindex + i)%10 , i = 0,1,2,3,4...
				Quadratic: 
				newIndex = (hashindex + i * i)%10 , i = 0,1,2,3,4...

insert(key value)
Find hash code, hash(key) = hash code
calculate index
check slot is empty(bucket in the index is empty)
if bucket is empty insert key value pair
if there is collision 
	use chaining
	or open addressing 


delete:
Apply hash function to key
check the slot corresponding to the hash value
if key matches delete key value pair
if collision exists, you may need to search for the key and remove it and take cae of chaining or any other collison handling methods.




# Heap or priority queue:
heapq (priority queue):
min-heap (smallest)
max-heap (largest)

smallest elements as root and large as leaf nodes
if smallest is popped out then it again rearrange the nodes with smallest as root.
smallest element is popped out first.

methods:
convert list into heap using heapify

heapq.heappushpop() -- add and delete 
heapq.heappush()
heapq.heappop() 



A trianlge can't from sum of any two sides less than are equal to third side then triangle can't form.
