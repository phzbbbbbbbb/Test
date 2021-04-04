# Quick Sort
def Partition(list, low, high):
    pivot = list[low]
    while low < high:
        while low < high and list[high] > pivot:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < pivot:
            low += 1
        list[high] = list[low]
    list[low] = pivot
    return low

def Partition_2(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1

def QuickSort(list, low, high):
    if low < high:
        p = Partition_2(list, low, high)

        QuickSort(list, low, p - 1)
        QuickSort(list, p + 1, high)


if __name__ == '__main__':
    array = list(map(int, input().strip().split()))
    QuickSort(array, 0, len(array) - 1)
    print(array)

# 2 8 7 1 3 5 6 4