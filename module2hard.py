def generate_password(n):
    # Инициализация пустой строки для пароля
    result = ""

    # Перебор всех возможных пар чисел от 1 до 20
    for i in range(1, 21):
        for j in range(i, 21):
            # Проверка, делится ли n на сумму пары
            if n % (i + j) == 0:
                # Добавление пары к результату
                result += str(i) + str(j)

    return result


# Пример использования
n = int(input("Введите число от 3 до 20: "))
print(generate_password(n))

# Проверка для всех чисел от 3 до 20
for num in range(3, 21):
    print(f"{num} - {generate_password(num)}")