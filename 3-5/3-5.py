import math
import requests
from xml.etree.ElementTree import fromstring


def convert_temperature(temperature):
    response = requests.post(
        'http://www.webservicex.net/ConvertTemperature.asmx',
        headers={
            'Content-Type': 'text/xml'
        },
        data=('<?xml version="1.0" encoding="utf-8"?>\n'
              '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
              'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n '
              '  <soap:Body>\n'
              '    <ConvertTemp xmlns="http://www.webserviceX.NET/">\n'
              '      <Temperature>') + temperature + ('</Temperature>\n'
              '      <FromUnit>degreeFahrenheit</FromUnit>\n'
              '      <ToUnit>degreeCelsius</ToUnit>\n'
              '    </ConvertTemp>\n'
              '  </soap:Body>\n'
              '</soap:Envelope>')

    )
    return float(fromstring(response.text)[0][0][0].text)


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
    response = requests.post(
        'https://fx.currencysystem.com/webservices/CurrencyServer4.asmx',
        headers={
            'Content-Type': 'text/xml',
        },
        data=('<?xml version="1.0" encoding="utf-8"?>\n'
              '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
              'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n '
              '  <soap:Body>\n'
              '    <ConvertToNum xmlns="http://webservices.cloanto.com/currencyserver/">\n'
              '      <licenseKey></licenseKey>\n'
              '      <fromCurrency>') + currency_in + ('</fromCurrency>\n'
              '      <toCurrency>') + currency_out + ('</toCurrency>\n'
              '      <amount>') + amount + ('</amount>\n'
              '      <rounding>true</rounding>\n'
              '      <date></date>\n'
              '      <type></type>\n'
              '    </ConvertToNum>\n'
              '  </soap:Body>\n'
              '</soap:Envelope>\n')

    )
    return float(fromstring(response.text)[0][0][0].text)


def travel_cost():
    with open('currencies.txt', 'r') as f:
        for line in f:
            travel_param = line.split()
            print(travel_param[0], math.ceil(convert_currency(travel_param[2], 'RUB', travel_param[1])), 'рублей')


def travel_lenght(lenght):
    response = requests.post(
        'http://www.webservicex.net/length.asmx',
        headers={
            'Content-Type': 'text/xml',
        },
        data=('<?xml version="1.0" encoding="utf-8"?>\n'
              '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
              'xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n '
              '  <soap:Body>\n'
              '    <ChangeLengthUnit xmlns="http://www.webserviceX.NET/">\n'
              '      <LengthValue>') + lenght + ('</LengthValue>\n'
              '      <fromLengthUnit>Miles</fromLengthUnit>\n'
              '      <toLengthUnit>Kilometers</toLengthUnit>\n'
              '    </ChangeLengthUnit>\n'
              '  </soap:Body>\n'
              '</soap:Envelope>')

    )
    return float(fromstring(response.text)[0][0][0].text)


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
