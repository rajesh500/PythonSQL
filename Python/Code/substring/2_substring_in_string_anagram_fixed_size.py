from collections import Counter

def find_anagrams(s, p):
    m = len(s)
    n = len(p)
    z = ''.join(sorted(p))
    sub = []
    for i in range(m-n+1):
        ss = s[i:n+i]
        a = ''.join(sorted(ss))
        if a == z:
            sub.append(i)

    return sub


y = 'eklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnifvhmoueklpyqrbgjdwtcaxzsnif'
z = 'yqrbgjdwtcaxzsnifvhmou'
#res = find_anagrams("cbaebabacd", "abc")  # [0, 6]
#res = find_anagrams("abab", "ab")
res = find_anagrams(y, z) 
print(res)


