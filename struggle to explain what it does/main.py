dict = {"key1": [1, 2, 3, 4], "key2": [2, 3, 4], "key3": [9, 0, 3], "key4": [9, 0, 78, 46], "key5": [8, 6, 10]}
list = [1, 2, 3]

keys = []
deleted_keys = []

for key in dict:
  keys.append(key)
 
for i in range(0, len(list)):
  for key, value in dict.items():
    if list[i] in value and key not in deleted_keys:
      keys.remove(key)
      deleted_keys.append(key)
      
    
print(keys)      
