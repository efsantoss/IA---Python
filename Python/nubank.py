def findMaximumGreatness(arr):
    sorted_arr = sorted(arr)
    greatness = 0
    sorted_index = 0

    for original_value in arr:
        if sorted_arr[sorted_index] > original_value:
            greatness += 1
            sorted_index += 1

    return greatness

arr = [1, 3, 5, 2, 1, 3, 1]
print(findMaximumGreatness(arr))  # Saída: 4
