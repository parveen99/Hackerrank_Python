n = int(input())
a = []
for _ in range(n):
    grades_item = int(input())
    a.append(grades_item)
for i in range(0,len(a)):
    if(a[i]>=38):
        if((a[i]+2)%5==0):
            a[i]=a[i]+2
        elif((a[i]+1)%5==0):
            a[i]=a[i]+1
        elif(a[i]%5==0):
            a[i]=a[i]+0
for j in range(0,len(a)):
    print(a[j])
