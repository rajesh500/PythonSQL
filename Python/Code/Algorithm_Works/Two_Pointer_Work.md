left-right approach:
taking one element from left and right, increasing and decrease by one position until the solution.

left, right --> move same direction
left, right --> move opposite direction
left, right --> start from middle
left, right --> left one step and right two steps 
.
.
.



sliding window:
Using a sliding window of fixed size k, we select each subarray of length k and compute its sum. The subarray with the largest sum is the result. We then slide the window forward by one position, continuing until we’ve checked all possible length‑k subarrays.

Ex:
for i in range(k, len(nums)+1):
        windowSum = sum(nums[(i-k):i])