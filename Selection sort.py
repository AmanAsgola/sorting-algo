arr=[5,4,3,2,1]
n=len(arr)
for i in range(n-1):
    minx=i
    for j in range(i,n):
        if arr[j]<arr[minx]:
            minx=j
    arr[i],arr[minx]=arr[minx],arr[i]
print(arr)
