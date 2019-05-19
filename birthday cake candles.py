def birthdayCakeCandles(ar):
    max1=max(ar)
    print(ar.count(max1))

n=int(input())
arr=list(map(int,input().split()))
birthdayCakeCandles(arr)

