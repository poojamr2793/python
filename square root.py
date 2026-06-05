def floorSqrt(n):
    
    # start iteration from 1 until the 
    # square of a number exceeds n
    res = 1
    while res * res <= n:
        res += 1
    
    # return the largest integer whose 
    # square is less than or equal to n
    return res - 1

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))
