import re 

class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None, domain="itcollege.lviv.ua") -> None:
        """Ініціалізація класу
        """
        initial_name = (name if name is not None else self.anonymous_user().name).capitalize() 

        # 1. ВИКЛИКАЄМО МЕТОД ВАЛІДАЦІЇ
        self._validate_name(initial_name)

        self.name = initial_name
        self.domain = domain
        
        # Умова для встановлення домену gmail.com для Marta та Anonymous
        if self.name in ["Marta", "Anonymous"]:
            self.domain = "gmail.com"
            
        MyName.total_names += 1  # modify class variable
        self.my_id = self.total_names

    # МЕТОД ДЛЯ ПЕРЕВІРКИ ІМЕНІ
    def _validate_name(self, name: str):
        """Перевіряє, чи містить ім'я лише літери, пробіли та дефіси.
        """
        if re.search(r'[^a-zA-Zа-яА-ЯіІїЇєЄ\s\-]', name):
            raise ValueError("Ім'я може містити лише літери та пробіли/дефіси!")
        
    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    @property
    def full_name(self) -> str:
        """Class property
        return: Повертає повну інформацію про користувача: "User #<id>: <name> (<email>)"
        """
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@{self.domain}" 

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    def save_to_file(self, filename="users.txt"):
        """Метод екземпляра, який додає рядок із записом (full_name) у вказаний файл.
        Використовує режим 'a' (append) для додавання.
        """
        record = self.full_name
        try:
            # Використовуємо 'with open' для безпечної роботи з файлом
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(record + '\n') # Додаємо рядок і перехід на новий рядок
            print(f"   [File Save] Інформація про {self.name} успішно додана до {filename}")
        except IOError as e:
            print(f"   [File Error] Не вдалося записати у файл {filename}: {e}")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"

    def count_letters(self) -> int:
        """Instance method to count the number of letters in the name
        """
        return len(self.name)


print("Розпочинаємо створювати обєкти та записувати їх у файл!")

# Очищуємо файл перед початком, щоб уникнути накопичення старих даних
try:
    with open("users.txt", 'w', encoding='utf-8') as f:
        f.write("--- Новий сеанс запису користувачів ---\n")
except IOError:
    pass

names_to_test = ("Bohdan", "Marta", "artem", None, "Oleg123", "Анна-Марія")
all_names = {}

for name in names_to_test:
    try:
        obj = MyName(name)
        key = obj.name if name is not None else name
        all_names[key] = obj
        
        # ⭐ ВИКЛИК НОВОГО МЕТОДУ
        obj.save_to_file()

        print(f"""{">*<"*20}
✅ Успіх: Об'єкт створено. Повна інформація: {obj.full_name} 
Email: {obj.my_email}
{"<*>"*20}""")
        
    except ValueError as e:
        print(f"""{">X<"*20}
❌ Помилка: Не вдалося створити об'єкт з вхідним значенням '{name}'.
Причина: {e}
{">X<"*20}""")
        
print(f"\nWe are done. Total successful objects created: {MyName.total_names}")
print(f"Перевірте файл 'users.txt' у вашій директорії.")