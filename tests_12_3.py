# Домашнее задание по теме "Систематизация и пропуск тестов".
# Код создан в учебных целях с полными комментариями для себя.

import runner  # Импортируем модуль runner, содержащий определение класса Runner
import runner_and_tournament  # Импортируем модуль runner_and_tournament, содержащий определения классов Runner и Tournament
import unittest  # Импортируем модуль unittest, необходимый для написания и выполнения юнит-тестов

class RunnerTest(unittest.TestCase):  # Наследуем класс RunnerTest от unittest.TestCase
    is_frozen = False  # Устанавливаем атрибут is_frozen как False для этого класса

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_walk(self):
        runn = runner.Runner("Олег")  # Создаём экземпляр класса Runner с именем "Олег"
        for _ in range(10):  # Выполняем цикл 10 раз
            runn.walk()  # Вызываем метод walk() у экземпляра runn
        self.assertEqual(runn.distance, 50)  # Проверяем, что расстояние равно 50

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_run(self):
        runn = runner.Runner("Пётр")  # Создаём экземпляр класса Runner с именем "Пётр"
        for _ in range(10):  # Выполняем цикл 10 раз
            runn.run()  # Вызываем метод run() у экземпляра runn
        self.assertEqual(runn.distance, 100)  # Проверяем, что расстояние равно 100

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_challenge(self):
        runn1 = runner.Runner("Никита")  # Создаём первый экземпляр класса Runner с именем "Никита"
        runn2 = runner.Runner("Алиса")  # Создаём второй экземпляр класса Runner с именем "Алиса"
        for _ in range(10):  # Выполняем цикл 10 раз
            runn1.run()  # Вызываем метод run() у первого экземпляра runn1
            runn2.walk()  # Вызываем метод walk() у второго экземпляра runn2
        self.assertNotEqual(runn1.distance, runn2.distance)  # Проверяем, что расстояния не равны

class TournamentTest(unittest.TestCase):  # Наследуем класс TournamentTest от unittest.TestCase
    is_frozen = True  # Устанавливаем атрибут is_frozen как True для этого класса

    @classmethod
    def setUpClass(cls):  # Метод, вызываемый перед всеми тестами в классе
        cls.all_results = {}  # Инициализируем словарь для хранения результатов

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска метода, если is_frozen=True
    def setUp(self):  # Метод, вызываемый перед каждым тестом
        self.usain = runner_and_tournament.Runner('Usain', 10)  # Создаём экземпляр класса Runner с именем Usain и скоростью 10
        self.andrey = runner_and_tournament.Runner('Andrey', 9)  # Создаём экземпляр класса Runner с именем Andrey и скоростью 9
        self.nick = runner_and_tournament.Runner('Nick', 3)  # Создаём экземпляр класса Runner с именем Nick и скоростью 3

    @classmethod
    def tearDownClass(cls):  # Метод, вызываемый после всех тестов в классе
        for key, value in cls.all_results.items():  # Проходимся по словарю all_results
            print("{")  # Печатаем открывающую фигурную скобку
            for k, v in value.items():  # Проходимся по каждому элементу внутри value
                print(f"\t{k}: {v},")  # Печатаем ключ и значение с отступом
            print("}")  # Печатаем закрывающую фигурную скобку

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nick)  # Создаём турнир с двумя участниками
        result = tournament.start()  # Запускаем турнир и получаем результаты
        self.all_results['usain_and_nick'] = result  # Сохраняем результаты в словарь all_results
        last_place_runner = max(result.keys())  # Находим участника, пришедшего последним
        self.assertTrue(result[last_place_runner].name == 'Nick')  # Проверяем, что последний участник - это Nick

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)  # Создаём турнир с двумя участниками
        result = tournament.start()  # Запускаем турнир и получаем результаты
        self.all_results['andrey_and_nick'] = result  # Сохраняем результаты в словарь all_results
        last_place_runner = max(result.keys())  # Находим участника, пришедшего последним
        self.assertTrue(result[last_place_runner].name == 'Nick')  # Проверяем, что последний участник - это Nick

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор для пропуска теста, если is_frozen=True
    def test_all_three(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nick)  # Создаём турнир с тремя участниками
        result = tournament.start()  # Запускаем турнир и получаем результаты
        self.all_results['all_three'] = result  # Сохраняем результаты в словарь all_results
        last_place_runner = max(result.keys())  # Находим участника, пришедшего последним
        self.assertTrue(result[last_place_runner].name == 'Nick')  # Проверяем, что последний участник - это Nick

if __name__ == "__main__":  # Если скрипт запущен напрямую, а не импортирован
    unittest.main()  # Запускаем все тесты