from math import sqrt

def square_eq_solver(a, b, c):
    result = []
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return result
    elif discriminant == 0:
        result.append(-b / (2 * a))
    else:
        result.append((-b + sqrt(discriminant)) / (2 * a))
        result.append((-b - sqrt(discriminant)) / (2 * a))
    return result


def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index + 1} равен {value:.2f}')
    else:
        print('Уравнение с заданными параметрами не имеет действительных корней')


def is_palindrome_iterative(s):
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    for i in range(len(s_clean) // 2):
        if s_clean[i] != s_clean[-(i + 1)]:
            return False
    return True


def compute_factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main_first_script():
    a, b, c = map(float, input('Пожалуйста, введите три числа через пробел: ').split())
    result = square_eq_solver(a, b, c)
    show_result(result)


def main_second_script():
    s = input("Введите строку для проверки на палиндром: ")
    if is_palindrome_iterative(s):
        print("Строка является палиндромом")
    else:
        print("Строка не является палиндромом")


def main_third_script():
    s = input("Введите число для расчета факториала: ")
    n = int(s)
    if n < 0:
        print("Ошибка: факториал отрицательного числа не определён.")
    else:
        print(f"Факториал числа {s} равен {compute_factorial(n)}")


def main():цццц
    num = input("Введите номер скрипта: 1-квадратное уравнение, 2-палиндром, 3-факториал: ")
    if num == "1":
        main_first_script()
    elif num == "2":
        main_second_script()
    elif num == "3":
        main_third_script()
    else:
        print("Выход из программы.")


if __name__ == '__main__':
    main()
