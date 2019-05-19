def miniMaxSum(arr):
    m1=max(arr)
    s1=sum(arr)
    s1=s1-m1
    m2=min(arr)
    s2=sum(arr)
    s2=s2-m2
    print(s1,s2)







n=list(map(int,input().split()))
miniMaxSum(n)

