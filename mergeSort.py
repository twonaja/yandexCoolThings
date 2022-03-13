def merge_sort(array: list):
    if len(array) == 1:  # базовый случай рекурсии
        return array
    half_len_arr = len(array) // 2
    len_arr = len(array)
    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: half_len_arr])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[half_len_arr: len_arr])

    # заводим массив для результата сортировки
    result = [] * len_arr

    # сливаем результаты
    l, r = 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result.append(left[l])  # перенеси оставшиеся элементы left в result
        l += 1
    while r < len(right):
        result.append(right[r])  # перенеси оставшиеся элементы right в result
        r += 1
    return result