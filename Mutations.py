def mutate_string(string, position, character):
    l=[]
    string = string[:position]+character+string[position+1:]
    return string
    

