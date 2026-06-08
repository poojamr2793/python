def primeFactor(n):
    ans = []
    
    # Loop from 2 to n
    for i in range(2, n+1):
        
        # n % i == 0 means n is divisible by i
        while n % i == 0 and n > 0:
            ans.append(i) 
            
             # divide n by i to remove this factor
            n = n // i
    return ans

if __name__ == "__main__":    

    n = 18
    ans = primeFactor(n)
    for x in ans:
        print(x, end=' ')
