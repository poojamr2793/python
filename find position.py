def findPosition(n):
    
    # Check if n has exactly one set bit
    if n == 0 or (n & (n - 1)) != 0:
        return -1
    
    pos = 1
    val = 1
    while (val & n) == 0:
        # Shifting left
        val = val << 1
        pos += 1
    return pos

# Driver Code
if __name__ == "__main__":
    n = 2
    print(findPosition(n))
