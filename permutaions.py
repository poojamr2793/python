def recurPermute(index, s, res):
    if index == len(s):
        res.append("".join(s)) 
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]

        recurPermute(index + 1, s, res)

        s[index], s[i] = s[i], s[index]


def findPermutation(s):
    res = []
    s = list(s)

    recurPermute(0, s, res)

    res.sort()  
    return res


if __name__ == "__main__":
    s = "AAB"
    res = findPermutation(s)

    for x in res:
        print(x, end=" ")
