def inversionCount(arr):
    
    n = len(arr) 
    invCount = 0  

    for i in range(n - 1):
        for j in range(i + 1, n):
          
            # If the current element is greater than the next,
            # increment the count
            if arr[i] > arr[j]:
                invCount += 1
            
    return invCount  

if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(inversionCount(arr))
