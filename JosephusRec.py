def josephusRec(person, k, index):
    
    # Base case , when only one person is left
    if len(person) == 1:
        return person[0]

    # find the index of first person which will die
    index = (index + k) % len(person)

    # remove the first person which is going to be killed
    person.pop(index)

    # recursive call for n-1 persons
    return josephusRec(person, k, index)


def josephus(n, k):
    
    # The index where the person which will die
    index = 0

    person = []

    # fill the person vector
    for i in range(1, n + 1):
        person.append(i)

    return josephusRec(person, k, index)

if __name__ == "__main__":
     n = 7
     k = 3
    
    # (k-1)th person will be killed
     k -= 1
     print(josephus(n, k))
