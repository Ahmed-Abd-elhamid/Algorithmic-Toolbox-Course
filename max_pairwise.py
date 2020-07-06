def max(arr):
    maxIndex1 = 0
    maxIndex2 = 0
    
    for i in range(len(arr)):
        if arr[maxIndex1] < arr[i]:
            maxIndex1 = i
    # print(maxIndex1)

    for i in range(len(arr)):
        if ((i != maxIndex1 and arr[maxIndex2] < arr[i]) or maxIndex1 == maxIndex2):
            maxIndex2 = i
    # print(maxIndex2)

    return arr[maxIndex1]*arr[maxIndex2]


size =int(input()) #take the size
arr = list(map(int, input().split()[:size])) #arr with fixed size

print(max(arr))
