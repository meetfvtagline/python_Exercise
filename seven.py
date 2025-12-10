row,col=input("Enter size of matrix row * columns : ").split()
rows=int(row)
cols=int(col)

matrix=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        element=int(input(f"Enter element at {i}{j}: "))
        row.append(element)
    matrix.append(row)

print(matrix)

j=cols
ans=0

for i in range(rows):
    _element=matrix[i][j-1]
    ans+=_element

print(ans)