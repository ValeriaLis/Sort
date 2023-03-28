def merge_sort(list1):
    if len(list1) > 1:
        middle = len(list1) // 2 #находим середину нашего массива 
        left_half = list1[:middle]
        right_half = list1[middle:]

        # рекурсивно вызываем функцию для левой и правой части массива
        merge_sort(left_half)
        merge_sort(right_half)

        # ниже действия для соединения нашего массива
        i = 0  # индекс для левого подсписка
        j = 0  # индекс для правого подсписка
        k = 0  # индекс для объединенного подсписка

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list1[k] = left_half[i]
                i += 1
            else:
                list1[k] = right_half[j]
                j += 1
            k += 1

        # добавляем все остальные элементы с левого и правого подсписка
        while i < len(left_half):
            list1[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list1[k] = right_half[j]
            j += 1
            k += 1

# пример искользования
list1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48] 
merge_sort(list1)
print(list1)
