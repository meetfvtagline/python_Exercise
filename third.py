# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length.
# For example:
# 	Input:
#  [
#    [1, 2, 3, 4],
#    [5, 6, 7, 8],
#    [9, 10, 11, 12],
#  ]

# Output:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



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