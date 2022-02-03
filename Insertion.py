def insertion_sort(array):


    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue

array = [7,3,5,8,2,9,4,15,6]
insertion_sort(array)
print("sorted array: " + str(array))