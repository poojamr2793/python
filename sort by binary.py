def segregate0and1(arr):

    # Count 0s
    count = 0
    for x in arr:
        if x == 0:
            count += 1

    # Fill the vector with 0s until count
    for i in range(0, count):
        arr[i] = 0

    # Fill the remaining vector space with 1s
    for i in range(count, len(arr)):
        arr[i] = 1


def main():
    arr = [0, 1, 0, 1, 1, 1]

    segregate0and1(arr)
    for x in arr:
        print(x, end=" ")


if __name__ == "__main__":
    main()
