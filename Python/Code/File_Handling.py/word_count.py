# count total number of words in a file
# import re
# with open('Data\word_count.txt', mode = 'r', encoding='utf-8') as file:
#     data = file.read()
#     sp_data = data.split()
#     count = 0
#     for i in sp_data:
#         count = count + 1

# print(count)


# find a word and count it.
# import re
# with open('Data\word_count.txt', mode = 'r', encoding='utf-8') as file:
#     data = file.read()
#     res = re.findall(r'\b[p]\w+n\b', data)
#     count = 0
#     for i in res:
#         count = count + 1

# print(count)



# total characters
def file_char_count(filename):
    try:
        with open(filename, mode = 'r', encoding='utf-8') as file:
            data = file.read()
            return len(data)
    except FileNotFoundError as e:
        return f"Error :'{filename}' not found."
    

path =  'Data\word_count1.txt'
res = file_char_count(path)
print(res)