my_string = "Learning Champion"
test = my_string[-1:13:-1]
print(test)
my_list = list(range(26))
copy_list = my_list.copy()
print(f"Before: {copy_list}")
copy_list[:5] = "exp"
print(f"After: :5 replaced by a single string 'exp': {copy_list}")
copy_list[:2] = "experiment"
print(f"After: :2 replaced by a single string 'experiment': {copy_list}")
