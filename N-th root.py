def power(base, expo, limit):
    result = 1
    for _ in range(expo):
        result *= base
        
        if result > limit:  
            return result
    return result

# function to find the 
# n-th root of m
def nthRoot(n, m):
    # n-th root of 0 is 0
    if m == 0:
        return 0

    # If n is 1, the answer 
    # is m itself
    if n == 1:
        return m

    # binary search to find 
    # the integer root
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2

        # compute mid^n and compare it with m
        val = power(mid, n, m)

        if val == m:
            return mid  
        elif val < m:
            low = mid + 1  
        else:
            high = mid - 1 

    return -1

if __name__ == "__main__":
    n = 3
    m = 27
    
    result = nthRoot(n, m)
    print(result)
