def bubble_sort(List):
    for i in range(len(List)):  # Corrected: Added closing parenthesis
        swapped = False

        for j in range(0, len(List) - i - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]  # Swap
                swapped = True

        if not swapped:
            break

    return List

#reverse
def bubble_sort_desc(List):
    for i in range(len(List)):  # Corrected: Added closing parenthesis
        swapped = False

        for j in range(0, len(List) - i - 1):
            if List[j] < List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]  # Swap
                swapped = True

        if not swapped:
            break

    return List
listed = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", bubble_sort(listed))
print("Sorted array in descending order is:", bubble_sort_desc(listed))