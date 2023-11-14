a=[9,6,4,8,10,7]
max=a[0]
for i in range(1,len(a)):
    if max<a[i]:
        max=a[i]
print(max)