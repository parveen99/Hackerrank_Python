
def compareTriplets():
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    x=0
    y=0
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            x=x+1
        elif(a[i]<b[i]):
            y=y+1
    print(x,y)
   
compareTriplets()



  
