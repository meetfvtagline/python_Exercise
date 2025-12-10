# Flatten a list using list comprehension and for a loop.
# For example:
#    Input:
#    [[1,2,3], [4,5,6], [7,8,9]]

#    Output: 
#     [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# 	Note: No need to input.



l1=[[1,2,3], [4,5,6], [7,8,9],[10,11,12]]

l2=[(l1[i][j]) for i in range(4) for j in range(3)]

print(l2)