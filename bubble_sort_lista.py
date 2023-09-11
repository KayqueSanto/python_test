lista = [1, 26, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 46, 
         37, 39, 41, 43, 45, 47, 2, 4, 6, 8, 10, 12, 14, 16, 
         18, 20, 22, 24, 3, 28, 30, 32, 34, 36, 38, 40, 42, 44, 35, 48, 50]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
print(bubble_sort(lista))
