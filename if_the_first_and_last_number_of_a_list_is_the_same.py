#Write a function to return True if the first and last number of a given list is same. 
#If numbers are different then return False.
given_list_1 = [10, 20, 30, 40, 10]
given_list_1_result = str()
given_list_1_len = len(given_list_1)

given_list_2 = [75, 65, 35, 75, 30]
given_list_2_result = str()
given_list_2_len = len(given_list_2)

if given_list_1[0] / given_list_1[given_list_1_len-1] == 1:
    given_list_1_result = 'True'
else:
    given_list_1_result = 'False'

if given_list_2[0] / given_list_2[given_list_2_len-1] == 1:
    given_list_2_result = 'True'
else:
    given_list_2_result = 'False'

print(given_list_1_result)
print(given_list_2_result)