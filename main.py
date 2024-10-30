def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания, были ли изменения
        swapped = False
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

def main():
    # Запрашиваем количество чисел
    n = int(input("Введите количество чисел: "))
    numbers = []

    # Запрашиваем n чисел
    for i in range(n):
        num = float(input(f"Введите число {i+1}: "))
        numbers.append(num)

    # Сортируем числа
    bubble_sort(numbers)

    # Выводим отсортированный список
    print("Отсортированные числа:", numbers)

if __name__ == "__main__":
    main()
