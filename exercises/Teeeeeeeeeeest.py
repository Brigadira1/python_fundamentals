# user_groups = [
#     [
#         {"name": "Yavor", "age": "43"},
#         {"name": "Tihomir", "age": "31"},
#         {"name": "Pesho Speka", "age": "24"},
#         {"name": "Martin", "age": "18"},
#     ]
#     ,
#     [
#         {"name": "Desi", "age": "65"},
#         {"name": "Poly", "age": "39"},
#         {"name": "Marti", "age": "21"},
#         {"name": "Moni", "age": "17"},
#     ]
# ]
#
# less_than_20 = [item["name"] for group in user_groups for item in group if item["age"] < str(20)]
# print(less_than_20)

my_string = "HelloMyNameIsIavor"
new_string = "".join([i for i in my_string])

print(new_string)