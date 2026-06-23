def URLify(s) :
    n = len(s)
    
    # Use a list to mimic 
    # push_back behavior efficiently
    result = []
    
    for i in range(n):
        
        # if " " is encountered, 
        # append "%20" to the list
        if s[i] == ' ':
            result.append('%')
            result.append('2')
            result.append('0')
        
        # else append the current 
        # character.
        else:
            result.append(s[i])
            
    # Join the list into a single string at the end
    return "".join(result)

if __name__ == "__main__":
    s = "i love programming"
    print(URLify(s))
