def merge(arr1,arr2):
    arr3 = arr1+ arr2

    for i in range(len(arr3)):
        for j in range(i+1, len(arr3)):
            current = arr3[i]

            if current > arr3[j]:
                arr3[i], arr3[j] = arr3[j], arr3[i]


    return arr3;



arr1 = [1,3,5]
arr2=[2,4,6]

print(merge(arr1,arr2))