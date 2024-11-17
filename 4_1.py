from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Тестовые вызовы функций
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Вывод результатов на экран
print(result1)  # Ожидаем 23.0
print(result2)  # Ожидаем 'Ошибка'
print(result3)  # Ожидаем 7.0
print(result4)  # Ожидаем inf
