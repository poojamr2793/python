def subarraySum(arr):
    
    n = len(arr)
    result = 0

    # Computing sum of subarrays using the formula
    for i in range(n):
        result += arr[i] * (i + 1) * (n - i)

    # Return the sum of all subarrays
    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr))
