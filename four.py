arr=list(map(int,input("Enter Value:").split()))
res=list(map(lambda x:x*2,filter(lambda x:x%2==0,arr)))
print(res)

