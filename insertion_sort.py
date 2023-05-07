import time
def insort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=i
        for j in range (i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
arr=[5,8,6,9,7,2]
print("before sort:",arr)
s=time.time()
insort(arr)
e=time.time()
print("after sorting:",arr)
print(e-s)