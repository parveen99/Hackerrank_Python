n=int(input())
A = list(map(int, input().split()))
A=list(set(A))
A.sort()
print(A[-2])


