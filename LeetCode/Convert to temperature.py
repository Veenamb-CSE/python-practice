class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        list=[]
        Kelvin = (celsius + 273.15)
        Fahrenheit = celsius * 1.80 + 32.00
        list.insert(0, Kelvin)
        list.insert(1, Fahrenheit)
        return list
