import math

def maclaurin_cos(x, n_terms=10):
    """
    Вычисляет значение cos(x) с помощью ряда Маклорена.

    :param x: Значение x (в радианах).
    :param n_terms: Количество итераций (по умолчанию 10).
    :return: Приближенное значение cos(x).
    """
    result = 0
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        result += term
    return result

def maclaurin_binomial(x, m, n_terms=10):
    """
    Вычисляет значение (1+x)^m с помощью ряда Маклорена.

    :param x: Значение x.
    :param m: Степень m.
    :param n_terms: Количество итераций (по умолчанию 10).
    :return: Приближенное значение (1+x)^m.
    """
    result = 1
    term = 1
    for n in range(1, n_terms):
        term *= (m - (n - 1)) / n * x
        result += term
    return result

def main():
    """
    Главное меню программы.
    """
    while True:
        print("\nВыберите функцию для вычисления:")
        print("1. cos(x)")
        print("2. (1+x)^m")
        print("3. Выход")

        choice = input("Введите номер функции (1, 2, 3): ")

        if choice == "1":
            try:
                x = float(input("Введите значение x (в радианах): "))
                result = maclaurin_cos(x)
                print(f"cos({x}) ≈ {result}")
            except ValueError:
                print("Ошибка. Введите корректное числовое значение x")

        elif choice == "2":
            try:
                x = float(input("Введите значение x: "))
                if x <= -1 or x >= 1:
                    print("Ошибка. x должен быть в пределах (-1, 1)")
                    continue
                m = float(input("Введите значение m: "))
                result = maclaurin_binomial(x, m)
                print(f"(1+{x})^{m} ≈ {result}")
            except ValueError:
                print("Ошибка. Введите корректные числовые значения x и m")

        elif choice == "3":
            print("Выход из программы")
            break

        else:
            print("Ошибка. Некорректный выбор.")

if __name__ == "__main__":
    main()
