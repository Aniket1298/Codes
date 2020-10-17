k=6
for z in range(1,64):
    i=12
    for j in range(1,64):
        if (k^i^j)>=min(i,j):
            print k^i^j,i,j
            print bin(k)[2:]
            print bin(i)[2:]
            print bin(i)[2:]
        
        