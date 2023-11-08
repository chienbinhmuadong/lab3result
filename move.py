def move_right(n, str):
    original_str=[i for i in str]
    new_str=''
    for i in range (n):
        change=original_str.pop(-1)
        original_str.insert(0,change)    
    for i in range (len(original_str)):
        new_str+=original_str[i]
    return new_str
def move_left(n,str):
    original_str=[i for i in str]
    new_str=''
    for i in range (n):
        change=original_str.pop(0)
        original_str.append(change)
    for i in range(len(original_str)):
        new_str+=original_str[i]
    return new_str