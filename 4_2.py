def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызов test_function
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")


''' 1)  Внутри test_function создается локальная функция inner_function.
    2)  inner_function вызывается внутри test_function, что выполняется успешно.
    3)  При попытке вызвать inner_function вне test_function возникает ошибка NameError,
     так как inner_function имеет локальную область видимости и недоступна за пределами test_function.'''