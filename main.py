import random
import string


class PasswordGenerator:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def generate_password(self):
        password = ""

        for word in self.words:
            # Додаємо першу літеру кожного слова до паролю
            password += word[0]

        # Генеруємо решту паролю з випадкових символів
        remaining_length = 10 - len(self.words)
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=remaining_length))
        password += random_chars

        return password

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for word in self.words:
                file.write(word + '\n')

    def save_password_to_file(self, filename, password):
        with open(filename, 'w') as file:
            file.write(password + '\n')


# Приклад використання класу:
generator = PasswordGenerator()

# Введення слів від користувача
while True:
    word = input("Введіть слово (або Enter для завершення): ")
    if word == "":
        break
    generator.add_word(word)

# Генерація пароля та виведення результату
password = generator.generate_password()
print("Згенерований пароль:", password)

generator.save_password_to_file('passwords.txt', password)