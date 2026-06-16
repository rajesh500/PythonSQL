data = [56, 3, 2, 78, 6, 0]

selection sort algorithm we need to find the min/max value from the data using list slicing.
each iteration we will need to find the minimum/maximum value and it index position move to iteration position.
iteration position has the value this need to move to low value position.
Example
0 is at 5th position(index) iterating at 0th then move it 0th position.
0th position has a value to 0 value index position.

swap the value -- finding minimum/max value at each iteration and find it index position.
Now move swap the values based on index.



[0, 3, 2, 78, 6, 56]
[0, 2, 3, 78, 6, 56]
[0, 2, 3, 78, 6, 56]
[0, 2, 3, 6, 78, 56]
[0, 2, 3, 6, 56, 78]