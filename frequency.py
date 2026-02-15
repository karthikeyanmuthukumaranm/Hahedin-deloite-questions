arr=['a','a','b','b','c','c']
count=1
for i in range(len(arr)):
    if (i<len(arr)-1 and arr[i]==arr[i+1]):
        count+=1
    else:
        print(arr[i]+str(count), end='')
        count=1
