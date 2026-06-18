def removeSpaces(s):
    n = len(s)
    i = 0
    itr = 0

    # convert to list 
    # (strings are immutable in Python)
    s = list(s)

    # Iterate through the string
    while i < n:
        
        # Check if current character 
        # is not a space
        if s[i] != ' ':
            
            # Copy the non-space character 
            # to the new string
            s[itr] = s[i]
            itr += 1
        i += 1

    # Return only the modified part of the string 
    # without any extra characters
    return "".join(s[:itr])


if __name__ == "__main__":
    s = "g  eeks   for ge  eeks  "
    print(removeSpaces(s))
