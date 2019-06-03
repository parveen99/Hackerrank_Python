# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    f=""
    S=input()
    try:
        re.compile(S)
        f="True"
    except re.error:
        f="False"
    print(f)

