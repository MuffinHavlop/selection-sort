def selection_sort(list):
    for i in range(0, len(list)-1):
        current_min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[current_min]:
                current_min = j
        
        list[current_min], list[i] = list[i], list[current_min]
    return list

list = [2, 4, 6, 3, 1, 5]
print(selection_sort(list))