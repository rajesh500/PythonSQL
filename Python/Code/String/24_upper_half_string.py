test_str = 'apples' 

len_check = len(test_str)
if len_check%2==0:
    half_len = len_check//2
    second_half = test_str[half_len:]
    first_half = test_str[:half_len]
    print(first_half+second_half.upper())


