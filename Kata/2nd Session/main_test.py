from multiprocessing.managers import ValueProxy
import unittest
import main

class TestMain(unittest.TestCase):

    def test_Add(self):
        a = main.Temperature(2, main.TemperatureScale.Kelvin)
        b = main.Temperature(-2, main.TemperatureScale.Celsius)
        result = main.Temperature.Add(a, b)
        self.assertEqual(result, (273.15, main.TemperatureScale.Kelvin))


    def test_Substract(self):
        a = main.Temperature(2, main.TemperatureScale.Kelvin)
        b = main.Temperature(-2, main.TemperatureScale.Celsius)
        result = main.Temperature.Substract(a, b)
        self.assertEqual(result, (-269.15, main.TemperatureScale.Kelvin))

    def test_MultiplyBy(self):
        a = main.Temperature(2, main.TemperatureScale.Kelvin)
        b = main.Temperature(-2, main.TemperatureScale.Celsius)
        result = main.Temperature.MultiplyBy(a, b)
        self.assertEqual(result, (542.3, main.TemperatureScale.Kelvin))

    def test_DivideBy(self):
        a = main.Temperature(2, main.TemperatureScale.Kelvin)
        b = main.Temperature(-2, main.TemperatureScale.Celsius)
        result = main.Temperature.DivideBy(a, b)
        self.assertEqual(result, (0.007376, main.TemperatureScale.Kelvin))

        a = main.Temperature(2, main.TemperatureScale.Kelvin)
        b = main.Temperature(0, main.TemperatureScale.Kelvin)
        self.assertRaises(ValueError, main.Temperature.DivideBy, a, b)

if __name__ == "__main__":
    unittest.main()