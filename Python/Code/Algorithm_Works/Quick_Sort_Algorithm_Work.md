Quick Sort Algorithm:
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


a = [14, 25, 100, 14, 1, 17]

left = 14, right = 1 and pivot = 17
comparsion will start from left with pivot values
first = 0(index of left), last = 4(index of right)

1. 0 <= 4 --> True then next step
2. 14 <= 17 --> True move to next value
next value


25 <= 17 --> False stop it and move to right

Right side:
1 >= 17: --> False Stop it 
swap the left and right values 
left value is 25 and right value is 1
[14, 1, 100, 14, 25, 17]

Again starts from left:
left = 2, right = 4
2 <= 4
100<=17 --> False -- stop 
right side:
left = 2, right = 3
2 <= 3
14 >= 17 --> False -- stop it
swap left <--> right
    left = 100, right = 14
[14, 1, 14, 100, 25, 17]

Again start from left:
left = 3, right = 3
3<= 3 True 
100 <= 17 --> False -- stop
right side move one position:
right 2, left = 3

3<=2 --> False condition
left and right are crossed then 
swap pivot values with left.

[14, 1, 14, 17, 25, 100]
once crossed then swap the element that means pivot value is in sorted position.
before the pivot and after the pivot elements are not sorted.

Now divide the pivot before value and after values as sub list.
[14, 1, 14] [17], [25, 100]

Repeat the same process what we did above for both sub lists.

finally element is split as sub lists and combine all those
[1, 14, 14, 17, 25, 100]


Pivot value is first element:
[54, 26, 93, 17, 77, 31]
pivot swap is with right.

left = 26, index = 1
right = 31, index = 5
pivot = 54

1. 1<= 5--> True then next step
26 <= 54 --> True next step
left move one position
left = 2, right = 5
2 <= 5:
93 <= 54 --> False -- stop
move to right side:
31 >= 54: --> False -- stop
swap the elements from left to right.
left = 93, right = 31
[54, 26, 31, 17, 77, 93]
left is at 2 is 31
right is at 5 is 93 now 
left side: 
31 <= 54 --> True   next step
left moved one position
left = 3, right = 5
3 <= 5: True
17 <= 54: --> True next step
left move one position 
left =4, right = 5
4 <= 5: True 
77 <= 54: --> False -- stop
right side:

93 >= 54 : True -- next step
right move one position
right =4, left = 4 
4 <= 4: True
77 >= 54: True next step
right moved one position
right =3, left = 4
4 <= 3: False --> stop and left and rigth crossed.
swap the elements right with pivot
[17, 26, 31, 54, 77, 93]
54 is pivot element since right and left crossed.
so sub list before and after pivot.

repeat the same process, each element will be sub list and then combine it.
[17, 26, 31, 54, 77, 93]


Random element:
[10,8,3,17, 14, 1]
17 is random element pivot.swap the 17 to either first or last and perform the same operation.


medain with above list example:
first = 10, last = 1, median (0+len(data)//2 ==> 2.5 ~ 2)
(10, 3, 1) -- sort it (1, 3, 10) --> medain is 3.

