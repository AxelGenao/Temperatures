from tkinter import Scale


class TemperatureScale:
    Kelvin = "°K"
    Fahrenheit = "°F"
    Celsius = "°C"

class Temperature():

    
    value = ""
    scale = ""

    
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    
    def Add(T1, T2):
        T1, T2 = Temperature.ConvertScales(T1, T2)

        result = Temperature(T1.value + T2.value, T1.scale)
        return result.value, result.scale

    def Substract(T1, T2):
        T1, T2 = Temperature.ConvertScales(T1, T2)

        result = Temperature(T1.value - T2.value, T1.scale)
        return result.value, result.scale

    def MultiplyBy(T1, T2):
        T1, T2 = Temperature.ConvertScales(T1, T2)

        result = Temperature(T1.value * T2.value, T1.scale)
        return result.value, result.scale

    def DivideBy(T1, T2):
        T1, T2 = Temperature.ConvertScales(T1, T2)

        if T2.value != 0:
            result = Temperature(T1.value / T2.value, T1.scale)
            return round(result.value, 6), result.scale
        else:
            raise ValueError("Can't divide by zero.")

    def ToFahrenheit(temp):
        if temp.scale == TemperatureScale.Kelvin:
            temp.value = (9 / 5) * (temp.value - 273.15) + 32
        elif temp.scale == TemperatureScale.Celsius:
            temp.value = ((9 / 5) * temp.value) + 32
        elif temp.scale != TemperatureScale.Fahrenheit:
            raise ValueError("Not a scale.")
        temp.scale = TemperatureScale.Fahrenheit
        return temp

    def ToCelsius(temp):
        if temp.scale == TemperatureScale.Fahrenheit:
            temp.value = (5 / 9) * (temp.value - 32)
        elif temp.scale == TemperatureScale.Kelvin:
            temp.value = temp.value - 273.15
        elif temp.scale != TemperatureScale.Celsius:
            raise ValueError("Not a scale.")
        temp.scale = TemperatureScale.Celsius
        return temp

    def ToKelvin(temp):
        if temp.scale == TemperatureScale.Celsius:
            temp.value = temp.value + 273.15
        elif temp.scale == TemperatureScale.Fahrenheit:
            temp.value = ((5 * (temp.value - 32)) / 9) + 273.15
        elif temp.scale != TemperatureScale.Kelvin:
            raise ValueError("Not a scale.")
        temp.scale = TemperatureScale.Kelvin
        return temp

    def ConvertScales(T1, T2):
        if T1.scale == TemperatureScale.Kelvin:
            T2 = Temperature.ToKelvin(T2)
        elif T1.scale == TemperatureScale.Celsius:
            T2 = Temperature.ToCelsius(T2)
        elif T1.scale == TemperatureScale.Fahrenheit:
            T2 = Temperature.ToFahrenheit(T2)
        else:
            raise ValueError("Not a scale.")
        return T1, 