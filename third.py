matrix= [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],]

_num_row=4
_num_col=3
new_matrix=[]

for i in range(_num_row):
    row=[]
    for j in range(_num_col):
        row.append(matrix[j][i])
    new_matrix.append(row)

print(new_matrix)