def check(arr, k, m, days):
    bouquets = 0
    cnt = 0

    # iterate through the bloom days of the flowers
    for i in range(len(arr)):
        if arr[i] <= days:
            cnt += 1
        else:

            # if the current bloom day count is greater
            # than days, update bouquets and reset count
            bouquets += cnt // k
            cnt = 0

    bouquets += cnt // k

    # check if current bouquets are greater than or
    # equal to the desired number of bouquets (m)
    return bouquets >= m


def minDaysBloom(arr, k, m):
    maxDays = max(arr)

    for d in range(maxDays + 1):
        if check(arr, k, m, d):
            return d
    return -1

if __name__ == "__main__":
    arr = [5, 5, 5, 5, 10, 5, 5]
    k = 3
    m = 2
    print(minDaysBloom(arr, k, m))
