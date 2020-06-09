# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     # elements = len(arrA) + len(arrB)
#     # merged_arr = [0] * elements
#     tempA = arrA[:]
#     tempB = arrB[:]
#     merged_arr = []
#     done = False

#     # Your code here
#     while not done:
#         if tempA and tempB:
#             if tempA[0] > tempB[0]:
#                 merged_arr.append(tempB.pop(0))
#             else:
#                 merged_arr.append(tempA.pop(0))
#         else:
#             if tempA:
#                 merged_arr += tempA
#             else:
#                 merged_arr += tempB
#             done = True

#     return merged_arr

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j = 0
    k = 0

    # Your code here
    for i in range(0, len(merged_arr)):
        if j < len(arrA) and k < len(arrB):
            if arrA[j] < arrB[k]:
                merged_arr[i] = arrA[j]
                j += 1
            else:
                merged_arr[i] = arrB[k]
                k += 1
        else:
            if j < len(arrA):
                merged_arr[i] = arrA[j]
                j += 1
            else:
                merged_arr[i] = arrB[k]
                k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        middle_index = len(arr)//2
        arrA = arr[:middle_index]
        arrB = arr[middle_index:]
        return merge(merge_sort(arrA), merge_sort(arrB))


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    while start <= mid and mid + 1 <= end:
        if arr[start] > arr[mid + 1]:
            current_index = mid + 1
            while current_index > start:
                arr[current_index - 1], arr[current_index] = arr[current_index], arr[current_index - 1]
                current_index -= 1
            # removed_num = arr.pop(mid + 1)
            # arr.insert(start, removed_num)
            start += 1
            mid += 1
        else:
            start += 1
  
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        middle = (l + r)//2

        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        merge_in_place(arr, l, middle, r)

    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr