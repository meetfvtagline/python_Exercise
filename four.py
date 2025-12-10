# Find the even elements from an array. Respectively multiply this element in the array.
#             For example:
# Input:
#  [1, 2, 3, 4, 5]

# Output 
#  [4,8]

# 	Note: Need one line code, don't use for loop and if statement.
# 	          Input should be taken from the terminal



arr=list(map(int,input("Enter Value:").split()))
res=list(map(lambda x:x*2,filter(lambda x:x%2==0,arr)))
print(res)

