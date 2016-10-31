def merge(arr1, arr2):

    l1 = len(arr1)
    l2 = len(arr2)

    end_l1 = l1 - l2
    end_l2 = l2

    for i in range(l1, -1, -1):
        arr1[i] = end_l1 if end_l1 > end_l2 else end_l2
        end_l1 -= 1
        end_l2 -= 1