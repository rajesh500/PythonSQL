d = {'John': 10, 'Jack': 9, 'Katty': 15, 'Kim':8, 'Lara':12, 'Tim':16}

new_d = {value:key for key, value in d.items()}
print(new_d[15])

tgt = 15
new_tgt = {key for key, value in d.items() if value == tgt }
print(new_tgt)

