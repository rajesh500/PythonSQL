data = [56, 0, 2, 3, 2, 78, 6, 0]

# ascending order
# for i in range(len(data)):
#     m_val = data[i]
#     for j in range(i+1, len(data)):
#         if data[j] < m_val:
#             m_val = data[j]
#     m_ind = data.index(m_val, i)
#     data[i], data[m_ind] = m_val, data[i]
#     #print(data)
# print(data)

#here with in the data, swaping is happening it doesn't take 0 on every iteration.
# once zero swaped then iteration will start from next element.


# this will give 0 every time, because swap is not happening and iteration is not moving.
# with out swaping even if iteration happens everytime it return zero.
# for i in range(len(data)):
#     m_val = data[i]
#     for j in range(i+1, len(data)):
#         if data[j] < m_val:
#             m_val = data[j]
#     print(m_val)



# descending order
for i in range(len(data)):
    m_val = data[i]
    for j in range(i+1, len(data)):
        if data[j] > m_val:
            m_val = data[j]
    m_ind = data.index(m_val, i)
    data[i], data[m_ind] = m_val, data[i]
    #print(data)
print(data)