n=int(input())
d={}
for i in range(n):
  s=input()
  d[s]=d.get(s,0)+1
K=int(input())
l=[]
for k,v in d.items():
  if v==1:
    l.append(k)
if 0<len(l)>=K:
  print(l[K-1])
else:
  print(-1)


