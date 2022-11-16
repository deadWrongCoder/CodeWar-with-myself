all_lists = [[1, 2, 3, 4, 5], [2, 5, 6, 7, 3], [8, 9, 0, 3, 4, 2], [2, 3, 4, 5, 6, 7, 8], [0, 9, 7, 5, 4, 3, 2]]
def intersection(all_lists):
  result = [value for value in all_lists[0] if value in all_lists[1]]
  for i in range(2, len(all_lists)):
    result = [value for value in result if value in all_lists[i]]    
  return result

print(intersection(all_lists))
