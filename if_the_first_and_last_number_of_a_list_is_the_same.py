#Write a function to return True if the first and last number of a given list is same. 
#If numbers are different then return False.
given_list_1 = [10, 20, 30, 40, 10]
given_list_1_len = len(given_list_1)

given_list_2 = [75, 65, 35, 75, 30]
given_list_2_len = len(given_list_2)


def given_list_result(given_list):
    if given_list[0] / given_list[given_list_1_len-1] == 1:
        return True
    else:
        return False
given_list_1 = [10, 20, 30, 40, 10]


print('The first given list is', given_list_result(given_list_1))