def totHammingDist(arr):
    count = 0
    n = len(arr)

    # Loop through all unique pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):

            # For each bit position from 0 to 30 
            for k in range(31):

                # If bit k is set in arr[i] and not in arr[j]
                if (arr[i] & (1 << k)) and not (arr[j] & (1 << k)):
                    count += 1

                # If bit k is not set in arr[i] and is set in arr[j]
                elif not (arr[i] & (1 << k)) and (arr[j] & (1 << k)):
                    count += 1

    return count

if __name__ == "__main__":
    arr = [4, 14, 4, 14]
    ans = totHammingDist(arr)
    print(ans)
