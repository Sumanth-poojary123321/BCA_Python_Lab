n=int(input("Enter the total number of element: "))
glist=[]

for i in range(n):
    glist.append(input(f"Enter the element no {i+1}"))

ulist=[]
for item in glist:
    if glist.count(item)==1:
        ulist.append(item)
print(glist)
if len(ulist)==0:
    print("no unique number ")
print(ulist)