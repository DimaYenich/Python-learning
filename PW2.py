#1
def sum_of_non_negative_numbers():
    sum = 0
    numbers = [9, 2, -3, -5, 1, 8]
    for number in numbers:
        if(number>=0):
            sum += number;
    print(sum)

#2
def reverve_string():
    text = input("Введіть рядок для реверсу:")
    print(text[::-1])

#3
def reverse_sentence():
    sentence = input("Введіть речення для реверсу").split(' ')
    reverse_sentence = ''
    for word in sentence:
        reverse_sentence += word[::-1]+' '
    print(reverse_sentence)

#4
def is_palidrome():
    word = input("Введіть слово для перевірки на паліндром:")
    if word == word[::-1]:
        print(f"Слово {word} є паліндромом.")
    else:
        print(f"Слово {word} не є паліндромом.")
#5       
def find_min_max():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    rows, cols = len(matrix), len(matrix[0])
    min_element = matrix[0][0]
    max_element = matrix[0][0]
    min_row, min_col = 0, 0
    max_row, max_col = 0, 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row, min_col = i, j
            elif matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_row, max_col = i, j
    for row in matrix:
        print(row)
    print(f"Координати мінімального числа: {min_row, min_col} "
          f"\nКоординати максимального числа: {max_row, max_col}")

#6
def count_unique_characters():
    input_string = input("Введіть рядок для підрахунку унікальних символів:")
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    unique_characters = list(char_count.keys())
    print(f"Унікальні символи у рядку '{input_string}': {unique_characters}")
    print("Кількість входжень кожного унікального символу:")
    for char in unique_characters:
        print(f"'{char}': {char_count[char]}")

#7
def dict_to_tuples():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    print(f"Словник: {dictionary}")
    tuple_list = list(dictionary.items())
    print(f"Список кортежів: {tuple_list}")


dict_to_tuples()