def plusMinus(arr):
    a=0
    b=0
    c=0
    for i in range(0,len(arr)):
        if(arr[i]>0):
            a=a+1
        elif(arr[i]<0):
            b=b+1
        else:
            c=c+1
    print(a/n)
    print(b/n)
    print(c/n)
    
   












n=int(input())
arr=list(map(int,input().split()))
plusMinus(arr)


