def celsius_para_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("A temperatura deve ser numérica.")

    fahrenheit = celsius * 9 / 5 + 32

    return round(fahrenheit, 2)


def fahrenheit_para_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("A temperatura deve ser numérica.")

    celsius = (fahrenheit - 32) * 5 / 9

    return round(celsius, 2)