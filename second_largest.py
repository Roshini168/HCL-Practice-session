b=list(map(int,input().split()))
c=list(set(b))
if len(c)<2:
    print(-1)
else:
    d=sorted(c)[-2]
    print(b.index(d))
