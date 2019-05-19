def staircase(n):
    for i in range(0,n):
        for spc in range(n-1-i,0,-1):
            print(" ",end="")
        for char in range(0,i+1):
            print("#",end="")
        print()







n=int(input())
staircase(n)

