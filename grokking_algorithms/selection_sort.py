def findSmallest(arr):
    smallest = arr[0] #armazena o menor valor
    smallest_index = 0 #armazena o indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): #ordena um array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) #encontra o menor elemento do array, e o adiciona ao novo array
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))
        