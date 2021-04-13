def setdict(l):
    d={}
    for i in l:
        try:
            d[i]+=1
        except KeyError:
            d[i]=1
    return d