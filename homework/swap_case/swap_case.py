def swap_case(s: str) -> int:
    lista = []
    for k in s:
        if k.isupper():
            lista.append(k.lower())
        elif k.islower:
            lista.append(k.upper())
        else:
            lista.append(k)
    s = "".join(lista)
    return(s)


