n=5
arr=[[1,2,3,4,5],[6,7,8,9,1],[2,3,4,5,6],[7,8,9,1,0],[9,6,4,2,3]]
def FindMaxProduct(arr,n):
    a=[]
    def product(x):
        temp=1
        for i in x:
            temp=temp*i
        print(temp)
        a.append(temp)
    for i in range(n):
        product(arr[i])
    print(max(a))
FindMaxProduct(arr,n)
