# In python we use = operator to create the copy of an object. by using this = operator it doesn't create new object
# it create a new variable that share the reference of the original object.

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

# Shallow_copy --> A shallow copy doesn't create a copy of nested object it just copy the reference of nested objects.

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

# Deep copy -->

list1 = [1,2,3,4,5]
list2 = copy.deepcopy(list1)
print(list1,list2)
list1[4] = 'a'
print(list2)
print(list1)