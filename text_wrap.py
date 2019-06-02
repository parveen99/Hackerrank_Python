#solution 1

def wrap(string, max_width):
    a=textwrap.fill(string,max_width)



    return a

#solution 2
def wrap(string, max_width):
    a=textwrap.wrap(string,max_width)
    for i in a:
        print(i)



    return " "
