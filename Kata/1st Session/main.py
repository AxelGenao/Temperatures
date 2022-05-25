from unittest import result


class TemperatureScale:
    Kelvin = "°K"
    Fahrenheit = "°F"
    Celsius = "°C"
    
    

class Temperature:

    
    value = 0
    scale = ""

    
    def __init__(value, scale):
        self.value = value
        self.scale = scale

    
    def Add(temp1, temp2):
        temp1, temp2 = Temperature.ConvertTemperatures(temp1, temp2)

        result = temp1.value + temp2.value
        return "Add:", result

    def Substract(temp1, temp2):
        temp1, temp2 = Temperature.ConvertTemperatures(temp1, temp2)

        result = temp1.value - temp2.value
        return "Subtract:", result

    def MultiplyBy(temp1, temp2):
        temp1, temp2 = Temperature.ConvertTemperatures(temp1, temp2)

        result = temp1.value * temp2.value
        return "Multiply:", result

    def DivideBy(temp1, temp2):
        temp1, temp2 = Temperature.ConvertTemperatures(temp1, temp2)

        result = temp1.value / temp2.value
        return "Divide:", result

    def ToFahrenheit(temp):
        if temp.scale == TemperatureScale.Celsius:
            temp.value = (temp.value * 1.8) + 32
        elif temp.scale == TemperatureScale.Kelvin:
            temp.value = 1.8 * (temp.value - 273) + 32
        elif temp.scale != TemperatureScale.Fahrenheit:
            print("Error, escala no existe.")
        temp.scale = TemperatureScale.Fahrenheit
        return temp.value, temp.scale

    def ToCelsius(temp):
        if temp.scale == TemperatureScale.Fahrenheit:
            temp.value = (temp.value - 32) / 1.8
        elif temp.scale == TemperatureScale.Kelvin:
            temp.value = temp.value - 273.15
        elif temp.scale != TemperatureScale.Celsius:
            print("Error, escala no existe.")
        temp.scale = TemperatureScale.Celsius
        return temp.value, temp.scale

    def ToKelvin(temp):
        if temp.scale == TemperatureScale.Celsius:
            temp.value = temp.value + 273.15
        elif temp.scale == TemperatureScale.Fahrenheit:
            temp.value = ((temp.value - 32) * (5/9)) + 273.15
        elif temp.scale != TemperatureScale.Kelvin:
            print("Error, escala no existe.")
        temp.scale = TemperatureScale.Kelvin
        return temp.value, temp.scale

    def ConvertTemperatures(T1, T2):
        if T1.scale == TemperatureScale.Celsius:
            T2 = Temperature.ToCelsius(T2)
        elif T1.scale == TemperatureScale.Fahrenheit:
            T2 = Temperature.ToFahrenheit(T2)
        elif T1.scale == TemperatureScale.Kelvin:
            T2 = Temperature.ToKelvin(T2)
        else:
            print("Error, escala no existente.")

        return T1, 