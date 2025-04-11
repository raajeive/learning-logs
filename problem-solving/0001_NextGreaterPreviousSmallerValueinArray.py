def nextGreater(arr):
    stack = []
    res = [-1] * len(arr)
    stack.append(arr[-1])
    for index in range(len(arr) - 2, -1, -1):
        while len(stack) > 0 and stack[-1] < arr[index]:
            stack.pop()
        if len(stack) > 0 and stack[-1] > arr[index]:
            res[index] = stack[-1]
        stack.append(arr[index])
    return res


def previousSmaller(arr):
    stack = []
    res = [-1] * len(arr)
    stack.append(arr[0])
    for index in range(1, len(arr)):
        while len(stack) and stack[-1] > arr[index]:
            stack.pop()
        if len(stack) > 0 and stack[-1] < arr[index]:
            res[index] = stack[-1]
        stack.append(arr[index])
    return res


def nextsmaller(arr):
    stack = []
    res = [-1] * len(arr)
    stack.append(arr[-1])
    for index in range(len(arr) - 2, -1, -1):
        while len(stack) > 0 and stack[-1] > arr[index]:
            stack.pop()
        if len(stack) > 0 and stack[-1] < arr[index]:
            res[index] = stack[-1]
        stack.append(arr[index])
    return res

print(nextGreater([6, 8, 0, 1, 3]))
# [8, -1, 1, 3, -1]

print(nextGreater([11, 13, 21, 3]))
# [13, 21, -1, -1]

print(previousSmaller([2, 5, 3, 7, 8, 1, 9]))
# [-1, 2, 2, 3, 7, -1, 1]

print(previousSmaller([5, 7, 4, 9, 8, 10]))
# [-1, 5, -1, 4, 4, 8]

print(nextsmaller([6, 8, 0, 1, 3]))
# [0, 0, -1, -1, -1]

print(nextsmaller([11, 13, 21, 3]))
# [3, 3, 3, -1]

print(nextsmaller([4, 8, 5, 2, 25]))
# [2, 5, 2, -1, -1]
