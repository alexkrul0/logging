import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.run1 = Runner('Runner 1', -5)
            for i in range(0, 10):
                self.run1.walk()
            self.assertEqual(self.run1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.run2 = Runner( 2)
            for i in range(0, 10):
                self.run2.run()
            self.assertEqual(self.run2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.run3 = Runner('Runner 3')
        self.run4 = Runner('Runner 4')
        for i in range(0, 10):
            self.run3.run()
            self.run4.walk()
        self.assertNotEqual(self.run3.distance, self.run4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()