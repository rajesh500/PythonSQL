# problem to find the longest subarray:
# two pointer left and right approach.

def longest_substring(s):
    d = {}
    length = 0
    left = 0
    max_length = 0
    longest_sub = ''
    for index, right in enumerate(s):
        if right in d:# and d[right] >= left:
            #print(s[:length], '2')
            left =  d[right]+1
        d[right] = index
        length = max(length, index-left+1)
        #print(s[:length], '1')
        if length > max_length:
            max_length = length
            longest_sub = s[left:index+1]
    return longest_sub  # length  --> this will return length 



#s = "pwwkew"
s = "abcdefabcbb"
res = longest_substring(s)
print(res)



