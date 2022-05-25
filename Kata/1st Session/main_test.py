import unittest
import main

class TestMethods(unittest.TestCase):

    def test_Add(self):
        T1 = main.Temperature(2, main.TemperatureScale.Kelvin)
        T2 = main.Temperature(-2, main.TemperatureScale.Celsius)
        self.assertEqual(main.Temperature.Add(T1, T2), "")

    def test_Substract(self):
        T1 = main.Temperature(2, main.TemperatureScale.Kelvin)
        T2 = main.Temperature(-2, main.TemperatureScale.Celsius)
        self.assertEqual(main.Temperature.Substract(T1, T2), "")

    def test_MultiplyBy(self):
        T1 = main.Temperature(2, main.TemperatureScale.Kelvin)
        T2 = main.Temperature(-2, main.TemperatureScale.Celsius)
        self.assertEqual(main.Temperature.MultiplyBy(T1, T2), "")

    def test_DivideBy(self):
        T1 = main.Temperature(2, main.TemperatureScale.Kelvin)
        T2 = main.Temperature(-2, main.TemperatureScale.Celsius)
        self.assertEqual(main.Temperature.DivideBy(T1, T2), "")

if __name__ == "__main__":
    unittest.main()