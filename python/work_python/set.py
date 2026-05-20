python_set = {"apple", "banana", "apple"}  
python_set.add("banana")
python_set.update({"kiwi","berry"})
print(len(python_set))

print('apple' in python_set)
set2 = {"kiwi"}
set3 = python_set | set2
print(set3)