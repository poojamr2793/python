def searchInsertK(arr, k):  
    for i in range(len(arr)):  
        # if k is found or needs to be inserted 
        # before arr[i]
        if arr[i] >= k:  
            return i  

    # if k is greater than all elements,
    # insert at the end
    return len(arr)  

if __name__ == "__main__":  
    arr = [1, 3, 5, 6]  
    k = 5  
    print(searchInsertK(arr, k))
