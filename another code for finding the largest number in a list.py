l=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    l.append(b)
l.sort()
print("Largest element is:",l[n-1])
