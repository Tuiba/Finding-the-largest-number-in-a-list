l=[]
s=int(input("Enter the size of list"))
for i in range(s):
    x=int(input("enter list items"))
    l.append(x)
    n=l[0]
if (l[i]>n):
    n=l[i]
print("max[list]",n)
