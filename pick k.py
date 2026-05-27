import sys

def helper(i, remk, prev, arr, k, memo):
    if remk == k:
        return sys.maxsize

    if i == len(arr):
        return -1

    if memo[i][remk][prev + 1] != -2:
        return memo[i][remk][prev + 1]

    skip = helper(i + 1, remk, prev, arr, k, memo)

    diff = sys.maxsize \
        if prev == -1 else abs(arr[i] - arr[prev])
    next_val = helper(i + 1, remk + 1, i, arr, k, memo)
    take = -1 if next_val == -1 else min(diff, next_val)

    memo[i][remk][prev + 1] = max(skip, take)
    return memo[i][remk][prev + 1]

def maxMinDiff(arr, k):
    arr.sort()
    n = len(arr)

    memo = [[[-2] * (n + 1) \
        for _ in range(k + 1)] for _ in range(n + 1)]

    return helper(0, 0, -1, arr, k, memo)



if __name__ == "__main__":
    arr = [1, 4, 9, 0, 2, 13, 3]
    k = 4
    print(maxMinDiff(arr, k))
