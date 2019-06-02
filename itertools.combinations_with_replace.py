# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
a,b=map(str,input().split(" "))
b=int(b)
a=list(a)
a.sort()
c=list(combinations_with_replacement(a,b))
for i in c:
    print("".join(i))
