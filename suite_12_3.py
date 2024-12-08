# Домашнее задание по теме "Систематизация и пропуск тестов".
# Код создан в учебных целях с полными комментариями для себя.

import unittest  # Импорт модуля unittest для проведения юнит-тестирования
from tests_12_3 import RunnerTest, TournamentTest  # Импорт классов RunnerTest и TournamentTest из модуля tests_12_3

# Часть 1. TestSuit
loader = unittest.TestLoader()  # Создаем объект TestLoader для загрузки тестов
suite = loader.loadTestsFromTestCase(RunnerTest)  # Загружаем тесты из класса RunnerTest
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))  # Добавляем тесты из класса TournamentTest в набор suite

runner = unittest.TextTestRunner(verbosity=2)  # Создаем объект TextTestRunner с уровнем детализации вывода 2
result = runner.run(suite)  # Запускаем выполнение тестов из набора suite