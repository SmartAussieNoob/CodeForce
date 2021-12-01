i=lambda:map(int,input().split())
n,k=i();l=list(i())
print(sum(0<v>=l[k-1] for v in l))
