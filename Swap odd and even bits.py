def swapBits(n):
    for i in range(0, 32, 2):

        # Find i th bit
        i_bit = (n >> i) & 1

        # Find i+1 th bit
        i_1_bit = (n >> (i + 1)) & 1

        # Remove i_bit
        n = n - (i_bit << i)
        
        # Remove i+1 th bit
        n = n - (i_1_bit << (i + 1))
        
        # Put i_bit at i+1 location
        n = n + (i_bit << (i + 1))
        
        # Put i+1 bit at i location
        n = n + (i_1_bit << i)

    return n

if __name__ == "__main__":
    n = 23
    print(swapBits(n))
