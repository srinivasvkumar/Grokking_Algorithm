def sumarr(arr):
    sum=0
    array_size=len(arr)
    for i in range(0,array_size):
     if (i <= array_size):
       sum=sum+arr[i]
    return sum


print("Sum of array is:", sumarr([1,2,3,4,5]))


