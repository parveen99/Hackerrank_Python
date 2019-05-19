def findDigits(n):
    for i in range(0,n):
        c=0
        num=int(input())
        temp=num
        while(num!=0):
            r=num%10
            if(r!=0 and temp%r==0):
                c=c+1
            num=num//10
        print(c)
t=int(input())
findDigits(t)


