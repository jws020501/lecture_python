arr = [3, 1, 4, 1, 5, 9]
#(숙제) 리스트 getIndex
def getIndex(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1
print(getIndex(arr, 4))
# getMax
def getMax(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
print(getMax(arr)) 
# getMin
def getMin(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value
print(getMin(arr))

# countGT
def countGT(lst, threshold):
    count = 0
    for num in lst:
        if num > threshold:
            count += 1
    return count
print(countGT(arr, 3))
# sumList
def sumList(arr):
    total = 0
    for num in arr:
        total += num
    return total
print(sumList(arr))     
# swapList
def swapList(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return arr
print(swapList(arr))

