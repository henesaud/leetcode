def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l,r):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j]  = arr[j], arr[i]

    arr[r], arr[i+1] = arr[i+1], arr[r]

    return i+1


def quicksort(arr, l, r):
    if l<r:
        pivot = partition(arr,l,r)
        quicksort(arr,l, pivot-1)
        quicksort(arr, pivot+1, r)
    return arr



class Solution(object):
    def sortArray(self, nums):
        return quicksort(nums,0 ,len(nums)-1)
