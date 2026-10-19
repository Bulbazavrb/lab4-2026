"""
Тести для перевірки функцій лабораторної роботи № 4 (Варіант 12)
"""

import unittest
import sys
import os

# Автоматичне додавання шляхів для пошуку lab4.py незалежно від місця запуску
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
src_dir = os.path.abspath(os.path.join(parent_dir, 'src'))

for p in [src_dir, parent_dir, current_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from lab4 import (
        find_substring,
        replace_substring,
        split_text,
        format_string_f,
        format_string_method,
        extract_emails,
        validate_phone_number,
        extract_hashtags,
        extract_mentions,
        count_words,
        count_sentences,
        word_frequency,
        extract_law_enforcement_ai,
        parse_recipe_details
    )
except ImportError as err:
    print(f"\n[!] Помилка імпорту lab4: {err}")
    print("Переконайтеся, що файл 'lab4.py' розташований у папці 'src' або у головній папці проекту.")
    input("\nНатисніть Enter для виходу...")
    sys.exit(1)


class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("Python", "Java"), -1)

    def test_replace_substring(self):
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])

    def test_format_string_f(self):
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")

    def test_format_string_method(self):
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")

    def test_extract_emails(self):
        text = "Контакти: info@example.com, support@test.ua та wrong-email@"
        expected = ["info@example.com", "support@test.ua"]
        self.assertEqual(extract_emails(text), expected)

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertTrue(validate_phone_number("380671112233"))
        self.assertTrue(validate_phone_number("0509998877"))
        self.assertFalse(validate_phone_number("12345"))
        self.assertFalse(validate_phone_number("+38012345678999"))

    def test_extract_hashtags(self):
        text = "Тестуємо #Python, #Dota2 та #CyberSport!"
        expected = ["#Python", "#Dota2", "#CyberSport"]
        self.assertEqual(extract_hashtags(text), expected)

    def test_extract_mentions(self):
        text = "Вітаємо @developer та @admin у чаті!"
        expected = ["@developer", "@admin"]
        self.assertEqual(extract_mentions(text), expected)

    def test_count_words(self):
        self.assertEqual(count_words("Це тестове речення для перевірки кількості слів."), 7)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("Перше речення. Друге речення! Третє речення?"), 3)

    def test_word_frequency(self):
        freq = word_frequency("дота гра дота турнір гра дота")
        self.assertEqual(freq['дота'], 3)
        self.assertEqual(freq['гра'], 2)

    def test_variant_12_ai_extraction(self):
        text = "Безпеку забезпечує LawForce-AI, а моніторинг веде Patrol-AI."
        expected = ["LawForce-AI", "Patrol-AI"]
        self.assertEqual(extract_law_enforcement_ai(text), expected)

    def test_variant_12_recipe_parser(self):
        sample_recipe = (
            "• Борошно - 300 г\n"
            "• Вода: 150 мл\n"
            "1. Замісити тісто.\n"
            "2. Залишити на 30 хвилин."
        )
        data = parse_recipe_details(sample_recipe)
        self.assertEqual(len(data['ingredients']), 2)
        self.assertEqual(data['ingredients'][0]['name'], "Борошно")
        self.assertEqual(data['ingredients'][0]['quantity'], "300 г")
        self.assertEqual(len(data['steps']), 2)
        self.assertEqual(data['steps'][0], "Замісити тісто.")


if __name__ == '__main__':
    # Створюємо Runner і перехоплюємо вихід, щоб вікно cmd не закривалося
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestTextAnalyzer)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 50)
    print(f"Всього тестів пройдено: {result.testsRun}")
    print(f"Успішних: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Помилок: {len(result.failures) + len(result.errors)}")
    print("=" * 50)

    # Цей рядок блокує закриття вікна
    input("\nНатисніть Enter для виходу...")