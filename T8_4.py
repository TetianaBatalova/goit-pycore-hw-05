from functools import wraps
from typing import Callable, List, Dict, Tuple

# 1. Декоратор для обробки помилок


def input_error(func: Callable) -> Callable:
    """
    Декоратор, що обробляє стандартні винятки введення користувача.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name please."
    return inner

# 2. Функції-обробники команд (Handlers)


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Розбирає введений рядок на команду та аргументи."""
    if not user_input.strip():
        return "invalid", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає контакт. ValueError виникне, якщо в args менше 2 елементів."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Змінює контакт. KeyError виникне, якщо імені немає в словнику."""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Показує номер. IndexError виникне, якщо args порожній."""
    name = args[0]
    return contacts[name]  # Тут KeyError виникне автоматично, якщо імені немає


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """Показує всі контакти."""
    if not contacts:
        return "No contacts stored."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# 3. Головний цикл бота


def main() -> None:
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
