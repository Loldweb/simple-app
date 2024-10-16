def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")

    choice = input("Введите номер операции (1/2/3): ")

    if choice in ['1', '2', '3']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"Результат: {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {multiply(num1, num2)}")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
