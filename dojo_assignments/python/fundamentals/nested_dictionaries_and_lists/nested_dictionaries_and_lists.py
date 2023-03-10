# # 1 Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30

# x[1][0] = 15
# students[0]['last_name'] = 'Bryant'
# sports_directory['soccer'][0] = 'Andres'
# z[0]['y'] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# #2 Iterate Through a List of Dictionaries

# # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the 
# # function loops through each dictionary in the list and prints each key and 
# # the associated value. For example, given the following list:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for i in range(len(students)):
#         print('first_name - '+students[i]['first_name']+', last_name - '+students[i]['last_name'])
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

#3 Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of
# dictionaries and a key name, the function prints the value stored in that key for each
# dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel


# def iterateDictionary2(key_name, some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][key_name])])
# iterateDictionary2('first_name', 'students')
# iterateDictionary2('last_name', 'students')


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

#4 Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all
# lists, prints the name of each key along with the size of its list, and then prints the
# associated values within each key's list. For example:

# def printInfo(some_dict):
#     for key in some_dict:
#         print(len(some_dict[key]), key)
#         for i in range(len(some_dict[key])):
#             print(some_dict[key][i])
#         print('')


# dojo = {
#   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon













