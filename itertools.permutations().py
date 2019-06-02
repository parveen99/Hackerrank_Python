# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b=map(str,input().split(" "))
b=int(b)
c=list(permutations(a,b))
c.sort()
for i in c:
    print("".join(i))

