def bubble_sort(score):  
    for i in range(len(score)):
        swapped = False
        
        for j in range(0, len(score) - i - 1):
            if score[j] > score[j + 1]:
                score[j], score[j + 1] = score[j + 1], score[j]  # Swap
                swapped = True
                
        if not swapped:
            break
    
    return score
