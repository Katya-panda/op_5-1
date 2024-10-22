# запрашиваем строку у пользователя
user_input = input("Введите строку: ")
# вычисляем длину строки
length = len(user_input)
# определяем гласные буквы
vowels = "уеёыаоэяиюУЕЫАОЭЯИЮ"
# подсчитываем количество гласных в строке
vowel_count = sum(1 for char in user_input if char in vowels)
# подсчитываем количество согласных: все буквы, которые не гласные и являются буквами русского алфавита
consonant_count = sum(1 for char in user_input if char.isalpha() and char not in vowels)
# выводим результаты
print(f"Длина строки: {length}")
print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")
