def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        # Проходим по списку от начала до конца
        for j in range(0, n - i - 1):
            # В зависимости от направления сравниваем и меняем местами
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Запрашиваем количество чисел
    n = int(input("Введите количество чисел: "))
    numbers = []

    # Запрашиваем n чисел
    for i in range(n):
        num = float(input(f"Введите число {i+1}: "))
        numbers.append(num)

    # Определяем тип сортировки
    direction = input("Введите направление сортировки (возрастание/убывание): ").lower()
    if direction == "возрастание":
        ascending = True
    elif direction == "убывание":
        ascending = False
    else:
        print("Неверное направление сортировки, сортировка будет происходить по возрастанию (по умолчанию)")
        ascending = True

    # Сортируем числа
    bubble_sort(numbers, ascending)

    # Выводим отсортированный список
    print("Отсортированные числа:", numbers)

if __name__ == "__main__":
    main()
