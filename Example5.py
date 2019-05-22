# Line 6 & 7 borrowed from this article:
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
import random

prnt_lst = []
usr_list1 = []
usr_list2 = []

"""
num_list1 = int(input("Enter number of elements in first list : "))
usr_list1 = list(map(int,input("\nEnter the numbers : ").strip().split()))[:num_list1]

num_list2 = int(input("Enter number of elements in second list : "))
usr_list2 = list(map(int,input("\nEnter the numbers : ").strip().split()))[:num_list2]
"""

num_list1 = random.randint(0,20)
for i in range(0,num_list1):
    usr_list1.append(random.randint(0, 200))

num_list2 = random.randint(0,20)
for i in range(num_list2):
    usr_list2.append(random.randint(0, 200))


if num_list1 > num_list2 :
    for i in range(num_list1):
        if usr_list1[i] in usr_list2:
            prnt_lst.append(usr_list1[i])

if num_list2 > num_list1 :
    for i in range(num_list2):
        if usr_list2[i] in usr_list1:
            prnt_lst.append(usr_list2[i])

print("The first list: " + str(usr_list1))
print("The second list: " + str(usr_list2))

print("The final list: " + str(prnt_lst))
