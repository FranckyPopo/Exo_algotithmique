def function_range(first: int, end: int, step: int = 0) -> list:
    liste = list()    
    i = first  
    while i < end:
        liste.append(i)
        
        if not step:
            i += 1
            continue
        i += step
    return liste
    

def function_len(obj) -> int:
    i = 0
    for item in obj:
        i += 1
    return i

# x = function_len(["hello word"])
# print(x)

x = function_range(0, 10, 2)
print(x)
