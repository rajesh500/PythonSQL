A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

a_split = A.split()
b_split = B.split()
common_words = {}
uncommon_words = {}

for i in b_split:
    if i in a_split:
        if i in common_words:
            common_words[i] +=1
        else:
            common_words[i] = 1
    else:
        uncommon_words[i] = 1


print("common words", common_words)
print("un common words", uncommon_words)
print("un common words keys", list(uncommon_words.keys()))

# AP-2
print(set(a_split) & set(b_split), 'set')