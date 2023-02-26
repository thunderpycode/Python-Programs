def bingap(N):
    gap=0
    mg=0
    oneslist=[]
    b=bin(N)[2:]
    print(b)
    l=list(b)
    print(l)
    
    for i in range(0,len(l)):
        if l[i] == "1":
            oneslist.append(i)
    print(oneslist)
    for j in range(len(oneslist)-1):
        gap = (oneslist[j+1] - oneslist[j] - 1)
        if gap > mg:
            mg = gap
    return mg
N = 1073741825
g = bingap(N)
print(g)

