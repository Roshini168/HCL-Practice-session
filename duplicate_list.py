b=list(map(int,input().split()))
c=[]
for i in range (len(b)):
    if b[i] not in b[i+1:]:
        c.append (b[i])
print(c)
