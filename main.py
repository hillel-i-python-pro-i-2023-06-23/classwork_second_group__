import random


def play_game():
    # Списки слов для выбора
    word_lists = [
        {
            "name": "Фрукты",
            "words": ["яблоко", "банан", "вишня", "дыня", "ежевика", "инжир"]
        },
        {
            "name": "Овощи",
            "words": ["морковь", "помидор", "огурец", "капуста", "брокколи", "редиска"]
        }
    ]

    # Выбор списка слов пользователем
    print("Выберите категорию слов:")
    for i, word_list in enumerate(word_lists):
        print(f"{i + 1}. {word_list['name']}")
    choice = int(input("Введите номер категории: ")) - 1

    # Проверка валидности выбора категории
    if choice < 0 or choice >= len(word_lists):
        print("Неверный выбор категории. Игра завершена.")
        return

    # Выбор случайного слова из выбранной категории
    word_list = word_lists[choice]
    word = random.choice(word_list["words"])
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print("Скрытое слово:", hidden_word)
        print("Попыток осталось:", attempts)

        if "_" not in hidden_word:
            print("Поздравляю! Вы угадали слово!")
            break

        guess = input("Угадайте букву или введите слово целиком: ").lower()

        if guess == word:
            print("Поздравляю! Вы угадали слово!")
            break

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Вы уже угадывали эту букву. Попробуйте еще раз!")
            elif guess in word:
                print("Отлично! Буква есть в слове.")
                guessed_letters.append(guess)
            else:
                print("Упс! Эта буква отсутствует в слове.")
                attempts -= 1
                guessed_letters.append(guess)
        else:
            print("Упс! Неверное слово. Попробуйте еще раз!")

    if attempts == 0:
        print("Игра окончена! У вас закончились попытки. Слово было:", word)


play_game()