string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
split_data = string.split()
for i in split_data:
    if i.startswith('https') or i.startswith('http'):
        print(i)

l = []
for j in split_data:
    if j.find("https")==0 or j.find("http")==0:
        l.append(j)
print(l)