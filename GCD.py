def gcd(a, b):
    
    # Everything divides 0
    if(a==0 or b==0):
        return max(a, b)
        
    # Find Minimum of a and b
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return gcd of a and b
    return result


if __name__ == '__main__':
    a = 20
    b = 28
    print(gcd(a, b))
