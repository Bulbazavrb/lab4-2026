"""
Лабораторна робота № 4: Обробка рядків та регулярні вирази
Варіант: 12
Тема: Аналіз кулінарних рецептів та витяг ШІ-систем правопорядку NeoTerra
Студент: Шульга Дмитро Ігорович
Група: 12
"""

import os
import re
from collections import Counter
from typing import Any, Dict, List


# === Функції для базових операцій з рядками ===

def find_substring(text: str, substring: str) -> int:
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    return text.find(substring)


def replace_substring(text: str, old: str, new: str) -> str:
    """
    Заміна підрядка в тексті.
    """
    return text.replace(old, new)


def split_text(text: str, delimiter: str = ' ') -> List[str]:
    """
    Розділення тексту за роздільником.
    """
    return text.split(delimiter)


def format_string_f(name: str, age: int) -> str:
    """
    Форматування рядка з використанням f-string.
    Приклад: "Мене звати Alice і мені 30 років."
    """
    return f"Мене звати {name} і мені {age} років."


def format_string_method(name: str, age: int) -> str:
    """
    Форматування рядка з використанням методу .format().
    Приклад: "Мене звати Bob і мені 25 років."
    """
    return "Мене звати {} і мені {} років.".format(name, age)


# === Функції для роботи з регулярними виразами ===

def extract_emails(text: str) -> List[str]:
    """
    Витяг email адрес з тексту.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


def validate_phone_number(number: str) -> bool:
    """
    Валідація українського телефонного номера.
    Підтримує формати: +380XXXXXXXXX, 380XXXXXXXXX, 0XXXXXXXXX.
    """
    pattern = r'^\+?3?8?(0\d{9})$'
    return bool(re.match(pattern, number.strip()))


def extract_hashtags(text: str) -> List[str]:
    """
    Витяг хештегів з тексту.
    """
    pattern = r'#\w+'
    return re.findall(pattern, text)


def extract_mentions(text: str) -> List[str]:
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    pattern = r'@\w+'
    return re.findall(pattern, text)


# === Функції для аналізу тексту ===

def count_words(text: str) -> int:
    """
    Підрахунок кількості слів у тексті.
    """
    return len(re.findall(r'\b\w+\b', text))


def count_sentences(text: str) -> int:
    """
    Підрахунок кількості речень у тексті.
    """
    return len(re.findall(r'[.!?]+', text))


def word_frequency(text: str) -> Counter:
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


def analyze_text(text: str) -> Dict[str, Any]:
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    words_cnt = count_words(text)
    sentences_cnt = count_sentences(text)
    freq = word_frequency(text)
    emails = extract_emails(text)
    hashtags = extract_hashtags(text)
    mentions = extract_mentions(text)

    return {
        'word_count': words_cnt,
        'sentence_count': sentences_cnt,
        'word_frequency': freq.most_common(5),
        'emails': emails,
        'hashtags': hashtags,
        'mentions': mentions
    }


def format_analysis_results(results: Dict[str, Any]) -> str:
    """
    Форматування результатів аналізу для зручного виведення.
    """
    output = "Результати аналізу тексту:\n\n"
    output += f"Кількість слів: {results.get('word_count', 0)}\n"
    output += f"Кількість речень: {results.get('sentence_count', 0)}\n\n"
    output += "Топ-5 найчастіших слів:\n"
    for word, count in results.get('word_frequency', []):
        output += f"  {word}: {count}\n"
    output += f"\nЗнайдені email адреси: {', '.join(results.get('emails', []))}\n"
    output += f"Знайдені хештеги: {', '.join(results.get('hashtags', []))}\n"
    output += f"Знайдені згадування: {', '.join(results.get('mentions', []))}\n"
    return output


# === Функції для Варіанту 12 ===

def extract_variant_data(text: str, variant_pattern: str) -> List[str]:
    """
    Вилучає дані з тексту за допомогою регулярного патерну варіанту.
    """
    return re.findall(variant_pattern, text)


def extract_law_enforcement_ai(text: str) -> List[str]:
    """
    Вилучає назви ШІ-систем правопорядку міста NeoTerra 3000 (Варіант 12).
    Патерн розпізнає назви типу 'LawForce-AI', 'Guardian-AI' тощо.
    """
    pattern = r'\b[A-Za-z]+(?:[A-Z][a-z]+)*-AI\b'
    return re.findall(pattern, text)


def parse_recipe_details(recipe_text: str) -> Dict[str, Any]:
    """
    Аналіз кулінарного рецепту (Варіант 12):
    витяг інгредієнтів з кількістю та пронумерованих кроків інструкції.
    """
    # Шаблон: Назва інгредієнта — Число Одиниця (напр. 'Борошно - 250 г', 'Цукор: 2 ст. л.')
    ingredient_pattern = r'[-*•]?\s*([А-Яа-яA-Za-z\s]+)\s*[-:]\s*(\d+(?:[.,]\d+)?\s*(?:г|кг|мл|л|шт|ст\.\s*л\.|ч\.\s*л\.))'
    ingredients = re.findall(ingredient_pattern, recipe_text)

    # Шаблон: Нумеровані інструкції (напр. '1. Замісити тісто.')
    step_pattern = r'(?:^|\n)\s*\d+[\.)]\s*([^\n]+)'
    steps = re.findall(step_pattern, recipe_text)

    return {
        'ingredients': [{'name': name.strip(), 'quantity': qty.strip()} for name, qty in ingredients],
        'steps': [step.strip() for step in steps]
    }


# === Головна частина програми ===

def read_file_content(filepath: str) -> str:
    """
    Читає вміст файлу. Якщо файл не знайдено, перевіряє суміжні відносні шляхи.
    """
    paths_to_try = [
        filepath,
        os.path.join(os.path.dirname(__file__), 'data', 'neoterra_text.txt'),
        os.path.join('data', 'neoterra_text.txt'),
        'neoterra_text.txt'
    ]

    for path in paths_to_try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()

    # Якщо файлу немає на диску, використовуємо стандартний текст NeoTerra 3000
    return (
        "Вітаємо вас у NeoTerra 3000, де технології та природа зливаються воєдино! "
        "Правопорядок підтримується за допомогою ШІ-системи LawForce-AI, яка аналізує дані "
        "з мільйонів сенсорів по всьому місту. Також розгорнуто патрульну систему Guardian-AI. "
        "Email для зв'язку: support@neoterra3000.earth, admin@neoterra.gov. "
        "Телефон служби підтримки: +380441234567. #NeoTerra #FutureCity @MayorAI @PoliceAI"
    )


def main():
    print("=" * 60)
    print("ТЕКСТОВИЙ АНАЛІЗАТОР ТА ОБРОБКА РЯДКІВ (Варіант 12)")
    print("=" * 60)

    text_filepath = 'src/data/neoterra_text.txt'
    text_to_analyze = read_file_content(text_filepath)

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація українського телефону")
            print("3. Вилучити ШІ-системи правопорядку (Варіант 12)")
            print("4. Парсинг рецепту (Варіант 12: інгредієнти, кількість, кроки)")
            print("5. Вихід")
            choice = input("Ваш вибір (1-5): ").strip()

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print("\n" + format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації (+380XXXXXXXXX): ")
                if validate_phone_number(phone):
                    print("-> Номер телефону валідний!")
                else:
                    print("-> Номер телефону невалідний.")

            elif choice == '3':
                # Регулярний вираз для пошуку ШІ-систем правопорядку (LawForce-AI)
                pattern = r'\b[A-Za-z]+(?:[A-Z][a-z]+)*-AI\b'
                ai_systems = extract_variant_data(text_to_analyze, pattern)
                print("\n--- Знайдені ШІ-системи правопорядку у тексті ---")
                if ai_systems:
                    for item in set(ai_systems):
                        print(f" • {item}")
                else:
                    print("ШІ-систем правопорядку не знайдено.")

            elif choice == '4':
                sample_recipe = (
                    "Рецепт домашнього чизкейка:\n"
                    "Інгредієнти:\n"
                    "• Крем-сир - 500 г\n"
                    "• Цукор: 150 г\n"
                    "• Вершки - 200 мл\n"
                    "• Яйця: 3 шт\n"
                    "Інструкція приготування:\n"
                    "1. Збити крем-сир із цукром до однорідності.\n"
                    "2. Поступово ввести вершки та яйця.\n"
                    "3. Випікати при 160 градусах 60 хвилин."
                )
                print("\nТестовий рецепт:")
                print(sample_recipe)
                parsed = parse_recipe_details(sample_recipe)
                print("\n-> Вилучені інгредієнти:")
                for ing in parsed['ingredients']:
                    print(f"   - {ing['name']}: {ing['quantity']}")
                print("-> Вилучені кроки приготування:")
                for i, step in enumerate(parsed['steps'], start=1):
                    print(f"   {i}. {step}")

            elif choice == '5':
                print("Дякуємо за використання програми!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")


if __name__ == '__main__':
    main()