import random
import string


class PasswordGenerator:
    def __init__(self):
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = string.punctuation

    def generate_password(self, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
        characters = ""

        if use_lowercase:
            characters += self.lowercase_letters
        if use_uppercase:
            characters += self.uppercase_letters
        if use_digits:
            characters += self.digits
        if use_special:
            characters += self.special_characters

        if not characters:
            print("Выберите хотя бы один тип символов.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password


def main():
    password_generator = PasswordGenerator()

    print("Добро пожаловать в генератор паролей!")

    while True:
        print("\n1. Сгенерировать пароль")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            length = int(input("Введите длину пароля: "))
            use_lowercase = input("Использовать строчные буквы? (y/n): ").lower() == 'y'
            use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
            use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
            use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'

            password = password_generator.generate_password(
                length=length,
                use_lowercase=use_lowercase,
                use_uppercase=use_uppercase,
                use_digits=use_digits,
                use_special=use_special
            )

            if password:
                print(f"Ваш новый пароль: {password}")
        elif choice == "0":
            print("Спасибо за использование генератора паролей. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
