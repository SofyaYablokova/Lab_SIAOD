#Башни
t=int(input())
x=list(map(int,input().split()))
y=set(x)
a=[]
for i in y:
    a.append(x.count(i))
print(max(a),len(set(x)))