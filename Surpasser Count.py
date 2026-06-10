def findSurpasser(arr):
    n = len(arr)
  
    # List to store surpasser counts
    res = [0] * n
    
    for i in range(n):
        
        # Find surpasser for arr[i]
        count = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1
        
        res[i] = count
    return res

if __name__ == "__main__":
    arr = [2, 7, 5, 3, 8, 1]
    result = findSurpasser(arr)
    for val in result:
        print(val, end=' ')
