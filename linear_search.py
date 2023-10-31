def linear_search(n, x):
    element = []
    for i in range(1, n + 1):
        element.append(i)
    count = 0
    flag = 0
    for i in element:
        count += 1
        if i == x:
            print("Yes!! I found my number at position: " + str(i))
            flag = 1
            break
    if flag == 0:
        print("Number is not found.")

    print("Number of iterations:", count)


linear_search(1000, 54)


def binary_search(a, x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0  # flag = 0 means that the element has not been found
    count = 0
    while first_pos <= last_pos and flag == 0:
        count += 1
        mid = (first_pos + last_pos) // 2
        if x == a[mid]:
            flag = 1
            print("The element is present at the position:", mid)
            print("the number of iterations are:", count)
            return
        else:
            if x < a[mid]:
                last_pos = mid - 1
            else:
                first_pos = mid + 1
    print("The number is not present")


a = []
for i in range(1, 1000):
    a.append(i)
binary_search(a, 54)
