def functionn_range(first: int, end: int, step: int = 0) -> list:
    liste = list()    
    i = first  
    while i < end:
        liste.append(i)
        print(i)
        i += step
    return liste
    

