nested_lists=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total=0
for i in range(len(nested_lists)):
    for j in range(len(nested_lists[i])):
        total += nested_lists[i][j]
print(total)