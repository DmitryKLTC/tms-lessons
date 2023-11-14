a=[6,4,8,10,2,0,1]
b=False
for i in range(len(a)):
    if a[i]==0:
        b=True
if b:
    print('yes')
else:
    print('no')



a=[6,4,8,10,2,0,1]
for i in range(len(a)):
    if a[i]==0:
        b=True
        print('yes')
        break
    if i == len(a)-1:
        print('no')