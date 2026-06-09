def upperBound(arr, target):
    n = len(arr)

    # Compare target with each element in array
    for i in range(n):

        # If larger value found, return its index
        if arr[i] > target:
            return i

    # If all elements are smaller, return length
    return n

if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 11
    print(upperBound(arr, target))
