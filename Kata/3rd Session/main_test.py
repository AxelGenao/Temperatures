import unittest
import main

class TestMain(unittest.TestCase):

    def test_Add(self):
        T1 = main.Temperature(2, main.Scales.Kelvin)
        T2 = main.Temperature(-2, main.Scales.Celsius)
        self.assertEqual(main.Temperature.Add(T1, T2), "273.15 °K")

        T1 = main.Temperature(2, main.Scales.Celsius)
        T2 = main.Temperature(-2, main.Scales.Celsius)
        self.assertEqual(main.Temperature.Add(T1, T2), "0 °C")

        T1 = main.Temperature(2, main.Scales.Fahrenheit)
        T2 = main.Temperature(-2, main.Scales.Celsius)
        self.assertEqual(main.Temperature.Add(T1, T2), "30.4 °F")

    def test_Substract(self):
        T1 = main.Temperature(2, main.Scales.Celsius)
        T2 = main.Temperature(-2, main.Scales.Fahrenheit)
        self.assertEqual(main.Temperature.Substract(T1, T2), "20.88889 °C")

        T1 = main.Temperature(2, main.Scales.Fahrenheit)
        T2 = main.Temperature(-2, main.Scales.Fahrenheit)
        self.assertEqual(main.Temperature.Substract(T1, T2), "4 °F")

        T1 = main.Temperature(2, main.Scales.Fahrenheit)
        T2 = main.Temperature(2, main.Scales.Fahrenheit)
        self.assertEqual(main.Temperature.Substract(T1, T2), "0 °F")

        T1 = main.Temperature(2, main.Scales.Kelvin)
        T2 = main.Temperature(-2, main.Scales.Fahrenheit)
        self.assertEqual(main.Temperature.Substract(T1, T2), "-252.26111 °K")

    def test_MultiplyBy(self):
        T1 = main.Temperature(2, main.Scales.Fahrenheit)
        T2 = main.Temperature(-2, main.Scales.Kelvin)
        self.assertEqual(main.Temperature.MultiplyBy(T1, T2), "-926.54 °F")

        T1 = main.Temperature(2, main.Scales.Kelvin)
        T2 = main.Temperature(-2, main.Scales.Kelvin)
        self.assertEqual(main.Temperature.MultiplyBy(T1, T2), "-4 °K")

        T1 = main.Temperature(2, main.Scales.Celsius)
        T2 = main.Temperature(-2, main.Scales.Kelvin)
        self.assertEqual(main.Temperature.MultiplyBy(T1, T2), "-550.3 °C")

    def test_DivideBy(self):
        # Positive Scenario
        T1 = main.Temperature(-275.15, main.Scales.Celsius)
        T2 = main.Temperature(-2, main.Scales.Kelvin)
        self.assertEqual(main.Temperature.DivideBy(T1, T2), "1.0 °C")

        T1 = main.Temperature(-23, main.Scales.Celsius)
        T2 = main.Temperature(-5, main.Scales.Kelvin)
        self.assertEqual(main.Temperature.DivideBy(T1, T2), "0.08269 °C")

        #Negative Scenario (Divide by Zero)
        T1 = main.Temperature(2, main.Scales.Kelvin)
        T2 = main.Temperature(-273.15, main.Scales.Celsius)
        self.assertRaises(ValueError, main.Temperature.DivideBy, T1, T2)

if __name__ == "__main__":
    unittest.main()