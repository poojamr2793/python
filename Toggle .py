def toggleChar(str):
    result = ""
    
    # Iterate over the original string
    for i in range(len(str)):
        ch = str[i]
        
        # Check the case of the character and
        # toggle accordingly
        if ch.isupper():
            result += ch.lower()
        else:
            result += ch.upper()
    return result

if __name__ == "__main__":
    str = "GeEkSfOrGeEkS"
    x = toggleChar(str)
    print(x)
