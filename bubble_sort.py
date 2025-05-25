def bubble_sort(List):  
    for i in range(len(List):
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
    for i in range(len(List):
        swapped = False
        
        for j in range(0, len(List) - i - 1):
            if List[j] < List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]  # Swap
                swapped = True
                
        if not swapped:
            break
    
    return List
