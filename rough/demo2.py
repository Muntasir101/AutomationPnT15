import unittest


class calculate(unittest.TestCase):

    def test_method1(self):
        number1 = 100
        number2 = 5
        sum = number1 + number2
        print(sum)

    def test_method2(self):
        number1 = 100
        number2 = 5
        sub = number1 - number2
        print(sub)


if __name__ == '__main__':
    unittest.main(verbosity=2)
