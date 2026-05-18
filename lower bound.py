def lowerBound(arr, target):
    n = len(arr)

    # compare target with each element in array
    for i in range(n):
      
        # if equal or larger value found
        # return its index
        if arr[i] >= target:
            return i

    # if all elements are smaller, return length
    return n

if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9
    print(lowerBound(arr, target))
