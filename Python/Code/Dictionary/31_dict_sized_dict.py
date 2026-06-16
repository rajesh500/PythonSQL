test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

d_data = test_dict.items()
print(d_data, 'data')
half = int(len(d_data)/2)
print(half)
#print(d_data[:half])
ld_data = list(d_data)
print(dict(ld_data[:half]))
print(dict(ld_data[half:]))