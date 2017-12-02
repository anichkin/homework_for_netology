import math
import osa


def convert_temperature(temperature):
    client = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    result = client.service.ConvertTemp(Temperature=temperature, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')
    return result


def average_temperature():
    with open('temps.txt', 'r') as f:
        sum_temperature = 0
        days = 0
        for line in f:
            temperature = line.split()
            sum_temperature += convert_temperature(temperature[0])
            days += 1
        average_temmperature = sum_temperature / days
        print('средняя температура в градусах Цельсия за', days, 'дней -', average_temmperature)


def convert_currency(currency_in, currency_out, amount):
    client = osa.Client("https://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    result = client.service.ConvertToNum(licenseKey=None, fromCurrency=currency_in, toCurrency=currency_out,
                                         amount=amount, rounding='true', date=None, type=None)
    return result


def travel_cost():
    with open('currencies.txt', 'r') as f:
        for line in f:
            travel_param = line.split()
            print(travel_param[0], math.ceil(convert_currency(travel_param[2], 'RUB', travel_param[1])), 'рублей')


def travel_lenght(lenght):
    client = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    result = client.service.ChangeLengthUnit(LengthValue=lenght, fromLengthUnit='Miles', toLengthUnit='Kilometers')
    return result


def travel_lenght_in_km():
    with open('travel.txt', 'r') as f:
        for line in f:
            travel_param = line.split()
            print(travel_param[0], round(travel_lenght(travel_param[1].replace(',', '')), 2), 'километров')


print('Подсчет средней температуры из файла temps.txt')
average_temperature()
print()
print('Перевод цен на путешествия в рубли из файла currencies.txt ')
travel_cost()
print()
print('Перевод расстояния в километры из файла travel.txt')
travel_lenght_in_km()